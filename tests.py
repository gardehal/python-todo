import sys
import os
import shutil

import todo

testDirectoryName = "test-tasks"
testTaskList = "tests"
testAllTaskListsDirectoryName = "."
testAllTaskListsFileName = "test-all-task-lists"
    
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
        testGetCurrentTaskListNoFileRes = Tests.testGetCurrentTaskListNoFile()
        Tests.after(useBeforeAfter)
        testGetCurrentTaskListFileExistsRes = Tests.testGetCurrentTaskListFileExists()
        Tests.after(useBeforeAfter)
        testAddTaskEmptyListRes = Tests.testAddTaskEmptyList()
        Tests.after(useBeforeAfter)
        testAddTaskFaultyFileRes = Tests.testAddTaskFaultyFile()
        Tests.after(useBeforeAfter)
        testAddTaskNoFileRes = Tests.testAddTaskNoFile()
        Tests.after(useBeforeAfter)
        testAddTaskNewTaskSameTaskListRes = Tests.testAddTaskNewTaskSameTaskList()
        Tests.after(useBeforeAfter)
        testloadFileNoListRes = Tests.testloadFileNoList()
        Tests.after(useBeforeAfter)
        testloadFileEmptyListRes = Tests.testloadFileEmptyList()
        Tests.after(useBeforeAfter)
        testloadFileOneTaskRes = Tests.testloadFileOneTask()
        Tests.after(useBeforeAfter)
        testSetListNoFileRes = Tests.testSetListNoFile()
        Tests.after(useBeforeAfter)
        testSetListToSameListRes = Tests.testSetListToSameList()
        Tests.after(useBeforeAfter)
        
        getFullFilePathRes = testGetFullFilePathDirectoryRes + testGetFullFilePathDirectoryAndFileRes
        getCurrentTaskListRes = testGetCurrentTaskListNoFileRes + testGetCurrentTaskListFileExistsRes
        addTaskRes = testAddTaskEmptyListRes + testAddTaskFaultyFileRes + testAddTaskNoFileRes + testAddTaskNewTaskSameTaskListRes 
        loadFileRes = testloadFileNoListRes + testloadFileEmptyListRes + testloadFileOneTaskRes
        setListRes = testSetListNoFileRes + testSetListToSameListRes
        finalRes = getFullFilePathRes + getCurrentTaskListRes + addTaskRes + loadFileRes + setListRes

        if(useBeforeAfter != 0):
            # Restore print fuction
            sys.stdout = sys.__stdout__

        # Print
        print("The results of the tests are: \n")
        Tests.printTestResult(testGetFullFilePathDirectoryRes, "testGetFullFilePathDirectory")
        Tests.printTestResult(testGetFullFilePathDirectoryAndFileRes, "testGetFullFilePathDirectoryAndFile")
        Tests.printTestResult(testGetCurrentTaskListNoFileRes, "testGetCurrentTaskListNoFile")
        Tests.printTestResult(testGetCurrentTaskListFileExistsRes, "testGetCurrentTaskListFileExists")
        Tests.printTestResult(testAddTaskEmptyListRes, "testAddTaskEmptyList")
        Tests.printTestResult(testAddTaskFaultyFileRes, "testAddTaskFaultyFile")
        Tests.printTestResult(testAddTaskNoFileRes, "testAddTaskNoFile")
        Tests.printTestResult(testAddTaskNewTaskSameTaskListRes, "testAddTaskNewTaskSameTaskList")
        Tests.printTestResult(testloadFileNoListRes, "testloadFileNoList")
        Tests.printTestResult(testloadFileEmptyListRes, "testloadFileEmptyList")
        Tests.printTestResult(testloadFileOneTaskRes, "testloadFileOneTask")
        Tests.printTestResult(testSetListNoFileRes, "testSetListNoFile")
        Tests.printTestResult(testSetListToSameListRes, "testSetListToSameList")

        print("\n" + ("All tests passed." if finalRes == 0 else "Some tests failed."))
        if(useBeforeAfter == 0):
            print("If some tests fail, try to run with before/after methods enabled, they are currently not; \n\t$ python todo.py -test")

    def printTestResult(result, testName):
        resultString = ("Passed\t\t" if result == 0 else "\tFailed\t")
        print(resultString + " - " + testName)

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

        # Delete test-file for list of all tasklists
        fullAllTaskListsPath = os.path.join(sys.path[0], testAllTaskListsFileName) + ".txt"

        if(os.path.isfile(fullAllTaskListsPath)):
            try:
                os.remove(fullAllTaskListsPath)
            except OSError as e:
                print("\nafter (tests) error: ")
                print(e)
                return 1

        # Delete test-directory of task lists (with children)
        fullTaskListsPath = os.path.join(sys.path[0], testDirectoryName)

        if(os.path.isdir(fullTaskListsPath)):
            # From https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
            try:
                shutil.rmtree(fullTaskListsPath)
            except OSError as e:
                print("\nafter (tests) error: ")
                print(e)
                return 1

        return 0

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

    def testGetCurrentTaskListNoFile():
        """
        Test getCurrentTaskList() with no existing file, this should create the file testAllTaskListsFileName and return the first line, 
        which is the current task list (taskList).
        """

        taskList = "testGetCurrentTaskListNoFile tasklist"

        # Check if file exists, it should not
        filePath = os.path.join(sys.path[0], testAllTaskListsFileName) + ".txt"
        if(os.path.isfile(filePath)):
            return 1

        currentTaskListRes = todo.Main.getCurrentTaskList(testAllTaskListsFileName, testAllTaskListsDirectoryName, taskList)

        if(os.path.isfile(filePath) and currentTaskListRes == taskList):
            return 0

        return 1

    def testGetCurrentTaskListFileExists():
        """
        Test getCurrentTaskList() with an existing file, this should return the first line, which is the current task list (currentTaskList).
        """

        currentTaskList = "testGetCurrentTaskListFileExists current tasklist"
        taskList = "testGetCurrentTaskListFileExists tasklist"

        filePath = os.path.join(sys.path[0], testAllTaskListsFileName) + ".txt"
        if(os.path.isfile(filePath)):
            return 1
        
        # Make the file
        try:
            with open(filePath, "a") as file:
                file.write(currentTaskList) 
                file.write("\n" + taskList) 

            file.close()
        except Exception as e:
            print("\ntestAddTaskEmptyList error: ")
            print(e)
            return 1

        currentTaskListRes = todo.Main.getCurrentTaskList(testAllTaskListsFileName, testAllTaskListsDirectoryName)

        if(currentTaskListRes == currentTaskList):
            return 0

        return 1

    def testAddTaskEmptyList():
        """
        Test addTask() with a task, an empty testTaskList, and testDirectoryName. The response should be true and our task should be added wihtout a newline.
        """

        emptyLine = ""
        task = "Run testAddTaskEmptyList"
        dirPath = os.path.join(sys.path[0], testDirectoryName)
        path = os.path.join(dirPath, testTaskList) + ".txt"
        
        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)
        else:
            return 1

        try:
            with open(path, "a") as file:
                file.write(emptyLine) 

            file.close()
        except Exception as e:
            # print("\ntestAddTaskEmptyList error: ")
            # print(e)
            return 1

        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName)
        
        # Check if the line was added in the file
        testTaskArray = []
        try:
            with open(path, "r") as file:
                for line in file:
                    testTaskArray.append(line)

            file.close() 
        except Exception as e:
            # print("\ntestAddTaskEmptyList error: ")
            # print(e)
            return 1

        fileCheck = len(testTaskArray) == 1 and testTaskArray[0] == "0 " + task

        if(taskRes and fileCheck):
            return 0
        
        return 1

    def testAddTaskFaultyFile():
        """
        Test addTask() with a task, a faulty formatted testTaskList, and testDirectoryName. The response should be false as the file could not be created.
        """

        task = "Run testAddTaskFaultyFile"
        faultyList = testTaskList + "\\"
        taskRes = todo.Main.addTask(task, faultyList, testDirectoryName)

        if(not taskRes):
            return 0
        
        return 1

    def testAddTaskNoFile():
        """
        Test addTask() with task, testTaskList, and testDirectoryName. This should return True and make direcotry testDirectoryName and file testTaskList (.txt).
        The line inside the file should be task, with a 0 to indicate it's not a completed task, without any newlines.
        """

        task = "Run testAddTaskNoFile"
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
        Test addTask() with 2 tasks, testTaskList, and testDirectoryName. This will repeat a lot of the checks from the test testAddTaskNoFile(), 
        but this time we will test on the second line in the file, which when added, should put a newline, 0, and the task.
        """

        task1 = "Run testAddTaskNewTaskSameTaskList"
        task2 = "Run testAddTaskNewTaskSameTaskList again!"
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

    def testloadFileNoList():
        """
        Test loadFile() with a non-existent list. It should return an empty array.
        """

        fileRes = todo.Main.loadFile(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 0):
            return 0

        return 1
        
    def testloadFileEmptyList():
        """
        Test loadFile() with a empty list. It should return an empty array.
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
            # print("\ntestloadFileEmptyList error: ")
            # print(e)
            return 1

        fileRes = todo.Main.loadFile(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 0):
            return 0

        return 1

    def testloadFileOneTask():
        """
        Test loadFile() with a empty list. It should return an array with one string, which should be our task (not '"0 " + task' as that is the job of addTask).
        """

        task = "Run testloadFileOneTask"
        dirPath = os.path.join(sys.path[0], testDirectoryName)
        path = os.path.join(dirPath, testTaskList) + ".txt"
        
        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)
        else:
            return 1

        try:
            with open(path, "a") as file:
                file.write(task) 

            file.close()
        except Exception as e:
            # print("\ntestloadFileOneTask error: ")
            # print(e)
            return 1

        fileRes = todo.Main.loadFile(testTaskList, testDirectoryName)

        if(type(fileRes) == list and len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1

    def testSetListNoFile():
        """
        Test setList with no pre-exisiting file. The should return true and create a file and write the newList into it as the only line.
        """

        newList = "setListNoFile list"

        filePath = os.path.join(sys.path[0], testAllTaskListsFileName) + ".txt"
        if(os.path.isfile(filePath)):
            return 1

        setRes = todo.Main.setList(newList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = []
        try:
            with open(filePath, "r") as file:
                for line in file:
                    fileRes.append(line)

            file.close()
        except Exception as e:
            print("\nsetListNoFile error: ")
            print(e)
            return 1

        fileCheck = len(fileRes) == 1 and fileRes[0] == newList

        if(setRes and os.path.isfile(filePath) and fileCheck):
            return 0

        return 1

    def testSetListToSameList():
        """
        Test setList for overriding a existing tasklist in a file. Should return true, and the newList should be the only line in the file.
        """

        oldList = "some other list"
        newList = "setListToSameList list"

        filePath = os.path.join(sys.path[0], testAllTaskListsFileName) + ".txt"
        
        try:
            with open(filePath, "a") as file:
                file.write(oldList)

            file.close()
        except Exception as e:
            print("\nsetListNoFile error: ")
            print(e)
            return 1

        if(not os.path.isfile(filePath)):
            return 1

        setRes = todo.Main.setList(newList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = []
        try:
            with open(filePath, "r") as file:
                for line in file:
                    fileRes.append(line)

            file.close()
        except Exception as e:
            print("\nsetListNoFile error: ")
            print(e)
            return 1

        fileCheck = len(fileRes) == 1 and fileRes[0] == newList

        if(setRes and os.path.isfile(filePath) and fileCheck):
            return 0

        return 1
        
    # no file
    # non existent action argument
    # bad file name
    # normal file tick
    # normal file delete
    # normal file switch
    # faulty task index (switch number)
    # faulty task index (task number)
    def testEditTask():
        """
        """

        return 1