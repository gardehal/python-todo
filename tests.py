import sys
import os
import shutil

import todo

testDirectoryName = "test-tasks"
testTaskList = "tests"
    
class Tests:

    def runTests(useBeforeAfter = 1):
        """
        Run all tests and print a result in console. \n
        int useBeforeAfter (optional)
        """

        if(useBeforeAfter == 0):
            print("Not invoking before/after methods in tests.")
        else:
            # From https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
            # Disable print function (ignore error prints that pop up while running tests)
            sys.stdout = open(os.devnull, 'w')

        
        # Run tests
        testGetFullFilePathDirectoryRes = Tests.testGetFullFilePathDirectory()
        Tests.after(useBeforeAfter)
        testGetFullFilePathDirectoryAndFileRes = Tests.testGetFullFilePathDirectoryAndFile()
        Tests.after(useBeforeAfter)
        testAddTaskNewTaskNewTaskListRes = Tests.testAddTaskNewTaskNewTaskList()
        Tests.after(useBeforeAfter)
        testAddTaskNewTaskSameTaskListRes = Tests.testAddTaskNewTaskSameTaskList()
        Tests.after(useBeforeAfter)
        testAddTaskFaultyFileRes = Tests.testAddTaskFaultyFile()
        Tests.after(useBeforeAfter)
        testLoadTaskListNoListRes = Tests.testLoadTaskListNoList()
        Tests.after(useBeforeAfter)
        testLoadTaskListEmptyListRes = Tests.testLoadTaskListEmptyList()
        Tests.after(useBeforeAfter)
        testLoadTaskListRes = Tests.testLoadTaskList()
        Tests.after(useBeforeAfter)

        res1 = testGetFullFilePathDirectoryRes + testGetFullFilePathDirectoryAndFileRes + testAddTaskNewTaskNewTaskListRes + testAddTaskNewTaskSameTaskListRes
        res2 = testAddTaskFaultyFileRes + testLoadTaskListNoListRes + testLoadTaskListEmptyListRes + testLoadTaskListRes
        finalRes = res1 + res2

        if(useBeforeAfter != 0):
            # Restore print fuction
            sys.stdout = sys.__stdout__

        # Print
        print("The results of the tests are: \n")
        print("testGetFullFilePathDirectory \t\t" + ("passed" if testGetFullFilePathDirectoryRes == 0 else "failed"))
        print("testGetFullFilePathDirectoryAndFile \t" + ("passed" if testGetFullFilePathDirectoryAndFileRes == 0 else "failed"))
        print("testAddTaskNewTaskNewTaskList \t\t" + ("passed" if testAddTaskNewTaskNewTaskListRes == 0 else "failed"))
        print("testAddTaskNewTaskSameTaskList \t\t" + ("passed" if testAddTaskNewTaskSameTaskListRes == 0 else "failed"))
        print("testAddTaskFaultyFile \t\t\t" + ("passed" if testAddTaskFaultyFileRes == 0 else "failed"))
        print("testLoadTaskListNoList \t\t\t" + ("passed" if testLoadTaskListNoListRes == 0 else "failed"))
        print("testLoadTaskListEmptyList \t\t" + ("passed" if testLoadTaskListEmptyListRes == 0 else "failed"))
        print("testLoadTaskList \t\t\t" + ("passed" if testLoadTaskListRes == 0 else "failed"))

        print("\n" + ("All tests passed." if finalRes == 0 else "Some tests failed."))
        if(useBeforeAfter == 0):
            print("If some tests fail, try to run with before/after methods enabled, they are currently not; \n\t$ python todo.py -test")

    def before(useBeforeAfter):
        """
        A before method to ready the system before every test. \n
        int useBeforeAfter
        """

        if(useBeforeAfter == 0):
            return 0

        return 1

    def after(useBeforeAfter):
        """
        An after method to clean up after every test. \n
        int useBeforeAfter
        """

        if(useBeforeAfter == 0):
            return 0

        fullDirPath = os.path.join(sys.path[0], testDirectoryName)

        if(os.path.isdir(fullDirPath)):
            # From https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
            try:
                shutil.rmtree(fullDirPath)
                return 0
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))

        return 1

    def testGetFullFilePathDirectory():
        """
        Test getFullFilePath() with directory name only. This should produce a string from C to the root of the python script pluss the directory name appened.
        """

        path = todo.Main.getFullFilePath(testDirectoryName) 
        sysPath = sys.path[0]

        if(path.__contains__(sysPath) and path.__contains__(testDirectoryName)):
            return 0

        return 1

    def testGetFullFilePathDirectoryAndFile():
        """
        Test getFullFilePath() with directory and file. This should produce a string from C to the root of the python script pluss the directory name, 
        file name, and ".txt" appened.
        """

        path = todo.Main.getFullFilePath(testDirectoryName, testTaskList) 
        sysPath = sys.path[0]

        if(path.__contains__(sysPath) and path.__contains__(testDirectoryName) and path.__contains__(testTaskList) and path.__contains__(".txt")):
            return 0

        return 1

    def testAddTaskNewTaskNewTaskList():
        """
        Test addTask() with task, testTaskList, and testDirectoryName. This should return True and make direcotry testDirectoryName and file testTaskList (.txt).
        The line inside the file should be task, with a 0 to indicate it's not a completed task, without any newlines.
        """

        task = "Run tests"
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName)

        if(not taskRes):
            return 1

        # Check if the directory was created
        testDirPath = os.path.join(sys.path[0], testDirectoryName)
        isTestDirPath = os.path.isdir(testDirPath)

        # Check if the file was created
        testFilePath = os.path.join(testDirPath, testTaskList + ".txt")
        isTestFilePath = os.path.isfile(testFilePath)

        # Check if the line was added in the file
        testTaskArray = []
        try:
            with open(testFilePath, "r") as file:
                for line in file:
                    testTaskArray.append(line)

            file.close() 
        except FileNotFoundError:
            return 1

        fileCheck = len(testTaskArray) == 1 and testTaskArray[0] == "0 " + task

        if(isTestDirPath and isTestFilePath and fileCheck):
            return 0
        
        return 1

    def testAddTaskNewTaskSameTaskList():
        """
        Test addTask() with 2 tasks, testTaskList, and testDirectoryName. This will repeat a lot of the checks from the test testAddTaskNewTaskNewTaskList(), 
        but this time we will test on the second line in the file, which when added, should put a newline, 0, and the task.
        """

        task1 = "Run tests"
        task2 = "Make sure tests work!"
        task1Res = todo.Main.addTask(task1, testTaskList, testDirectoryName)
        task2Res = todo.Main.addTask(task2, testTaskList, testDirectoryName)

        if(not task1Res or not task2Res):
            return 1
            
        testDirPath = os.path.join(sys.path[0], testDirectoryName)
        testFilePath = os.path.join(testDirPath, testTaskList + ".txt")

        # Check if the line was added in the file
        testTaskArray = []
        try:
            with open(testFilePath, "r") as file:
                for line in file:
                    testTaskArray.append(line)

            file.close() 
        except FileNotFoundError:
            return 1

        task1Check = len(testTaskArray) == 2 and testTaskArray[0] == "0 " + task1 + "\n"
        task2Check = len(testTaskArray) == 2 and testTaskArray[1] == "0 " + task2

        if(task1Check and task2Check):
            return 0
        
        return 1

    def testAddTaskFaultyFile():
        """
        Test addTask() with a task, a faulty formatted testTaskList, and testDirectoryName. The response should be false as the file could not be created.
        """

        task = "Run tests"
        faultyList = testTaskList + "\\"
        taskRes = todo.Main.addTask(task, faultyList, testDirectoryName)

        if(not taskRes):
            return 0
        
        return 1

    def testLoadTaskListNoList():
        """
        Test loadTaskList() with a non-existent list. It should return an empty array.
        """

        fileRes = todo.Main.loadTaskList(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 0):
            return 0

        return 1
        
    def testLoadTaskListEmptyList():
        """
        Test loadTaskList() with a empty list. It should return an empty array.
        """

        dirPath = os.path.join(sys.path[0], testDirectoryName)
        path = os.path.join(dirPath, testTaskList) + ".txt"
        task = ""
        
        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)
        else:
            return 1

        try:
            with open(path, "a") as file:
                file.write(task) 
                uselessVar = True

            file.close()
        except Exception as e:
            # print("\ntestLoadTaskListEmptyList error: ")
            # print(e)
            return 1

        fileRes = todo.Main.loadTaskList(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 0):
            return 0

        return 1

    def testLoadTaskList():
        """
        Test loadTaskList() with a empty list. It should return an empty array.
        """

        dirPath = os.path.join(sys.path[0], testDirectoryName)
        path = os.path.join(dirPath, testTaskList) + ".txt"
        task = "Run tests"
        
        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)
        else:
            return 1

        try:
            with open(path, "a") as file:
                file.write(task) 

            file.close()
        except Exception as e:
            # print("\ntestLoadTaskList error: ")
            # print(e)
            return 1

        fileRes = todo.Main.loadTaskList(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1