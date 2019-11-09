import sys
import os
import shutil

import todo

testDirectoryName = "test-tasks"
testTaskList = "tests"
testAllTaskListsDirectoryName = ""
testAllTaskListsFileName = "test-all-task-lists"
    
class Tests:

    def runTests(useBeforeAfter = 1):
        """
        Run all tests and print a result in console. \n
        int useBeforeAfter (optional)
        """

        # For checking individual tests
        # testFormatPrintListMalformedTaskTextRes = Tests.testFormatPrintListMalformedTaskText()
        # Tests.after(useBeforeAfter)
        
        # Tests.printTestResult(testFormatPrintListMalformedTaskTextRes, "testFormatPrintListMalformedTaskText")
        # quit()

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
        testAddTaskNoTaskRes = Tests.testAddTaskNoTask() 
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
        testEditTaskNoFileRes = Tests.testEditTaskNoFile()
        Tests.after(useBeforeAfter)
        testEditTaskNoActionRes = Tests.testEditTaskNoAction()
        Tests.after(useBeforeAfter)
        testEditTaskNoTaskNumberRes = Tests.testEditTaskNoTaskNumber()
        Tests.after(useBeforeAfter)
        testEditTaskIllegalNumberRes = Tests.testEditTaskIllegalNumber()
        Tests.after(useBeforeAfter)
        testEditTaskIllegalPermissionRes = Tests.testEditTaskIllegalPermission()
        Tests.after(useBeforeAfter)
        testEditTaskCheckMarkMalformedTaskRes = Tests.testEditTaskCheckMarkMalformedTask()
        Tests.after(useBeforeAfter)
        testEditTaskCheckMarkTaskRes = Tests.testEditTaskCheckMarkTask()
        Tests.after(useBeforeAfter)
        testEditTaskDeleteTaskRes = Tests.testEditTaskDeleteTask()
        Tests.after(useBeforeAfter)
        testEditTaskSwitchLastTaskRes = Tests.testEditTaskSwitchLastTask()
        Tests.after(useBeforeAfter)
        testEditTaskSwitchTasksRes = Tests.testEditTaskSwitchTasks()
        Tests.after(useBeforeAfter)
        testEditTaskInsertLastTaskRes = Tests.testEditTaskInsertLastTask()
        Tests.after(useBeforeAfter)
        testEditTaskInsertTaskRes = Tests.testEditTaskInsertTask()
        Tests.after(useBeforeAfter)
        testEditTaskIllegalTaskNumberRes = Tests.testEditTaskIllegalTaskNumber()
        Tests.after(useBeforeAfter)
        testEditTaskNoActionNumberRes = Tests.testEditTaskNoActionNumber()
        Tests.after(useBeforeAfter)
        testFormatPrintListNoFileRes = Tests.testFormatPrintListNoFile()
        Tests.after(useBeforeAfter)
        testFormatPrintListEmptyFileRes = Tests.testFormatPrintListEmptyFile()
        Tests.after(useBeforeAfter)
        testFormatPrintListMalformedZeroOneRes = Tests.testFormatPrintListMalformedZeroOne()
        Tests.after(useBeforeAfter)
        testFormatPrintListMalformedTaskTextRes = Tests.testFormatPrintListMalformedTaskText()
        Tests.after(useBeforeAfter)
        testFormatPrintListNormalFormatRes = Tests.testFormatPrintListNormalFormat()
        Tests.after(useBeforeAfter)
        
        getFullFilePathRes = testGetFullFilePathDirectoryRes + testGetFullFilePathDirectoryAndFileRes
        getCurrentTaskListRes = testGetCurrentTaskListNoFileRes + testGetCurrentTaskListFileExistsRes
        addTaskRes = testAddTaskEmptyListRes + testAddTaskFaultyFileRes + testAddTaskNoFileRes + testAddTaskNoTaskRes + testAddTaskNewTaskSameTaskListRes 
        loadFileRes = testloadFileNoListRes + testloadFileEmptyListRes + testloadFileOneTaskRes
        setListRes = testSetListNoFileRes + testSetListToSameListRes
        editFileRes1 = testEditTaskNoFileRes + testEditTaskNoActionRes + testEditTaskNoTaskNumberRes + testEditTaskIllegalNumberRes + testEditTaskIllegalPermissionRes
        editFileRes2 = testEditTaskCheckMarkMalformedTaskRes + testEditTaskCheckMarkTaskRes + testEditTaskDeleteTaskRes + testEditTaskSwitchLastTaskRes + testEditTaskSwitchTasksRes
        editFileRes3 = testEditTaskInsertLastTaskRes + testEditTaskInsertTaskRes + testEditTaskIllegalTaskNumberRes + testEditTaskNoActionNumberRes
        formatPrintListRes1 = testFormatPrintListNoFileRes + testFormatPrintListEmptyFileRes + testFormatPrintListMalformedZeroOneRes + testFormatPrintListMalformedTaskTextRes
        formatPrintListRes2 = testFormatPrintListNormalFormatRes
        finalRes = getFullFilePathRes + getCurrentTaskListRes + addTaskRes + loadFileRes + setListRes + editFileRes1 + editFileRes2 + editFileRes3 + formatPrintListRes1 + formatPrintListRes2

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
        Tests.printTestResult(testAddTaskNoTaskRes, "testAddTaskNoTask")
        Tests.printTestResult(testAddTaskNewTaskSameTaskListRes, "testAddTaskNewTaskSameTaskList")
        Tests.printTestResult(testloadFileNoListRes, "testloadFileNoList")
        Tests.printTestResult(testloadFileEmptyListRes, "testloadFileEmptyList")
        Tests.printTestResult(testloadFileOneTaskRes, "testloadFileOneTask")
        Tests.printTestResult(testSetListNoFileRes, "testSetListNoFile")
        Tests.printTestResult(testSetListToSameListRes, "testSetListToSameList")
        Tests.printTestResult(testEditTaskNoFileRes, "testEditTaskNoFile")
        Tests.printTestResult(testEditTaskNoActionRes, "testEditTaskNoAction")
        Tests.printTestResult(testEditTaskNoTaskNumberRes, "testEditTaskNoTaskNumber")
        Tests.printTestResult(testEditTaskIllegalNumberRes, "testEditTaskIllegalNumber")
        Tests.printTestResult(testEditTaskIllegalPermissionRes, "testEditTaskIllegalPermission")
        Tests.printTestResult(testEditTaskCheckMarkMalformedTaskRes, "testEditTaskCheckMarkMalformedTask")
        Tests.printTestResult(testEditTaskCheckMarkTaskRes, "testEditTaskCheckMarkTask")
        Tests.printTestResult(testEditTaskDeleteTaskRes, "testEditTaskDeleteTask")
        Tests.printTestResult(testEditTaskSwitchLastTaskRes, "testEditTaskSwitchLastTask")
        Tests.printTestResult(testEditTaskSwitchTasksRes, "testEditTaskSwitchTasks")
        Tests.printTestResult(testEditTaskInsertLastTaskRes, "testEditTaskInsertLastTask")
        Tests.printTestResult(testEditTaskInsertTaskRes, "testEditTaskInsertTask")
        Tests.printTestResult(testEditTaskIllegalTaskNumberRes, "testEditTaskIllegalTaskNumber")
        Tests.printTestResult(testEditTaskNoActionNumberRes, "testEditTaskNoActionNumber")
        Tests.printTestResult(testFormatPrintListNoFileRes, "testFormatPrintListNoFile")
        Tests.printTestResult(testFormatPrintListEmptyFileRes, "testFormatPrintListEmptyFile")
        Tests.printTestResult(testFormatPrintListMalformedZeroOneRes, "testFormatPrintListMalformedZeroOne")
        Tests.printTestResult(testFormatPrintListMalformedTaskTextRes, "testFormatPrintListMalformedTaskText")
        Tests.printTestResult(testFormatPrintListNormalFormatRes, "testFormatPrintListNormalFormat")

        print("\n" + ("All tests passed." if finalRes == 0 else (str(finalRes) + " test(s) failed.")))
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

    def writeFile(line, fileName, filePath):
        """
        Utility method for creating and writing a sigle string line in a new file (permissions "a"). Returns absolute path of file if successful. \n
        string line \n
        string fileName \n
        string filePath
        """

        dirPath = os.path.join(sys.path[0], filePath)
        path = os.path.join(dirPath, fileName) + ".txt"
        
        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)

        try:
            with open(path, "a") as file:
                file.write(line) 

            file.close()
            return path
        except Exception as e:
            print("\nwriteFile error: ")
            print(e)
            return None

    def readFile(fileName, filePath):
        """
        Utility method for reading file. Returns array with all lines. \n
        string fileName \n
        string filePath
        """

        dirPath = os.path.join(sys.path[0], filePath)
        path = os.path.join(dirPath, fileName) + ".txt"
        result = []

        try:
            with open(path, "r") as file:
                for line in file:
                    result.append(line)

            file.close()

            return result
        except Exception as e:
            print("\nwriteFile error: ")
            print(e)
            return result

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
        taskList = "\ntestGetCurrentTaskListFileExists tasklist"

        filePath1 = Tests.writeFile(currentTaskList, testAllTaskListsFileName, testAllTaskListsDirectoryName)
        filePath2 = Tests.writeFile(taskList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

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
        filePath = Tests.writeFile(emptyLine, testTaskList, testDirectoryName)

        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName)
            
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == "0 " + task

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

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == "0 " + task

        if(isTestDirPath and isTestFilePath and fileCheck):
            return 0
        
        return 1
        
    def testAddTaskNoTask():
        """
        Test addTask() with an empty task string. Should return false and no create a file or task.
        """

        task = ""
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName)

        testDirPath = os.path.join(sys.path[0], testDirectoryName)
        isTestDirPath = os.path.isdir(testDirPath)

        testFilePath = os.path.join(testDirPath, testTaskList + ".txt")
        isTestFilePath = os.path.isfile(testFilePath)

        if(not taskRes and not isTestDirPath and not isTestFilePath):
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
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        task1Check = len(fileRes) == 2 and fileRes[0] == "0 " + task1 + "\n"
        task2Check = len(fileRes) == 2 and fileRes[1] == "0 " + task2

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

        task = ""
        
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
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
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
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

        fileRes = Tests.readFile(testAllTaskListsFileName, testAllTaskListsDirectoryName)

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
        
        filePath = Tests.writeFile(oldList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        if(filePath == None):
            return 1

        setRes = todo.Main.setList(newList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = Tests.readFile(testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == newList

        if(setRes and os.path.isfile(filePath) and fileCheck):
            return 0

        return 1
    
    def testEditTaskNoFile():
        """
        Test editTask() with no file. This should return false.
        """
        
        taskNumber = [0]
        fileName = ""
        filePath = "."
        actionName = "delete"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, fileName, filePath, actionName, permissions)

        if(not editRes):
            return 0

        return 1
    
    def testEditTaskNoAction():
        """
        Test editTask() with no action. This should return false and not alter the contents of the file.
        """ 

        task = "Run testEditTaskNoAction"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = [0]
        actionName = ""
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1
    
    def testEditTaskNoTaskNumber():
        """
        Test editTask() with no number refrence to task. This should return false and not alter the contents of the file.
        """ 

        task = "Run testEditTaskNoTaskNumber"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = None
        actionName = "delete"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1
    
    def testEditTaskIllegalNumber():
        """
        Test editTask() with too high and too low task numbers. This should return false and not alter the contents of the file.
        """ 

        task = "Run testEditTaskIllegalNumber"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        # Too high
        taskNumberHigh = [9999]
        actionName = "delete"
        permissions = "w"
        editHighRes = todo.Main.editTask(taskNumberHigh, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editHighRes):
            return 1

        fileHighRes = Tests.readFile(testTaskList, testDirectoryName)
        
        # Too low
        taskNumberLow = [-42]
        editLowRes = todo.Main.editTask(taskNumberLow, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editLowRes):
            return 1

        fileLowRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileHighRes) == 1 and fileHighRes[0] == task and len(fileLowRes) == 1 and fileLowRes[0] == task):
            return 0

        return 1

    def testEditTaskIllegalPermission():
        """
        Test editTask() with illegal permission. This should return false and not alter the contents of the file.
        """ 

        task = "Run testEditTaskIllegalPermission"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = [0]
        actionName = "delete"
        permissions = "some nonexistent permission"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1
    
    def testEditTaskCheckMarkMalformedTask():
        """
        Test editTask() with a normal file and number, however the line is missing a leading 0/1, making the operation impossible. Should return false and not alter the line.
        """ 

        # Note: no 0 or 1 in beginning of line
        task = "Run testEditTaskCheckMarkMalformedTask"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = [0]
        actionName = "check"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1

    def testEditTaskCheckMarkTask():
        """
        Test editTask() with a normal file, number, and line. Should return true and only change the 0 to a 1.
        """ 

        taskStatus = "0"
        task = "Run testEditTaskCheckMarkTask"
        taskLine = taskStatus + " " + task
        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = [0]
        actionName = "check"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0][1:] == " " + task and fileRes[0][0] == "1"):
            return 0

        return 1

    def testEditTaskDeleteTask():
        """
        Test editTask() with a normal file, number, and line. Should return true and remove the line taskNumber, but not delete the file.
        """ 
        
        task = "Run testEditTaskDeleteTask"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = [0]
        actionName = "delete"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 0 and os.path.isfile(filePath)):
            return 0

        return 1

    def testEditTaskSwitchLastTask():
        """
        Test editTask() with a normal file, numbers, and line, and switching the last task for newline reasons. Should return true and switch the lines.
        """ 
        
        firstTask = "Run testEditTaskSwitchLastTask first\n"
        secondTask = "Run testEditTaskSwitchLastTask second\n"
        thirdTask = "Run testEditTaskSwitchLastTask third\n"
        fourthTask = "Run testEditTaskSwitchLastTask fourth"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)
        thirdFilePath = Tests.writeFile(thirdTask, testTaskList, testDirectoryName)
        fourthFilePath = Tests.writeFile(fourthTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None or thirdFilePath == None or fourthFilePath == None):
            return 1
            
        firstFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) != 4 or firstFileRes[0] != firstTask or firstFileRes[1] != secondTask or firstFileRes[2] != thirdTask or firstFileRes[3] != fourthTask):
            return 1

        taskNumbers = [0, 3]
        actionName = "switch"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        secondFileRes = Tests.readFile(testTaskList, testDirectoryName)

        # The second(index: 1) and third(index: 2) lines should not be altered
        untouchedLinesRes = len(secondFileRes) == 4 and secondFileRes[1] == secondTask and secondFileRes[2] == thirdTask

        # Note: The newline has been moved from the end of the first task to the end of the second task
        switchedLinesRes = secondFileRes[0] == (fourthTask + "\n") and secondFileRes[3] == firstTask.rstrip()

        if(untouchedLinesRes and switchedLinesRes):
            return 0

        return 1

    def testEditTaskSwitchTasks():
        """
        Test editTask() with a normal file, numbers, and line. Should return true and switch the lines.
        """ 
        
        firstTask = "Run testEditTaskSwitchTasks first\n"
        secondTask = "Run testEditTaskSwitchTasks again"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None):
            return 1
            
        firstFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) != 2 or firstFileRes[0] != firstTask or firstFileRes[1] != secondTask):
            return 1

        taskNumbers = [0, 1]
        actionName = "switch"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        secondFileRes = Tests.readFile(testTaskList, testDirectoryName)

        # Note: The newline has been moved from the end of the first task to the end of the second task
        if(len(secondFileRes) == 2 and secondFileRes[0] == (secondTask + "\n") and secondFileRes[1] == firstTask.rstrip()):
            return 0

        return 1

    def testEditTaskInsertLastTask():
        """
        Test editTask() with a normal file, numbers, and line. Should return true and insert the taskNumber into the insertNumber. 
        The lines should shift up or down depending on the taskNumber and inserNumber.
        """ 
        
        firstTask = "Run testEditTaskInsertLastTask first\n"
        secondTask = "Run testEditTaskInsertLastTask again\n"
        thirdTask = "Run testEditTaskInsertLastTask and again"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)
        thirdFilePath = Tests.writeFile(thirdTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None or thirdFilePath == None):
            return 1
            
        firstFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) != 3 or firstFileRes[0] != firstTask or firstFileRes[1] != secondTask or firstFileRes[2] != thirdTask):
            return 1

        # First task to last postition. Second and third line should shift one line up.
        taskNumber = 0
        insertNumber = 2
        taskNumbers = [taskNumber, insertNumber]
        actionName = "insert"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        secondFileRes = Tests.readFile(testTaskList, testDirectoryName)

        # Note: The newline has been moved from the end of the first task to the end of the third task
        if(len(secondFileRes) == 3 and secondFileRes[0] == secondTask and secondFileRes[1] == (thirdTask + "\n") and secondFileRes[2] == firstTask.rstrip()):
            return 0

        return 1

    def testEditTaskInsertTask():
        """
        Test editTask() with a normal file, numbers, and line. Should return true and insert the taskNumber into the insertNumber. 
        The lines should shift up or down depending on the taskNumber and inserNumber.
        """ 
        
        firstTask = "Run testEditTaskInsertTask first\n"
        secondTask = "Run testEditTaskInsertTask again\n"
        thirdTask = "Run testEditTaskInsertTask and again"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)
        thirdFilePath = Tests.writeFile(thirdTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None or thirdFilePath == None):
            return 1
            
        firstFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) != 3 or firstFileRes[0] != firstTask or firstFileRes[1] != secondTask or firstFileRes[2] != thirdTask):
            return 1

        # Last task to first postition. First and second line should shift one line down.
        taskNumber = 2
        insertNumber = 0
        taskNumbers = [taskNumber, insertNumber]
        actionName = "insert"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        secondFileRes = Tests.readFile(testTaskList, testDirectoryName)

        # Note: The newline has been moved from the end of the second task to the end of the third task
        if(len(secondFileRes) == 3 and secondFileRes[0] == (thirdTask + "\n") and secondFileRes[1] == firstTask and secondFileRes[2] == secondTask.rstrip()):
            return 0

        return 1
        
    def testEditTaskIllegalTaskNumber():
        """
        Test editTask() with a normal file, but the number is not an array. Should return false and not alter the file.
        """ 
        
        task = "Run testEditTaskIllegalTaskNumber"
        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        illegalTaskNumber = 0
        actionName = "delete"
        permissions = "w"
        editRes = todo.Main.editTask(illegalTaskNumber, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == task):
            return 0

        return 1
        
    def testEditTaskNoActionNumber():
        """
        Test editTask() with a normal file, tasknumber, but the second number is not in the array. Should return false and not alter the file.
        """ 
        
        firstTask = "Run testEditTaskNoActionNumber first\n"
        secondTask = "Run testEditTaskNoActionNumber again"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None):
            return 1
            
        firstFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) != 2 or firstFileRes[0] != firstTask or firstFileRes[1] != secondTask):
            return 1

        taskNumbers = [0]
        actionName = "switch"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(editRes):
            return 1

        secondFileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(firstFileRes) == 2 and firstFileRes[0] == firstTask and firstFileRes[1] == secondTask):
            return 0

        return 1
    
    def testFormatPrintListNoFile():
        """
        Test formatPrintList() with a no previous file exisiting. Should return a empty array.
        """ 


        testDirPath = os.path.join(sys.path[0], testDirectoryName)
        testFilePath = os.path.join(testDirPath, testTaskList + ".txt")
        isTestFilePath = os.path.isfile(testFilePath)

        if(isTestFilePath):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        if(type(formatRes) == list and len(formatRes) == 0):
            return 0

        return 1
    
    def testFormatPrintListEmptyFile():
        """
        Test formatPrintList() with a an empty file. Should return an empty array.
        """ 

        task = ""

        filePath = Tests.writeFile(task, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(type(fileRes) != list or len(fileRes) != 0):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        if(type(formatRes) == list and len(formatRes) == 0):
            return 0

        return 1
        
    def testFormatPrintListMalformedZeroOne():
        """
        Test formatPrintList() with a file which has a malformed task line (no 0/1). Should return an array of the lines in a special format.
        """ 

        firstTask = "0 Run testFormatPrintListMalformedZeroOne normal entree\n"
        secondTask = "1 Run testFormatPrintListMalformedZeroOne normal entree\n"
        thirdTask = "Run testFormatPrintListMalformedZeroOne no completed number\n"
        fourthTask = "-1 Run testFormatPrintListMalformedZeroOne negative completed number"

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)
        thirdFilePath = Tests.writeFile(thirdTask, testTaskList, testDirectoryName)
        fourthFilePath = Tests.writeFile(fourthTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None or thirdFilePath == None or fourthFilePath == None):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        # Only check on array size, format should be checked in another test
        if(len(formatRes) != 4):
            return 1
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # First and second line should be fine
        normalLineCheck = fileRes[0] == firstTask and fileRes[1] == secondTask


        # Thid line is missing a completed number and fourth line has a negative number. 
        # Both should be rectified in the formating list and returned, as well as saved in the file.
        thirdLineCheck = fileRes[2] == "0 " + thirdTask
        fourthLineCheck = fileRes[3] == "0 " + fourthTask # Note that the "-1" is not removed

        if(normalLineCheck and thirdLineCheck and fourthLineCheck):
            return 0

        return 1

    def testFormatPrintListMalformedTaskText():
        """
        Test formatPrintList() with a file which has a malformed task line (no task text). This should return an array with the malformed lines removed
        and save the changes to the file.
        """

        firstTask = "0 Run testFormatPrintListMalformedTaskText next line is empty but has a completed number\n"
        secondTask = "1\n"
        thirdTask = "0 Run testFormatPrintListMalformedZeroOne no completed number or task\n"
        fourthTask = ""

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)
        thirdFilePath = Tests.writeFile(thirdTask, testTaskList, testDirectoryName)
        fourthFilePath = Tests.writeFile(fourthTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None or thirdFilePath == None or fourthFilePath == None):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        # Only check on array size, format should be checked in another test
        if(len(formatRes) != 2):
            return 1
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # First and thid line should be fine, the lines without text should be deleted, so line three is now line two.
        # Note: The newline on thridTask has been removed.
        normalLineCheck = fileRes[0] == firstTask and fileRes[1] == thirdTask.rstrip()

        if(normalLineCheck):
            return 0

        return 1
        
    def testFormatPrintListNormalFormat():
        """
        Test formatPrintList() with a normal file and content. This should return an array of formatted lines which is easier to read than the file.
        """

        firstTaskText = "Run testFormatPrintListNormalFormat not completed line"
        secondTaskText = "Run testFormatPrintListNormalFormat completed line"
        firstTask = "0 " + firstTaskText + "\n"
        secondTask = "1 " + secondTaskText

        firstFilePath = Tests.writeFile(firstTask, testTaskList, testDirectoryName)
        secondFilePath = Tests.writeFile(secondTask, testTaskList, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        # Format is:
        # [index] ["Yes"/"No"] [task]
        firstTaskFormat = "1\tNo\t\t" + firstTaskText + "\t"
        secondTaskFormat = "2\tYes\t\t" + secondTaskText + "\t"

        formatCheck = len(formatRes) == 2 and formatRes[0] == firstTaskFormat and formatRes[1] == secondTaskFormat
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # Check the file array
        fileCheck = fileRes[0] == firstTask and fileRes[1] == secondTask

        if(fileCheck and formatCheck):
            return 0

        return 1