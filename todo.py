import sys
import time
import os

import tests

listArgs = ["-list", "-ls"]
addArgs = ["-add", "-a"]
deleteArgs = ["-delete", "-d"]
checkArgs = ["-check", "-c", "-x", "-tick", "-t"]
switchArgs = ["-switch", "-s"]
changeListArgs = ["-changelist", "-cl"]
helpArgs = ["-help", "-h"]
testArgs = ["-test"]

class Main:
    def main():
        # Defaults
        task = None
        taskList = "default"
        taskListPath = "tasklists"
        resetChecked = None

        # TODO: groom/trigger reset


        argC = len(sys.argv)
        argIndex = 1
        while argIndex < argC:
            arg = sys.argv[argIndex].lower()

            # List curret todo list ()
            if(arg in listArgs):
                Main.printList(taskList, taskListPath)
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

                delRes = Main.editTask(taskNumber, taskList, taskListPath, "delete", "w")
                print(("Successfully" if delRes else "Failed to") + " delete task.")

                argIndex += 2
                continue

            # Toggle check/tick off a task (mark as done)
            elif(arg in checkArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: tasknumber (int)")
                    quit()
                
                taskNumber = int(sys.argv[argIndex + 1]) - 1

                tickRes = Main.editTask(taskNumber, taskList, taskListPath, "tick", "w")
                print(("Successfully" if tickRes else "Failed to") + " tick task.")

                argIndex += 2
                continue

            # Switch tasks position
            elif(arg in switchArgs):
                print("switch")

            # Change list of tasks
            elif(arg in changeListArgs):
                print("cl")

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
            Main.printList(taskList, taskListPath)

        print("\nend")

        
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

    def addTask(task, taskList, taskListPath):
        """
        A method for saving/adding a task "task" to the list "taskList" in directory "taskListPath". \n
        string task \n
        string taskList \n
        string taskListPath
        """

        fullPath = Main.getFullFilePath(taskListPath, taskList)

        fileExists = False
        try:
            with open(fullPath, "r") as file:
                fileExists = True

            file.close()
        except FileNotFoundError:
            fileExists = False

        # If no directory for task lists exist, make one
        taskListDirectory = Main.getFullFilePath(taskListPath)
        if(not os.path.exists(taskListDirectory)):
            os.mkdir(taskListDirectory)

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

    def loadTaskList(taskList, taskListPath):
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
            print("Error loading task list " + taskList)
            print("\nloadTaskList error: ")
            print(e)

        return res

    # idea: a generic editing method can let me add (append), delete, change check status, set new reset time etc
    def editTask(taskNumber, taskList, taskListPath, action, filePermissions = "rw+"):
        """
        A method editing a tasklist. \n
        int taskNumber \n
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
        if(taskNumber < 0 or taskNumber > (len(fileArray) - 1)):
            print("Invalid task number, for task list " + taskList + " minimum is 1 and maximum is " + str(len(fileArray)))
            quit()


        taskNumber = int(taskNumber)
        # Edit array
        if(action == "tick"):
            fileArray[taskNumber] = ("1" if fileArray[taskNumber][0] == "0" else "0") + fileArray[taskNumber][1:]
        elif(action == "delete"):
            fileArray.pop(taskNumber)
            fileArray[len(fileArray) - 1] = fileArray[len(fileArray) - 1].rstrip()
        else:
            print("Action not recognized, must be \"tick\", \"delete\"")
            quit()

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

    def setList(taskList, taskListPath):
        """
        A method for changeing current default task list, so a argument to save or read from a list is not necessary. \n
        string taskList \n
        string taskListPath
        """

        print("--- setList ---")

    def printList(taskList, taskListPath):
        """
        A method for formatting the task in a task list in a legible manner. \n
        string taskList \n
        string taskListPath
        """

        tasks = Main.loadTaskList(taskList, taskListPath)
        if(len(tasks) == 0):
            print("The task list " + taskList + " is empty.")
            quit()
        
        # Legend for task list
        print("#" + "\t" + "Completed?" + "\t" + "Task name" + "\t" + "Next reset")

        nTasks = len(tasks)
        index = 0
        while index < nTasks:
            task = tasks[index].rstrip()
            
            taskReset = ""
            # TODO
            # if(task[1][0] == "Z"):
            #     taskReset = task[1]

            try:
                taskCompleted = "Yes" if task[0] == "1" else "No"
                taskText = task[1:]
                
                print(str(index + 1) + "\t" + str(taskCompleted) + "\t\t" + str(taskText) + "\t" + str(taskReset))
            except:
                # Malformed line, attempt to fix it, if it's empty, remove it.
                # if(len(task) > 0):
                #     tasks[index] = ((task[0] + " " + task[1:]) if type(task[0]) == int else ("0 " + task[1:]))

                # Understand the problem with the line
                # Try to repair the line
                # Save the line (addTask)
                # Put the task in the right place (switch? or insert with custom code)

                print("This task, number " + str(index + 1) + " was malformed. Consider delete and add it again, the text is: \"" + task + "\"")
                index +=1
                continue

            index += 1

    # listArgs = ["-list", "-ls"]
    # addArgs = ["-add", "-a"]
    # deleteArgs = ["-delete", "-d"]
    # checkArgs = ["-check", "-c", "-x", "-tick", "-t"]
    # switchArgs = ["-switch", "-s"]
    # changeListArgs = ["-changelist", "-cl"]
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

        print(str(listArgs) + ": prints an indexed list of tasks in the current task list.")
        print(str(addArgs) + " + string + ?taskList: adds the following string to the current task list.")
        print(str(deleteArgs) + " + number + ?taskList: deletes the corresponding task in the current task list.")
        print(str(checkArgs) + " + number: toggle the completetion of the corresponding task in the current task list.")
        print(str(switchArgs) + "+ number + number: switches the position of the two corresponding tasks in the current task list.")
        print(str(changeListArgs) + ": string: changes the current task list to the string given.")
        print(str(helpArgs) + ": prints this information about input arguments.")
        print(str(testArgs) + ": runs unit tests and prints the result.")
            
if __name__ == "__main__":
    Main.main()