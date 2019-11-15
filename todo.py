import sys
import time
import os
import datetime
import calendar

import tests

listTaskArgs = ["-tasks", "-t"]
listListsArgs = ["-lists", "-l"]
addArgs = ["-add", "-a"]
deleteArgs = ["-delete", "-d"]
checkArgs = ["-check", "-c", "-x"]
switchArgs = ["-switch", "-s"]
insertArgs = ["-insert", "-i"]
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
            print("arg: " + str(sys.argv[argIndex]))

            # List contents of curret task list
            if(arg in listTaskArgs):
                formatRes = Main.formatPrintList(taskList, taskListPath)
                for line in formatRes:
                    print(line)

                argIndex += 1
                continue

            # List all tasklists in directory "tasklists"
            if(arg in listListsArgs):
                formatListRes = Main.formatTaskListsPrint(taskListPath)
                for line in formatListRes:
                    print(line)

                argIndex += 1
                continue

            # Add a task
            elif(arg in addArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: task (string), resetInterval (enum)(optional)")
                    quit()

                task = sys.argv[argIndex + 1]
                # TODO incrementing agindex here rather than later seems to have unintended skipping of args
                # argIndex += 2

                # Pick up reset args if there are any
                resetInterval = None
                resetDateTime = None
                totalResetTime = None
                optionalArgIndex = 0

                # Interval
                if(argC > argIndex + 2 and sys.argv[argIndex + 2][0] != "-"):
                    useDefaultMultiplier = True
                    totalResetTime = 0    
                    intervalIndex = argIndex + 2
                    while(intervalIndex < argC):
                        print("idx " + str(intervalIndex) + ": " + str(sys.argv[intervalIndex]) + ", 0 :" + str(sys.argv[intervalIndex][0]))

                        # If next argument is a flag (-xyz) or not a recognized increment argument, break loop, use useDefaultMultiplier
                        # Notice the decrementation of intervalIndex so the date arguments are not skipped
                        if(sys.argv[intervalIndex][0] == "-" or sys.argv[intervalIndex][0] != "s" and sys.argv[intervalIndex][0] != "h"  
                        and sys.argv[intervalIndex][0] != "d"  and sys.argv[intervalIndex][0] != "w"  and sys.argv[intervalIndex][0] != "m"):
                            intervalIndex -= 1
                            break

                        if(sys.argv[intervalIndex][0] == "s"):
                            useDefaultMultiplier = False
                            totalResetTime += int(sys.argv[intervalIndex][1:])
                            intervalIndex += 1
                            continue

                        if(sys.argv[intervalIndex][0] == "h"):
                            useDefaultMultiplier = False
                            totalResetTime += int(sys.argv[intervalIndex][1:]) * 60 * 60
                            intervalIndex += 1
                            continue
                        
                        elif(sys.argv[intervalIndex][0] == "d"):
                            useDefaultMultiplier = False
                            totalResetTime += int(sys.argv[intervalIndex][1:]) * 60 * 60 * 24
                            intervalIndex += 1
                            continue
                        
                        elif(sys.argv[intervalIndex][0] == "w"):
                            useDefaultMultiplier = False
                            totalResetTime += int(sys.argv[intervalIndex][1:]) * 60 * 60 * 24 * 7
                            intervalIndex += 1
                            continue
                        
                        # 30 / 31?
                        elif(sys.argv[intervalIndex][0] == "m"):
                            useDefaultMultiplier = False
                            totalResetTime += int(sys.argv[intervalIndex][1:]) * 60 * 60 * 24 * 7 * 30
                            intervalIndex += 1
                            continue
                        
                        else:
                            print("Interval argument not recognized " + sys.argv[intervalIndex] + ". Quitting.")
                            intervalIndex -= 1
                            quit()

                        intervalIndex += 1
                        
                    # Interval arguments finished, increment optionalArgIndex so we don't have to reiterate over the same arguments
                    optionalArgIndex += intervalIndex

                    # TODO try/except for int parse 
                    # Use useDefaultMultiplier which is hours of no letter is given in the interval argument
                    if(useDefaultMultiplier and argC > optionalArgIndex + 1 and sys.argv[optionalArgIndex + 1][0] != "-"):
                        totalResetTime += int(sys.argv[optionalArgIndex + 1]) * 60 * 60
                        optionalArgIndex += 1

                    # Date
                    if(argC > optionalArgIndex + 1 and sys.argv[optionalArgIndex + 1][0] != "-"):
                        print("date")
                        resetDateTime = sys.argv[optionalArgIndex + 1]
                        optionalArgIndex += 1

                # All optional arguments and the recognized permutations have been dealt with, finally run the method
                saveRes = Main.addTask(task, taskList, taskListPath, totalResetTime, resetDateTime)
                print("Add task " + ("was successful." if saveRes else "failed."))

                argIndex += optionalArgIndex
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

            elif(arg in insertArgs):
                if(argC - argIndex < 2):
                    print("Too few arguments to insert task, need at least 2: tasknumber (int), insertNumber(int)")
                    quit()
                
                taskNumber = int(sys.argv[argIndex + 1]) - 1
                insertNumber = int(sys.argv[argIndex + 2]) - 1

                checkRes = Main.editTask([taskNumber, insertNumber], taskList, taskListPath, "insert", "w")
                print(("Successfully" if checkRes else "Failed to") + " insert task.")

                argIndex += 3
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

        # No arguments, print the contents of the current tasklist
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

    def addTask(task, taskList, taskListPath, resetInterval = None, resetDateTime = None):
        """
        A method for saving/adding a task "task" to the list "taskList" in directory "taskListPath". If the optional argument resetInterval (int, seconds) is given,
        the format method will reset the tasks completeion status after the resetInterval period, from the datetime when the task was added.
        If the argument resetDateTime (datetime) is also given, the reset will trigger on the interval from that datetime. \n
        string task \n
        string taskList \n
        string taskListPath \n
        int resetInterval \n
        Datetime resetDateTime
        """

        if(task.rstrip() == ""):
            return False

        # TODO reset
        # 1. Finish add
        # - 2. Program input arguments (resetInterval, month, week, day, hour options)
        # 3. Reset completeion and increment next resetDateTime in formatPrintList (+ detect malformed line)
        # 4. Tests
        # 5. Documentation

        resetString = ""
        incrementedRestString = ""

        # Deal with resetInterval and resetDateTime
        if(resetInterval != None):
            try:
                sanitizedResetInterval = int(resetInterval)

                # About 3.8 months limit
                if(sanitizedResetInterval > 9999999 or sanitizedResetInterval < 1):
                    raise Exception("Invalid interval argument")
            except Exception as e:
                print("\naddTask reset arguments error:")
                print(e)
                return False
            
            # hh:dd-mm-yyyy
            if(resetDateTime != None):
                try:
                    now = datetime.datetime.now()
                    hour = None
                    day = None
                    month = None
                    year = None

                    # Hour is the minimum expected input for datetime
                    hourDateSplit = resetDateTime.split(":")
                    hour = int(hourDateSplit[0])
                    if(hour < 0 or hour > 23):
                        return False

                    dateArray = []
                    if(len(hourDateSplit) > 1):
                        dateArray = hourDateSplit[1].split("-")

                        # Convert all elements to ints
                        dateArrayIndex = 0
                        while(dateArrayIndex < len(dateArray)):
                            dateArray[dateArrayIndex] = int(dateArray[dateArrayIndex])
                            dateArrayIndex += 1

                    # Note: The inverted structure of year, month, day is so we can use year and month to get maxDate.
                    # Get year from input, if none use current
                    if(len(dateArray) > 2 and dateArray[2]):
                        year = dateArray[2]
                    else:
                        year = now.year

                    # Get month from input, if none use current
                    if(len(dateArray) > 1 and dateArray[1] and dateArray[1] > 0 and dateArray[1] < 13):
                        month = dateArray[1]
                    else:
                        month = now.month
                        
                    # Get day from input, if none use current
                    # Thanks to https://stackoverflow.com/questions/42950/get-last-day-of-the-month for the line
                    maxDate = calendar.monthrange(year, month)[1]
                    if(len(dateArray) > 0 and dateArray[0] and dateArray[0] > 0 and dateArray[0] < (maxDate + 1)):
                        day = dateArray[0]
                    else:
                        day = now.day

                    # Year, month, day, hour from users input or current, minute, seconds, etc. default 0
                    sanitizedResetDateTime = datetime.datetime(year, month, day, hour)

                except Exception as e:
                    print("\naddTask datetime arguments error:")
                    print(e)
                    return False
                
            else:
                now = datetime.datetime.now()
                sanitizedResetDateTime = datetime.datetime(now.year, now.month, now.day, now.hour)

            # interval and datetime format:
            # !interval%datetime
            resetString = "!" + str(sanitizedResetInterval) + "Z" + str(sanitizedResetDateTime).replace(" ", "T")

            incrementedRestString = str(Main.incrementResetDateTime(resetString)) + " "
            if(incrementedRestString.strip() == None):
                return False

            print("Task will reset every " + str(sanitizedResetInterval/60/60) + " hours from the date and time " + str(sanitizedResetDateTime))

        loadTaskRes = Main.loadFile(taskList, taskListPath)
        fileExists = True if len(loadTaskRes) > 0 else False

        # If no directory for task lists exist, make one
        taskListDirectory = Main.getFullFilePath(taskListPath)
        if(not os.path.exists(taskListDirectory)):
            os.mkdir(taskListDirectory)

        fullPath = Main.getFullFilePath(taskListPath, taskList)
        taskLine = ("\n" if fileExists else "") + "0 " + incrementedRestString + task

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
            
            if(action == "switch" or action == "insert"):
                actionNumber = int(taskRefrence[1])
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

        elif(action == "switch"):
            try:                    
                tmp = fileArray[taskNumber]
                fileArray[taskNumber] = fileArray[actionNumber].rstrip() + "\n"
                fileArray[actionNumber] = tmp.rstrip() + "\n"

            except Exception as e:
                print("\neditTask switch error:")
                print(e)
                return False

        elif(action == "insert"):
            try:
                # fileArray[taskNumber] inserts into index actionNumber
                tmp = fileArray[taskNumber].rstrip() + "\n"
                fileArray[actionNumber] = fileArray[actionNumber].rstrip() + "\n"
                
                fileArray.pop(taskNumber)
                fileArray.insert(actionNumber, tmp)

            except Exception as e:
                print("\neditTask insert error:")
                print(e)
                return False
            
        else:
            print("Action not recognized, must be \"check\", \"delete\", \"switch\", \"insert\"")
            return False

        # After modifying array, remove newline and trailing white space, if it exists
        if(len(fileArray) > 1):
            fileArray[len(fileArray) - 1] = fileArray[len(fileArray) - 1].rstrip()

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

        # Not forbidden but poor practice:
        #   (space)
        # Forbidden chars in filenames (Windows):
        # From stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names
        # < (less than)
        # > (greater than)
        # : (colon - sometimes works, but is actually NTFS Alternate Data Streams)
        # " (double quote)
        # / (forward slash)
        # \ (backslash)
        # | (vertical bar or pipe)
        # ? (question mark)
        # * (asterisk)

        replaceChars = [" ", "<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
        # sanitizedTaskList = str(taskList).replace(replaceChars, "-")
        sanitizedTaskList = taskList

        for char in replaceChars:
            sanitizedTaskList = str(sanitizedTaskList).replace(char, "-")

        currentTaskList = Main.getCurrentTaskList(allTaskListsFileName, allTaskListsPath)
        if(taskList == currentTaskList):
            return True

        allTaskListsFullPath = Main.getFullFilePath(allTaskListsPath, allTaskListsFileName)
        try:
            with open(allTaskListsFullPath, "w") as file:
                file.write(sanitizedTaskList)

            file.close()
        except Exception as e:
            # print("\ntestloadFileEmptyList error: ")
            # print(e)
            return False

        return True

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
                taskText = str(task[2:]).rstrip()

                if(len(taskText) < 1):
                    raise Exception
                
                printArray.append(str(index + 1) + "\t" + str(taskCompleted) + "\t\t" + str(taskText) + "\t" + str(taskReset))
            except:
                # Malformed line, attempt to fix it, if it's empty, remove it.
                taskLine = str(task).rstrip()
                
                # taskLine is empty string ("") or only contains a complete number ("0"/"1"), delete line
                if(len(taskLine) < 1 or len(taskLine[1:]) < 1):
                    Main.editTask([index], taskList, taskListPath, "delete")

                # taskLine has no complete number ("0"/"1"), but has a task, add task again
                elif(taskLine[0] != "0" and taskLine[0] != "1"):
                    Main.editTask([index], taskList, taskListPath, "delete")
                    Main.addTask(taskLine, taskList, taskListPath)
                    Main.editTask([len(tasks) - 1, index], taskList, taskListPath, "insert")

                # Unknown error, implore the user fix and quit
                else:
                    printArray.append("This task, number " + str(index + 1) + " was malformed. Please delete and add it again before trying agian. The text is: \"" + task + "\"")
                    quit()
                    
                # Though recursion, run method again, this should load the fixed file into memory and recursivly fix the 
                # file when it finds an error untill all is well or it hits the else part above.
                return Main.formatPrintList(taskList, taskListPath, True)

            index += 1

        return printArray

    def formatTaskListsPrint(taskListPath):
        """
        A method for formatting the task lists in a legible manner. \n
        string taskListPath
        """

        if(len(taskListPath) < 1):
            return []

        path = Main.getFullFilePath(taskListPath)

        printArray = []
        for f in os.listdir(path):
            filePath = os.path.join(path, f)
            if(os.path.isfile(filePath)):
                fileName = f.split(".")
                printArray.append(fileName[0])

        return printArray

    def incrementResetDateTime(resetString):
        """
        Return the incremented resetString of the given resetString. \n
        string resetString
        """

        incrementedDateTime = None

        try:
            # !resetIntervalZdateTtime
            # !123Z2019-01-02T03:04:05 -> !123, 2019-01-02T03:04:05 
            resetStringIncrementDateTimeSplit = resetString.split("Z")

            # !123 -> 123
            increment = int(resetStringIncrementDateTimeSplit[0][1:])

            # 2019-01-02T03:04:05 -> 2019-01-02, 03:04:05 
            dateTimeSplit = resetStringIncrementDateTimeSplit[1].split("T")

            # 2019-01-02  -> 2019, 01, 02
            dateArray = dateTimeSplit[0].split("-")

            # 03:04:05  -> 03, 04, 05 
            timeArray = dateTimeSplit[1].split(":")

            # Convert to ints
            dateArrayIndex = 0
            while(dateArrayIndex < len(dateArray)):
                dateArray[dateArrayIndex] = int(dateArray[dateArrayIndex])
                dateArrayIndex += 1

            timeArrayIndex = 0
            while(timeArrayIndex < len(timeArray)):
                timeArray[timeArrayIndex] = int(timeArray[timeArrayIndex])
                timeArrayIndex += 1

            # Increment datetime with the datetime library
            oldDateTime = datetime.datetime(dateArray[0], dateArray[1], dateArray[2], timeArray[0], timeArray[1], timeArray[2])
            newDateTime = oldDateTime + datetime.timedelta(seconds = increment)

            # Assemble the resetString format !resetIntervalZdateTtime
            joinedNewDateTime = str(newDateTime).replace(" ", "T")
            incrementedDateTime = "!" + str(increment) + "Z" + joinedNewDateTime

            return incrementedDateTime

        except Exception as e:
            print("\nincrementResetDateTime error:")
            print(e)
            return incrementedDateTime

        return incrementedDateTime

    {
        # listTaskArgs = ["-tasks", "-t"]
        # listListsArgs = ["-lists", "-l"]
        # deleteArgs = ["-delete", "-d"]
        # checkArgs = ["-check", "-c", "-x"]
        # switchArgs = ["-switch", "-s"]
        # insertArgs = ["-insert", "-i"]
        # setListArgs = ["-setList", "-sl"]
        # helpArgs = ["-help", "-h"]
        # testArgs = ["-test"]
    }

    def printHelp():
        """
        A simple console print that informs user of program arguments.
        """

        print("--- Help ---")
        print("Arguments marked with ? are optional.")
        print("All arguments that triggers a function start with dash(-).")
        print("All arguments must be separated by space only.")
        print("To submit sentences with spaces between words, use quotation marks (\", \'), otherwise they will be counted as separate arguments.")
        print("\te.g.: $ python todo.py -add \"This is a sentence.\"")
        print("\n")

        print(str(listTaskArgs) + ": prints an indexed list of tasks in the current task list.")
        print(str(listListsArgs) + ": prints a list of all task lists.")
        print(str(addArgs) + " + string: adds the following string to the current task list.")
        print(str(deleteArgs) + " + number: deletes the corresponding task in the current task list.")
        print(str(checkArgs) + " + number: toggle the completion of the corresponding task in the current task list.")
        print(str(switchArgs) + "+ number + number: switches the position of the two corresponding tasks in the current task list.")
        print(str(insertArgs) + "+ number + number: inserts the task (first number) into position of the second number.")
        print(str(setListArgs) + ": string: sets the current task list to the string given.")
        print(str(helpArgs) + ": prints this information about input arguments.")
        print(str(testArgs) + ": runs unit tests and prints the result.")
            
if __name__ == "__main__":
    Main.main()