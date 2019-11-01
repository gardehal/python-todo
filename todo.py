import sys
import time
import os 

class Main:
    def main():
        # Defaults
        task = None
        taskList = "default"
        taskListPath = "tasklists"
        resetChecked = None

        listTasks = False
        addTask = False

        argC = len(sys.argv)
        argIndex = 1
        while argIndex < argC:
            arg = sys.argv[argIndex]

            # List curret todo list ()
            if(arg == "-list" or arg == "-ls"):
                listTasks = True

            # Add a task
            elif(arg == "-add" or arg == "-a"):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: task (string), task list (string)(optional), resetChecked (enum)(optional)")
                    quit()

                task = sys.argv[argIndex + 1]
                addTask = True

                # reset args?
                # hour reset after completed easiest? h 2 -> write Z or T + datetime first in line, when next list is called, check timestamp, compare to reset time in args, 
                #   if past, uncheck (or better set utc datetime + reset time check if datetime is current or in past, if yes, uncheck)
                # datetime?
                # enum: daily, hourly, month, year, weekly.. ?
                # give datetime + interval, or just interval (datetime = now). When interval interact with datetime, reset, then set new datetime = old datetime + interval?
                    # better to set datetime + interval = datetimeTriggerAlert? vs check datet

                # Optional arguments, tasklist (file) and path
                optionalArgIndex = 0
                if(argC > argIndex + 2 and sys.argv[argIndex + 2][0] != "-"):
                    taskList = sys.argv[argIndex + 2]
                    optionalArgIndex += 1
                if(argC > argIndex + 3 and sys.argv[argIndex + 3][0] != "-"):
                    resetChecked = sys.argv[argIndex + 3]
                    optionalArgIndex += 1

                argIndex += 2 + optionalArgIndex
                continue

            # Delete a task
            elif(arg == "-delete" or arg == "-d"):
                print("d")

            # Check off a task (mark as done)
            elif(arg == "-check" or arg == "-c" or arg == "-x" or arg == "-tick" or arg == "-t"):
                print("c")

            # Uncheck a task (unmark as done)
            elif(arg == "-uncheck" or arg == "-uc"):
                print("uc")

            # Change list of tasks
            elif(arg == "-changeList" or arg == "-cl"):
                print("cl")

            # Switch tasks position
            elif(arg == "-switch" or arg == "-s"):
                print("cl")

            # Help
            elif(arg == "-h" or arg == "-help"):
                Main.printHelp()
                quit()

            # Invalid, inform and quit
            else:
                print("Argument not recognized: \"" + arg + "\", please see documentation or run with \"-help\" for help.")
                quit()

            argIndex += 1

        # TODO: groom/trigger reset
        
        if(addTask):
            saveRes = Main.addTask(task, taskList, taskListPath)
            print("Add task " + ("was successful." if saveRes else "failed."))

        if(listTasks):
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
        print(fullPath)

        fileExists = False
        try:
            with open(fullPath, "r") as file:
                fileExists = True
        except FileNotFoundError:
            fileExists = False

        # If no directory for task lists exist, make one
        taskListDirectory = Main.getFullFilePath(taskListPath)
        if(not os.path.exists(taskListDirectory)):
            os.mkdir(taskListDirectory)

        taskLine = ("\n" if fileExists else "") + "0" + task

        try:
            with open(fullPath, "a") as file:
                file.write(taskLine) 

            file.close() 
            return True
        except:
            print("Error saving task list " + taskList)
            return False

    def loadTaskList(taskList, taskListPath):
        """ 
        ???. \n
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
        except:
            print("Error loading task list " + taskList)

        return res

    def removeTask(task, taskList, taskListPath):
        """
        A method for removing a task from a tasklist. \n
        string task
        string taskList \n
        string taskListPath
        """

        print("--- removeTask ---")

    def toggleDone(taskNumber, taskList, taskListPath):
        """
        A method for removing a task from a tasklist. \n
        int taskNumber
        string taskList \n
        string taskListPath
        """

        tasks = Main.loadTaskList(taskList, taskListPath)
        tasks[taskNumber - 1]

        print("--- toggleDone ---")

# idea: a generic editing method can let me add (append), delete, change check status, set new reset time etc
    def editTaskList(taskList, taskListPath, filePermissions, taskNumber):
        """
        A method editing a tasklist. \n
        string taskList \n
        string taskListPath \n
        string filePermissions \n
        array seekArgs
        """
        fullPath = Main.getFullFilePath(taskListPath, taskList)

        try:
            with open(fullPath, filePermissions) as file:
                for line in file:
                    res.append(line)

            file.close() 
            return True
        except:
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

            taskCompleted = "Yes" if task[0] == "1" else "No"
            taskText = task[1:]

            print(str(index + 1) + "\t" + str(taskCompleted) + "\t\t" + str(taskText) + "\t" + str(taskReset))
            index += 1


    def printHelp():
        """
        A simple console print that informs user of program arguments.
        """

        print("--- Help ---")
            
if __name__ == "__main__":
    Main.main()