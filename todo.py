import sys
import time
import os

import tests

listTaskArgs = ["-tasks", "-t"]
listListsArgs = ["-lists", "-l"]
addArgs = ["-add", "-a"]
deleteArgs = ["-delete", "-d"]
checkArgs = ["-check", "-c", "-x"]
switchArgs = ["-switch", "-s"]
setListArgs = ["-setlist", "-sl"]
helpArgs = ["-help", "-h"]
testArgs = ["-test"]

class Main:
    def main():
        # Defaults
        allTaskListsFileName = "all-task-lists"
        allTaskListsPath = "."
        task = None
        taskListPath = "tasklists"
        resetChecked = None

        taskList = Main.getCurrentTaskList(allTaskListsFileName, allTaskListsPath)

        # TODO: groom/trigger reset

        argC = len(sys.argv)
        argIndex = 1
        while argIndex < argC:
            arg = sys.argv[argIndex].lower()

            # List curret todo list ()
            if(arg in listTaskArgs):
                formatRes = Main.formatPrintList(taskList, taskListPath)
                for line in formatRes:
                    print(line)

                argIndex += 1
                continue

            # Add a task
            elif(arg in addArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: task (string), resetChecked (enum)(optional)")
                    quit()

                task = sys.argv[argIndex + 1]

                # TODO: reset args for automatically resetting the "completed" value after a predefined time, consider having a interval and a datetime so the reset triggers on an interval from datetime given
                # hour reset after completed easiest? h 2 -> write Z or T + datetime first in line, when next list is called, check timestamp, compare to reset time in args, 
                #   if past, uncheck (or better set utc datetime + reset time check if datetime is current or in past, if yes, uncheck)
                # datetime?
                # enum: daily, hourly, month, year, weekly.. ?
                # give datetime + interval, or just interval (datetime = now). When interval interact with datetime, reset, then set new datetime = old datetime + interval?
                    # better to set datetime + interval = datetimeTriggerAlert? vs check datet

                optionalArgIndex = 0
                if(argC > argIndex + 3 and sys.argv[argIndex + 2][0] != "-"):
                    resetChecked = sys.argv[argIndex + 2]
                    optionalArgIndex += 1
                    
                saveRes = Main.addTask(task, taskList, taskListPath)
                print("Add task " + ("was successful." if saveRes else "failed."))

                argIndex += 2 + optionalArgIndex
                continue

            # Delete a task
            elif(arg in deleteArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: tasknumber (int)")
                    quit()
                
                taskNumber = int(sys.argv[argIndex + 1]) - 1

                delRes = Main.editTask([taskNumber], taskList, taskListPath, "delete", "w")
                print(("Successfully" if delRes else "Failed to") + " delete task.")

                argIndex += 2
                continue

            # Toggle check/tick off a task (mark as done)
            elif(arg in checkArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to check task, need at least 1: tasknumber (int)")
                    quit()
                
                taskNumber = int(sys.argv[argIndex + 1]) - 1

                checkRes = Main.editTask([taskNumber], taskList, taskListPath, "check", "w")
                print(("Successfully" if checkRes else "Failed to") + " check task.")

                argIndex += 2
                continue

            # Switch tasks position
            elif(arg in switchArgs):
                if(argC - argIndex < 3):
                    print("Too few arguments to switch task, need at least 2: tasknumber (int), switchnumber (int)")
                    quit()

                taskNumber = int(sys.argv[argIndex + 1]) - 1
                switchNumber = int(sys.argv[argIndex + 2]) - 1
                
                switchRes = Main.editTask([taskNumber, switchNumber], taskList, taskListPath, "switch", "w")
                print(("Successfully" if switchRes else "Failed to") + " switched tasks.")

                argIndex += 3
                continue

            # Set the current list of tasks
            elif(arg in setListArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: task list (string)")
                    quit()
                    
                newTaskList = sys.argv[argIndex + 1]
                setRes = Main.setList(newTaskList, allTaskListsFileName, allTaskListsPath)
                print(("Successfully" if setRes else "Failed to") + " set task list to " + newTaskList + ".")

                argIndex += 2
                continue

            # Help
            elif(arg in helpArgs):
                Main.printHelp()
                quit()

            # Tests
            elif(arg in testArgs):
                useBeforeAfter = 1

                if(argC > argIndex + 1 and sys.argv[argIndex + 1][0] != "-"):
                    useBeforeAfter = int(sys.argv[argIndex + 1])
                    
                tests.Tests.runTests(useBeforeAfter)
                quit()

            # Invalid, inform and quit
            else:
                print("Argument not recognized: \"" + arg + "\", please see documentation or run with \"-help\" for help.")

            argIndex += 1

        if(argC < 2):
            formatRes = Main.formatPrintList(taskList, taskListPath)
            for line in formatRes:
                print(line)
        
    def getFullFilePath(dirPath, fileName = None):
        """
        A method for getting the full path from root file the script is called from and a sub-directory with optional file. \n
        string dirPath \n
        string fileName(optional)
        """

        appendPath = dirPath
        if(fileName != None):
            appendPath = os.path.join(dirPath, fileName + ".txt")

        return os.path.join(sys.path[0], appendPath)

    def getCurrentTaskList(allTaskListsFileName, allTaskListsPath, defaultTaskListName = "default"):
        """
        A method for returning the current tasklist used (first result in file allTaskListsFileName). If there is no file, this will make one. \n
        string allTaskListsFileName \n
        string allTaskListsPath \n
        string defaultTaskListName(optional)
        """

        allTaskListsRes = Main.loadFile(allTaskListsFileName, allTaskListsPath)
        fileExists = True if len(allTaskListsRes) > 0 else False

        if(fileExists):
            return allTaskListsRes[0].rstrip()

        allTaskListsFullPath = Main.getFullFilePath(allTaskListsPath, allTaskListsFileName)
        try:
            with open(allTaskListsFullPath, "a") as file:
                file.write(defaultTaskListName)

            file.close()
        except Exception as e:
            # print("\ntestloadFileEmptyList error: ")
            # print(e)
            return None

        allTaskListsRes = Main.loadFile(allTaskListsFileName, allTaskListsPath)
        fileExists = True if len(allTaskListsRes) > 0 else False

        if(fileExists):
            return allTaskListsRes[0].rstrip()

        return None

    def addTask(task, taskList, taskListPath):
        """
        A method for saving/adding a task "task" to the list "taskList" in directory "taskListPath". \n
        string task \n
        string taskList \n
        string taskListPath
        """

        if(task.rstrip() == ""):
            return False

        loadTaskRes = Main.loadFile(taskList, taskListPath)
        fileExists = True if len(loadTaskRes) > 0 else False

        # If no directory for task lists exist, make one
        taskListDirectory = Main.getFullFilePath(taskListPath)
        if(not os.path.exists(taskListDirectory)):
            os.mkdir(taskListDirectory)

        fullPath = Main.getFullFilePath(taskListPath, taskList)
        taskLine = ("\n" if fileExists else "") + "0 " + task

        try:
            with open(fullPath, "a") as file:
                file.write(taskLine) 

            file.close() 
            return True
        except Exception as e:
            print("\naddTask error:")
            print(e)
            return False

    def loadFile(taskList, taskListPath):
        """ 
        A method that reads file and returns an array of the content. \n
        string taskList \n
        string taskListPath
        """

        fullPath = Main.getFullFilePath(taskListPath, taskList)

        res = []
        try:
            with open(fullPath, "r") as file:
                for line in file:
                    res.append(line)

            file.close() 
        except Exception as e:
            # print("Error loading task list " + taskList)
            # print("\nloadFile error: ")
            # print(e)
            uselessVar = True

        return res

    def editTask(taskRefrence, taskList, taskListPath, action, filePermissions = "w"):
        """
        A method editing a tasklist. \n
        int array taskRefrence \n
        string taskList \n
        string taskListPath \n
        string action \n
        string filePermissions
        """

        fullPath = Main.getFullFilePath(taskListPath, taskList)

        fileArray = []
        # Read
        try:
            with open(fullPath, "r") as readFile:
                for line in readFile:
                    fileArray.append(line)

            readFile.close()
        except Exception as e:
            print("\neditTask readFile error:")
            print(e)
            return False

        if(len(fileArray) == 0):
            print("The task list " + taskList + " is empty.")
            quit()

        try:
            taskNumber = int(taskRefrence[0])
        except Exception as e:
            print("\neditTask readFile error:")
            print(e)
            return False


        if(taskNumber < 0 or taskNumber > (len(fileArray) - 1)):
            print("Invalid task number, for task list " + taskList + " minimum is 1 and maximum is " + str(len(fileArray)))
            return False

        # Edit array
        if(action == "check"):
            if(fileArray[taskNumber][0] == "0" or fileArray[taskNumber][0] == "1"):
                fileArray[taskNumber] = ("1" if fileArray[taskNumber][0] == "0" else "0") + fileArray[taskNumber][1:]
            else:
                return False

        elif(action == "delete"):
            fileArray.pop(taskNumber)

            # Delete first line, no need to strip revious line of newline
            if(taskNumber != 0):
                fileArray[len(fileArray) - 1] = fileArray[len(fileArray) - 1].rstrip()

        elif(action == "switch"):
            try:
                switchNumber = int(taskRefrence[1])
                if(taskNumber < 0 or taskNumber > (len(fileArray) - 1)):
                    print("Invalid switch number, for task list " + taskList + " minimum is 1 and maximum is " + str(len(fileArray)))
                    return False
                    
                tmp = fileArray[taskNumber].rstrip()
                fileArray[taskNumber] = fileArray[switchNumber].rstrip() + "\n"
                fileArray[switchNumber] = tmp

            except Exception as e:
                print("\neditTask readFile error:")
                print(e)
                return False
            
        else:
            print("Action not recognized, must be \"check\", \"delete\", \"switch\"")
            return False

        # Write back to array
        try:
            with open(fullPath, filePermissions) as writeFile:
                index = 0
                while index < len(fileArray):
                    writeFile.write(fileArray[index])
                    index += 1

            writeFile.close() 
            return True
        except Exception as e:
            print("\neditTask writeFile error:")
            print(e)
            return False

    def setList(taskList, allTaskListsFileName, allTaskListsPath):
        """
        A method for setting current task list. \n
        string taskList \n
        string allTaskListsFileName \n
        string allTaskListsPath
        """

        currentTaskList = Main.getCurrentTaskList(allTaskListsFileName, allTaskListsPath)
        if(taskList == currentTaskList):
            return True

        allTaskListsFullPath = Main.getFullFilePath(allTaskListsPath, allTaskListsFileName)
        try:
            with open(allTaskListsFullPath, "w") as file:
                file.write(taskList)

            file.close()
        except Exception as e:
            # print("\ntestloadFileEmptyList error: ")
            # print(e)
            return False

        return True

    def mendTaskList(taskList, taskListPath):
        print("WIP")

    def formatPrintList(taskList, taskListPath, retry = False):
        """
        A method for formatting the task in a task list in a legible manner. \n
        string taskList \n
        string taskListPath
        """

        if(not retry):
            # Prints should be added to return array at the end of method, or sent separatly, though other array (array of metadata array and content array, aka wrap) or on separate method
            # Legend for task list
            print("From task list: " + taskList)
            print("#" + "\t" + "Completed?" + "\t" + "Task name" + "\t" + "Next reset")

        tasks = Main.loadFile(taskList, taskListPath)
        if(len(tasks) == 0):
            print("The task list " + taskList + " is empty.")
            return []
        

        printArray = []

        nTasks = len(tasks)
        index = 0
        while index < nTasks:
            task = tasks[index].rstrip()
            
            taskReset = ""
            # TODO
            # if(task[1][0] == "Z"):
            #     taskReset = task[1]

            try:
                taskCompleted = "Yes" if int(task[0]) == 1 else "No"
                taskText = str(task[1:]).rstrip()

                if(len(taskText) < 1):
                    raise Exception
                
                printArray.append(str(index + 1) + "\t" + str(taskCompleted) + "\t\t" + str(taskText) + "\t" + str(taskReset))
            except:
                # TODO extract to method
                # mendRes = Main.mendTaskList(taskList, taskListPath)

                # Malformed line, attempt to fix it, if it's empty, remove it.
                taskLine = str(task).rstrip()
                
                # taskLine is empty string ("") or only contains a complete number ("0"/"1"), delete line
                if(len(taskLine) < 1 or len(taskLine[1:]) < 1):
                    Main.editTask([index], taskList, taskListPath, "delete")

                # taskLine has no complete number ("0"/"1"), but has a task, add task again
                elif(taskLine[0] != "0" and taskLine[0] != "1"):
                    Main.editTask([index], taskList, taskListPath, "delete")
                    Main.addTask(taskLine, taskList, taskListPath)

                    # TODO insert new task line to index where it was
                    # Main.editTask([len(tasks), index], taskList, taskListPath, "insert")

                # Unknown error, implore the user fix and quit
                else:
                    printArray.append("This task, number " + str(index + 1) + " was malformed. Please delete and add it again before trying agian. The text is: \"" + task + "\"")
                    quit()
                    
                # Though recursion, run method again, this should load the fixed file into memory and recursivly fix the 
                # file when it finds an error untill all is well or it hits the else part above.
                return Main.formatPrintList(taskList, taskListPath, True)

            index += 1

        return printArray

    # no completed number
    # 0 next is blank

    # 0 next is no task
    # 0

    # listTaskArgs = ["-tasks", "-t"]
    # listListsArgs = ["-lists", "-l"]
    # deleteArgs = ["-delete", "-d"]
    # checkArgs = ["-check", "-c", "-x"]
    # switchArgs = ["-switch", "-s"]
    # setListArgs = ["-setList", "-sl"]
    # helpArgs = ["-help", "-h"]
    # testArgs = ["-test"]

    def printHelp():
        """
        A simple console print that informs user of program arguments.
        """

        print("--- Help ---")
        print("Arguments marked with ? are optional.")
        print("All arguments that triggers a function start with dash(-).")
        print("All arguments must be separated by space only.")
        print("To submit sentences with spaces beween words, use quotation marks (\", \'), othwerwise they will be counted as separate arguments.")
        print("\te.g.: $ python todo.py -add \"This is a sentence.\"")
        print("\n")

        print(str(listTaskArgs) + ": prints an indexed list of tasks in the current task list.")
        # print(str(listListsArgs) + ": prints a list of all task lists.")
        print(str(addArgs) + " + string + ?taskList: adds the following string to the current task list.")
        print(str(deleteArgs) + " + number + ?taskList: deletes the corresponding task in the current task list.")
        print(str(checkArgs) + " + number: toggle the completetion of the corresponding task in the current task list.")
        print(str(switchArgs) + "+ number + number: switches the position of the two corresponding tasks in the current task list.")
        print(str(setListArgs) + ": string: sets the current task list to the string given.")
        print(str(helpArgs) + ": prints this information about input arguments.")
        print(str(testArgs) + ": runs unit tests and prints the result.")
            
if __name__ == "__main__":
    Main.main()