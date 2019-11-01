import sys
import time
import os 

class Main:
    def main():
        # Defaults
        task = None
        taskList = "default"
        taskListPath = "./tasklists/"
        resetChecked = None

        saveTask = False

        argC = len(sys.argv)
        argIndex = 1
        while argIndex < argC:
            arg = sys.argv[argIndex]

            # List curret todo list ()
            if(arg == "-list" or arg == "-ls"):
                Main.printList(taskList, taskListPath)

            # Add a task
            elif(arg == "-add" or arg == "-a"):
                if(argC - argIndex < 2):
                    print("Too few arguments to save task, need at least 1: task (string), task list (string)(optional), resetChecked (enum)(optional)")
                    quit()

                task = sys.argv[argIndex + 1]
                saveTask = True

                # reset args?
                # hour reset after completed easiest? h 2 -> write Z or T + datetime first in line, when next list is called, check timestamp, compare to reset time in args, 
                #   if past, uncheck (or better set utc datetime + reset time check if datetime is current or in past, if yes, uncheck)
                # datetime?
                # enum: daily, hourly, month, year, weekly.. ?

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

        if(saveTask):
            Main.saveTask(task, taskList, taskListPath)
        print(".\n.\n.end")

        
    def saveTask(task, taskList, taskListPath):
        """
        """

        taskListFile = taskListPath + taskList + ".txt"
        fileExists = False
        try:
            with open(taskListFile, "r") as file:
                fileExists = True
        except FileNotFoundError:
            fileExists = False

        # Make directory, if one exists, ignore error   
        try:
            os.mkdir(taskListPath)
        except FileExistsError:
            uselessVar = True

        taskObject = ("\n" if fileExists else "") + task

        try:
            with open(taskListFile, "a") as file:
                file.write(taskObject) 

            file.close() 
            return True
        except:
            print("Error saving task list " + taskList)
            return False

    def loadTaskList(taskList, taskListPath):
        """
        """

        taskListFile = taskListPath + taskList + ".txt"
        res = ""
        try:
            with open(taskListFile, "r") as file:
                for line in file:
                    res += line

            file.close() 
        except:
            print("Error loading task list " + taskList)
            res = None

        return res

    def setList(taskList, taskListPath):
        print("--- Help ---")

    def printList(taskList, taskListPath):
        tasks = Main.loadTaskList(taskList, taskListPath)
        print(tasks)

    def printHelp():
        print("--- Help ---")
            
if __name__ == "__main__":
    Main.main()