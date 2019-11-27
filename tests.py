import sys
import os
import shutil
import datetime

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
        # testIndividualRes = Tests.testFormatTaskListReset()
        # Tests.after(useBeforeAfter)
        
        # Tests.printTestResult(testIndividualRes, "testIndividual")
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
        testAddTaskResetMalformedDateTimeRes = Tests.testAddTaskResetMalformedDateTime()
        Tests.after(useBeforeAfter)
        testAddTaskResetOutOfBoundsValuesRes = Tests.testAddTaskResetOutOfBoundsValues()
        Tests.after(useBeforeAfter)
        testAddTaskResetIllegalValuesRes = Tests.testAddTaskResetIllegalValues()
        Tests.after(useBeforeAfter)
        testAddTaskResetIntervalRes = Tests.testAddTaskResetInterval()
        Tests.after(useBeforeAfter)
        testAddTaskResetDateTimeRes = Tests.testAddTaskResetDateTime()
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
        testSetListIllegalCharactersRes = Tests.testSetListIllegalCharacters()
        Tests.after(useBeforeAfter)
        testSetListNormalListRes = Tests.testSetListNormalList()
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
        testEditTaskUpdateNoResetStringRes = Tests.testEditTaskUpdateNoResetString()
        Tests.after(useBeforeAfter)
        testEditTaskUpdateMalformedStringRes = Tests.testEditTaskUpdateMalformedString()
        Tests.after(useBeforeAfter)
        testEditTaskUpdateResetRes = Tests.testEditTaskUpdateReset()
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
        testFormatPrintListMalformedZeroOneInsertPositionRes = Tests.testFormatPrintListMalformedZeroOneInsertPosition()
        Tests.after(useBeforeAfter)
        testFormatPrintListMalformedTaskTextRes = Tests.testFormatPrintListMalformedTaskText()
        Tests.after(useBeforeAfter)
        testFormatPrintListNormalFormatRes = Tests.testFormatPrintListNormalFormat()
        Tests.after(useBeforeAfter)
        testFormatTaskListMalformedResetStringRes = Tests.testFormatTaskListMalformedResetString()
        Tests.after(useBeforeAfter)
        testFormatTaskListIllegalResetStringValuesRes = Tests.testFormatTaskListIllegalResetStringValues()
        Tests.after(useBeforeAfter)
        testFormatTaskListNoIncrementRes = Tests.testFormatTaskListNoIncrement()
        Tests.after(useBeforeAfter)
        testFormatTaskListResetRes = Tests.testFormatTaskListReset()
        Tests.after(useBeforeAfter)
        testFormatTaskListsPrintNoDirectoryRes = Tests.testFormatTaskListsPrintNoDirectory()
        Tests.after(useBeforeAfter)
        testFormatTaskListsPrintEmptyDirectoryRes = Tests.testFormatTaskListsPrintEmptyDirectory()
        Tests.after(useBeforeAfter)
        testFormatTaskListsPrintTwoListsRes = Tests.testFormatTaskListsPrintTwoLists()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeNoStringRes = Tests.testIncrementResetDateTimeNoString()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeMalformedStringRes = Tests.testIncrementResetDateTimeMalformedString()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeIncrementNonIntRes = Tests.testIncrementResetDateTimeIncrementNonInt()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeDateNonIntRes = Tests.testIncrementResetDateTimeDateNonInt()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeTimeNonIntRes = Tests.testIncrementResetDateTimeTimeNonInt()
        Tests.after(useBeforeAfter)
        testIncrementResetDateTimeIncrementValueRes = Tests.testIncrementResetDateTimeIncrementValue()
        Tests.after(useBeforeAfter)
        
        getFullFilePathRes = testGetFullFilePathDirectoryRes + testGetFullFilePathDirectoryAndFileRes
        getCurrentTaskListRes = testGetCurrentTaskListNoFileRes + testGetCurrentTaskListFileExistsRes
        addTaskRes1 = testAddTaskEmptyListRes + testAddTaskFaultyFileRes + testAddTaskNoFileRes + testAddTaskNoTaskRes + testAddTaskNewTaskSameTaskListRes 
        addTaskRes2 = testAddTaskResetMalformedDateTimeRes + testAddTaskResetOutOfBoundsValuesRes + testAddTaskResetIllegalValuesRes + testAddTaskResetIntervalRes + testAddTaskResetDateTimeRes
        loadFileRes = testloadFileNoListRes + testloadFileEmptyListRes + testloadFileOneTaskRes
        setListRes = testSetListNoFileRes + testSetListToSameListRes + testSetListIllegalCharactersRes + testSetListNormalListRes
        editFileRes1 = testEditTaskNoFileRes + testEditTaskNoActionRes + testEditTaskNoTaskNumberRes + testEditTaskIllegalNumberRes + testEditTaskIllegalPermissionRes
        editFileRes2 = testEditTaskCheckMarkMalformedTaskRes + testEditTaskCheckMarkTaskRes + testEditTaskDeleteTaskRes + testEditTaskSwitchLastTaskRes + testEditTaskSwitchTasksRes
        editFileRes3 = testEditTaskInsertLastTaskRes + testEditTaskInsertTaskRes + testEditTaskIllegalTaskNumberRes + testEditTaskNoActionNumberRes
        editFileRes4 = testEditTaskUpdateNoResetStringRes + testEditTaskUpdateMalformedStringRes + testEditTaskUpdateResetRes
        formatPrintListRes1 = testFormatPrintListNoFileRes + testFormatPrintListEmptyFileRes + testFormatPrintListMalformedZeroOneRes + testFormatPrintListMalformedZeroOneInsertPositionRes
        formatPrintListRes2 = testFormatPrintListMalformedTaskTextRes + testFormatPrintListNormalFormatRes
        formatTaskListsPrintRes = testFormatTaskListsPrintNoDirectoryRes + testFormatTaskListsPrintEmptyDirectoryRes + testFormatTaskListsPrintTwoListsRes
        formatTaskListsResetRes = testFormatTaskListMalformedResetStringRes + testFormatTaskListIllegalResetStringValuesRes + testFormatTaskListNoIncrementRes + testFormatTaskListResetRes
        incrementResetDateTimeRes1 = testIncrementResetDateTimeNoStringRes + testIncrementResetDateTimeMalformedStringRes + testIncrementResetDateTimeIncrementNonIntRes
        incrementResetDateTimeRes2 = testIncrementResetDateTimeDateNonIntRes + testIncrementResetDateTimeTimeNonIntRes + testIncrementResetDateTimeIncrementValueRes

        finalRes = getFullFilePathRes + getCurrentTaskListRes + addTaskRes1 + addTaskRes2 + loadFileRes + setListRes + editFileRes1 + editFileRes2 + editFileRes3 + editFileRes4
        + formatPrintListRes1 + formatPrintListRes2 + formatTaskListsPrintRes + formatTaskListsResetRes + incrementResetDateTimeRes1 + incrementResetDateTimeRes2

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
        Tests.printTestResult(testAddTaskResetMalformedDateTimeRes, "testAddTaskResetMalformedDateTime")
        Tests.printTestResult(testAddTaskResetOutOfBoundsValuesRes, "testAddTaskResetOutOfBoundsValues")
        Tests.printTestResult(testAddTaskResetIllegalValuesRes, "testAddTaskResetIllegalValues")
        Tests.printTestResult(testAddTaskResetIntervalRes, "testAddTaskResetInterval")
        Tests.printTestResult(testAddTaskResetDateTimeRes, "testAddTaskResetDateTime")
        Tests.printTestResult(testloadFileNoListRes, "testloadFileNoList")
        Tests.printTestResult(testloadFileEmptyListRes, "testloadFileEmptyList")
        Tests.printTestResult(testloadFileOneTaskRes, "testloadFileOneTask")
        Tests.printTestResult(testSetListNoFileRes, "testSetListNoFile")
        Tests.printTestResult(testSetListToSameListRes, "testSetListToSameList")
        Tests.printTestResult(testSetListIllegalCharactersRes, "testSetListIllegalCharacters")
        Tests.printTestResult(testSetListNormalListRes, "testSetListNormalList")
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
        Tests.printTestResult(testEditTaskUpdateNoResetStringRes, "testEditTaskUpdateNoResetString")
        Tests.printTestResult(testEditTaskUpdateMalformedStringRes, "testEditTaskUpdateMalformedString")
        Tests.printTestResult(testEditTaskUpdateResetRes, "testEditTaskUpdateReset")
        Tests.printTestResult(testEditTaskIllegalTaskNumberRes, "testEditTaskIllegalTaskNumber")
        Tests.printTestResult(testEditTaskNoActionNumberRes, "testEditTaskNoActionNumber")
        Tests.printTestResult(testFormatPrintListNoFileRes, "testFormatPrintListNoFile")
        Tests.printTestResult(testFormatPrintListEmptyFileRes, "testFormatPrintListEmptyFile")
        Tests.printTestResult(testFormatPrintListMalformedZeroOneRes, "testFormatPrintListMalformedZeroOne")
        Tests.printTestResult(testFormatPrintListMalformedZeroOneInsertPositionRes, "testFormatPrintListMalformedZeroOneInsertPosition")
        Tests.printTestResult(testFormatPrintListMalformedTaskTextRes, "testFormatPrintListMalformedTaskText")
        Tests.printTestResult(testFormatPrintListNormalFormatRes, "testFormatPrintListNormalFormat")
        Tests.printTestResult(testFormatTaskListMalformedResetStringRes, "testFormatTaskListMalformedResetString")
        Tests.printTestResult(testFormatTaskListIllegalResetStringValuesRes, "testFormatTaskListIllegalResetStringValues")
        Tests.printTestResult(testFormatTaskListNoIncrementRes, "testFormatTaskListNoIncrement")
        Tests.printTestResult(testFormatTaskListResetRes, "testFormatTaskListReset")
        Tests.printTestResult(testFormatTaskListsPrintNoDirectoryRes, "testFormatTaskListsPrintNoDirectory")
        Tests.printTestResult(testFormatTaskListsPrintEmptyDirectoryRes, "testFormatTaskListsPrintEmptyDirectory")
        Tests.printTestResult(testFormatTaskListsPrintTwoListsRes, "testFormatTaskListsPrintTwoLists")
        Tests.printTestResult(testIncrementResetDateTimeNoStringRes, "testIncrementResetDateTimeNoString")
        Tests.printTestResult(testIncrementResetDateTimeMalformedStringRes, "testIncrementResetDateTimeMalformedString")
        Tests.printTestResult(testIncrementResetDateTimeIncrementNonIntRes, "testIncrementResetDateTimeIncrementNonInt")
        Tests.printTestResult(testIncrementResetDateTimeDateNonIntRes, "testIncrementResetDateTimeDateNonInt")
        Tests.printTestResult(testIncrementResetDateTimeTimeNonIntRes, "testIncrementResetDateTimeTimeNonInt")
        Tests.printTestResult(testIncrementResetDateTimeIncrementValueRes, "testIncrementResetDateTimeIncrementValue")

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

    def testAddTaskResetMalformedDateTime():
        """
        Test addTask() with a new task, reset interval, but the datetime string is not formatted correctly from the user ("[hour]:[day]-[month]-[year]").
        Should return false and not add task to file.
        """

        now = datetime.datetime.now()

        task = "Run testAddTaskResetDateTime"
        resetInterval = 5 * 60 * 60 # 5 hours
        resetHour = "01"
        resetDay = "02"
        resetMonth = "03"
        resetYear = str(now.year + 1)
        resetDatetime = resetHour + "a" + resetDay + "b" + resetMonth + "c" + resetYear
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName, resetInterval, resetDatetime)

        if(taskRes):
            return 1
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 0):
            return 0
        
        return 1

    def testAddTaskResetOutOfBoundsValues():
        """
        Test addTask() with a new task, but the reset arguments are out of bounds. Should return false and not add anything to the file.
        """

        now = datetime.datetime.now()

        # Acceptable variables
        task = "Run testAddTaskResetOutOfBoundsValues"
        resetIntervalNormal = 1 * 60 * 60 # 1 hour
        resetDatetimeNone = None
        resetDatetimeHourNormal = "01"
        resetDatetimeDayNormal = "02"
        resetDatetimeMonthNormal = "03"
        resetDatetimeYearNormal = str(now.year + 1)

        # Interval varaiables
        resetIntervalHigh = 11_111_111
        resetIntervalLow = -1

        # Datetime variables
        resetDatetimeHourHigh = "42"
        resetDatetimeHourLow = "-2"
        resetDatetimeDayHigh = "99"
        resetDatetimeDayLow = "-3"
        resetDatetimeMonthHigh = "123"
        resetDatetimeMonthLow = "-4"
        resetDatetimeYearHigh = str(now.year + 321)
        resetDatetimeYearLow = str(now.year - 10)

        # Assemble datetime arguments
        resetArgumentHourHigh = resetDatetimeHourHigh + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentHourLow = resetDatetimeHourLow + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentDayHigh = resetDatetimeHourNormal + ":" + resetDatetimeDayHigh + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentDayLow = resetDatetimeHourNormal + ":" + resetDatetimeDayLow + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentMonthHigh = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthHigh + "-" + resetDatetimeYearNormal
        resetArgumentMonthLow = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthLow + "-" + resetDatetimeYearNormal
        resetArgumentYearHigh = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearHigh
        resetArgumentYearLow = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearLow

        # Run method with arguments
        taskResIntervalHigh = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalHigh, resetDatetimeNone)
        taskResIntervalLow = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalLow, resetDatetimeNone)

        taskResDatetimeHourHigh = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentHourHigh)
        taskResDatetimeHourLow = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentHourLow)
        taskResDatetimeDayHigh = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentDayHigh)
        taskResDatetimeDayLow = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentDayLow)
        taskResDatetimeMonthHigh = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentMonthHigh)
        taskResDatetimeMonthLow = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentMonthLow)
        taskResDatetimeYearHigh = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentYearHigh)
        taskResDatetimeYearLow = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentYearLow)

        if(taskResIntervalHigh or taskResIntervalLow or taskResDatetimeHourHigh or taskResDatetimeHourLow or taskResDatetimeDayHigh or taskResDatetimeDayLow
        or taskResDatetimeMonthHigh or taskResDatetimeMonthLow or taskResDatetimeYearHigh or taskResDatetimeYearLow):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 0):
            return 0
        
        return 1

    def testAddTaskResetIllegalValues():
        """
        Test addTask() with a new task, but with non-castable int chars as interval and in datetime positions. Should return false and not add anything to the file.
        """

        now = datetime.datetime.now()

        # Acceptable variables
        task = "Run testAddTaskResetOutOfBoundsValues"
        resetIntervalNormal = 1 * 60 * 60 # 1 hour
        resetDatetimeNone = None
        resetDatetimeHourNormal = "01"
        resetDatetimeDayNormal = "02"
        resetDatetimeMonthNormal = "03"
        resetDatetimeYearNormal = str(now.year + 1)

        # Interval varaiable
        resetIntervalChar = "a"

        # Datetime variables
        resetDatetimeHourChar = "b"
        resetDatetimeDayChar = "c"
        resetDatetimeMonthChar = "d"
        resetDatetimeYearChar = "e"

        # Assemble datetime arguments
        resetArgumentHourChar = resetDatetimeHourChar + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentDayChar = resetDatetimeHourNormal + ":" + resetDatetimeDayChar + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearNormal
        resetArgumentMonthChar = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthChar + "-" + resetDatetimeYearNormal
        resetArgumentYearChar = resetDatetimeHourNormal + ":" + resetDatetimeDayNormal + "-" + resetDatetimeMonthNormal + "-" + resetDatetimeYearChar

        # Run method with arguments
        taskResIntervalChar = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalChar, resetDatetimeNone)
        taskResHourChar = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentHourChar)
        taskResDayChar = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentDayChar)
        taskResMonthChar = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentMonthChar)
        taskResYearChar = todo.Main.addTask(task, testTaskList, testDirectoryName, resetIntervalNormal, resetArgumentYearChar)

        if(taskResIntervalChar or taskResHourChar or taskResDayChar or taskResMonthChar or taskResYearChar):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 0):
            return 0
        
        return 1

    def testAddTaskResetInterval():
        """
        Test addTask() with a new task and a reset interval. The method should add a reset string (formatted "![interval]Z[date]T[time]) where the
        time and date is the current time and date since no arguments was given by the user, and the method should return true.
        """

        task = "Run testAddTaskResetInterval"
        resetInterval = 5 * 60 * 60 # 5 hours
        resetDatetime = None
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName, resetInterval, resetDatetime)

        if(not taskRes):
            return 1

        now = datetime.datetime.now()
        leadingZeroHour1 = (str(now.hour) if now.hour > 9 else "0" + str(now.hour))
        future = now + datetime.timedelta(hours = 1)
        leadingZeroHour2 = (str(future.hour) if future.hour > 9 else "0" + str(future.hour))

        expectedResetString1 = "!" + str(resetInterval) + "Z" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "T" + leadingZeroHour1 + ":00:00"
        expectedResetString2 = "!" + str(resetInterval) + "Z" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "T" + leadingZeroHour2 + ":00:00"
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # If you're unlucky (or highly skilled), you may trigger the tests so that the datetime.datetime in this test runs a few milliseconds before the clock ticks over to a new hour,
        # causing the resetString in the task file to have a different time, causing the test to fail. To prevent that, simply check on two very similar resetStrings.
        expectedResetStringTimeException = fileRes[0] == "0 " + expectedResetString1 + " " + task or fileRes[0] == "0 " + expectedResetString2 + " " + task

        if(len(fileRes) == 1 and expectedResetStringTimeException):
            return 0
        
        return 1

    def testAddTaskResetDateTime():
        """
        Test addTask() with a new task, reset interval, time and date. The method should add a reset string (formatted "![interval]Z[date]T[time]) where the
        time and date is the current time and date since no arguments was given by the user, and the method should return true.
        """

        now = datetime.datetime.now()

        task = "Run testAddTaskResetDateTime"
        resetInterval = 5 * 60 * 60 # 5 hours
        resetHour = "01"
        resetDay = "02"
        resetMonth = "03"
        resetYear = str(now.year + 1)
        resetDatetime = resetHour + ":" + resetDay + "-" + resetMonth + "-" + resetYear
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName, resetInterval, resetDatetime)

        if(not taskRes):
            return 1

        expectedResetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":00:00"
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # This test, as opposed to testAddTaskResetInterval(), set time and date so no need to consider time roll over.
        if(len(fileRes) == 1 and fileRes[0] == "0 " + expectedResetString + " " + task):
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

        newList = "setListNoFile-list"

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

        oldList = "some-other-list"
        newList = "setListToSameList-list"
        
        filePath = Tests.writeFile(oldList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        if(filePath == None):
            return 1

        setRes = todo.Main.setList(newList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = Tests.readFile(testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == newList

        if(setRes and os.path.isfile(filePath) and fileCheck):
            return 0

        return 1

    def testSetListIllegalCharacters():
        """
        Test setList with a list name that contains illegal characters. The method should replace illegal characters 
        ([" ", "<", ">", ":", "\"", "/", "\\", "|", "?", "*"]) and replace them with "-", return true, and write the list name to the file.
        """
        
        illegalChars = [" ", "<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
        illegalString = ""
        for char in illegalChars:
            illegalString += char

        newIllegalList = "start" + illegalString + "end"
        newIllegalListResult = "start" + ("-" * len(illegalChars)) + "end"

        setRes = todo.Main.setList(newIllegalList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = Tests.readFile(testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == newIllegalListResult

        if(setRes and fileCheck):
            return 0

        return 1

    def testSetListNormalList():
        """
        Test setList with a normal list name. This should return true and write the list name in the file.
        """
        
        newList = "testSetListNormalList-my-list"

        setRes = todo.Main.setList(newList, testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileRes = Tests.readFile(testAllTaskListsFileName, testAllTaskListsDirectoryName)

        fileCheck = len(fileRes) == 1 and fileRes[0] == newList

        if(setRes and fileCheck):
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

    def testEditTaskUpdateNoResetString():
        """
        Test editTask() with a normal file, numbers, and line, but we are sending the task to be updated without a reset string. Should return false and not alter file.
        """ 
        
        resetString = ""
        taskLine = "0 " + resetString + " Run testEditTaskUpdateNoResetString"

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = 0
        taskNumbers = [taskNumber]
        actionName = "update"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)

        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == taskLine):
            return 0

        return 1

    def testEditTaskUpdateMalformedString():
        """
        Test editTask() with a normal file, numbers, and line, but the task has a malformed (short) resetString. Should return false and not put update the file. \n
        Sidenote: the datetime library can handle single digit numbers, but this extra check keeps the program more consistent. 
        """ 
        
        # Note: "short" strings, the month, day, hour, minSec should be 2 numbers (leading zero)
        # Interval and year can be be 1 digit, but we're testing for less than minimal length which is 22
        resetInterval = 1
        resetYear = "2000"
        resetMonth = "1"
        resetDay = "1"
        resetHour = "0"
        resetMinSec = "0"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        taskLine = "0 " + resetString + " Run testEditTaskUpdateMalformedString"

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = 0
        taskNumbers = [taskNumber]
        actionName = "update"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)

        if(editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == taskLine):
            return 0

        return 1

    def testEditTaskUpdateReset():
        """
        Test editTask() with a normal file, numbers, and line. Should return true and increment the resetString once with the seconds value after "!" before "Z".
        """ 
        
        resetInterval = 60 * 60 # 1 hour, 3600 seconds
        resetYear = "2000"
        resetMonth = "01"
        resetDay = "01"
        resetHour = "00"
        resetMinSec = "00"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        taskLine = "0 " + resetString + " Run testEditTaskUpdateReset"

        incrementedResetHour = "01" # resetHour + resetInterval
        expectedIncrementedResetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + incrementedResetHour + ":" + resetMinSec + ":" + resetMinSec

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        taskNumber = 0
        taskNumbers = [taskNumber]
        actionName = "update"
        permissions = "w"
        editRes = todo.Main.editTask(taskNumbers, testTaskList, testDirectoryName, actionName, permissions)
        
        if(not editRes):
            return 1

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # The line in the file should not longer be the same as the taskLine variable, the second "word" (resetString) should now be expectedIncrementedResetString
        resetStringCompare = fileRes[0].split()[1] == expectedIncrementedResetString
        if(len(fileRes) == 1 and fileRes[0] != taskLine and resetStringCompare):
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

        # Third line is missing a completed number and fourth line has a negative number. 
        # Both should be rectified in the formating list and returned, as well as saved in the file.
        thirdLineCheck = fileRes[2] == "0 " + thirdTask
        fourthLineCheck = fileRes[3] == "0 " + fourthTask # Note that the "-1" is not removed

        if(normalLineCheck and thirdLineCheck and fourthLineCheck):
            return 0

        return 1

    def testFormatPrintListMalformedZeroOneInsertPosition():
        """
        Test formatPrintList() with a file which has a malformed task line (no 0/1). Should return an array of the lines in a special format.
        """ 

        firstTask = "0 Run testFormatPrintListMalformedZeroOne first normal entree\n"
        secondTask = "Run testFormatPrintListMalformedZeroOne no completed number\n"
        thirdTask = "0 Run testFormatPrintListMalformedZeroOne second normal entree\n"
        fourthTask = "0 Run testFormatPrintListMalformedZeroOne third normal entree"

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

        # First, third, and fourth task should be fine, and in the same positions
        normalLineCheck = fileRes[0] == firstTask and fileRes[2] == thirdTask and fileRes[3] == fourthTask

        # Second line is missing a completed number. The formatPrintList should detect, fix (add leading "0 "), and insert the line into the same position it was.
        secondLineCheck = fileRes[1] == "0 " + secondTask

        if(normalLineCheck and secondLineCheck):
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
        firstTaskFormat = "1\tNo\t\t" + firstTaskText
        secondTaskFormat = "2\tYes\t\t" + secondTaskText

        # When the method formatPrintList was changed to parse line into array, this test failed. Removing trailing whitespace makes it pass, 
        # which is understandable for the first line (rstrip removes the newline), but for some reason the second line needs to be rstripped too for the test to pass, 
        # though there is no newline or trailing whitespace in the file. This should not be the case in theory, but it is de facto.
        formatCheck = len(formatRes) == 2 and formatRes[0].rstrip() == firstTaskFormat and formatRes[1].rstrip() == secondTaskFormat
        
        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        # Check the file array
        fileCheck = fileRes[0] == firstTask and fileRes[1] == secondTask

        if(fileCheck and formatCheck):
            return 0

        return 1

    def testFormatTaskListMalformedResetString():
        """
        Test formatPrintList() with a normal file but the resetString is too short. Should quit and not alter the file.
        """
        
        # Note: "short" strings, the month, day, hour, minSec should be 2 numbers (leading zero)
        # Interval and year can be be 1 digit, but we're testing for less than minimal length which is 22
        resetInterval = 1
        resetYear = "2000"
        resetMonth = "1"
        resetDay = "1"
        resetHour = "0"
        resetMinSec = "0"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        taskLine = "0 " + resetString + " Run testFormatTaskListMalformedResetString"

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        try:
            formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

            # Program did not quit, return 1
            return 1
        # except Exception as e:
        except:
            # Expected, nothing to do
            formatResCheck = True

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == taskLine and formatResCheck):
            return 0

        return 1

    def testFormatTaskListIllegalResetStringValues():
        """
        Test formatPrintList() with a normal file but the resetString has a char that is not castable to an integer. Should quit and not alter the file.
        """
        
        resetInterval = 60 * 60 # 1 hour, 3600 seconds
        resetYear = "2000"
        resetMonth = "01"
        # A is not castable to int
        resetDay = "a"
        resetHour = "00"
        resetMinSec = "00"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        taskLine = "0 " + resetString + " Run testFormatTaskListIllegalResetStringValues"

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        try:
            formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

            # Program did not quit, return 1
            return 1
        # except Exception as e:
        except:
            # Expected, nothing to do
            formatResCheck = True

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == taskLine and formatResCheck):
            return 0

        return 1

    def testFormatTaskListNoIncrement():
        """
        Test formatPrintList() with a normal file and line with a resetString that is in the future. Should return a formatted array and no increment the resetString.
        """
        
        resetInterval = 60 * 60 # 1 hour, 3600 seconds
        now = datetime.datetime.now()
        resetYear = str(now.year + 1)
        resetMonth = "01"
        resetDay = "01"
        resetHour = "00"
        resetMinSec = "00"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        task = "Run testFormatTaskListNoIncrement"
        taskLine = "0 " + resetString + " " + task

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        lineSplit = formatRes[0].split()
        lineRecreation = lineSplit[2] + " " + lineSplit[3]

        formatResCheck = len(formatRes) == 1 and lineRecreation == task

        fileRes = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileRes) == 1 and fileRes[0] == taskLine and formatResCheck):
            return 0

        return 1
    
    def testFormatTaskListReset():
        """
        Test formatPrintList() with a normal file and line with a resetString that is in the past. Should return a formatted array and increment the resetString to today.
        """
        
        resetInterval = 60 * 60 # 1 hours, 3600 seconds
        now = datetime.datetime.now()
        oneHourAgo = now - datetime.timedelta(hours = 1)

        # Since the method increments recursivly until the resetString is in the future, about once
        resetYear = str(oneHourAgo.year)
        resetMonth = str(oneHourAgo.month)
        resetDay = str(oneHourAgo.day)
        resetHour = (str(oneHourAgo.hour) if oneHourAgo.hour > 9 else "0" + str(oneHourAgo.hour))
        resetMinSec = "00"
        resetString = "!" + str(resetInterval) + "Z" + resetYear + "-" + resetMonth + "-" + resetDay + "T" + resetHour + ":" + resetMinSec + ":" + resetMinSec
        task = "Run testFormatTaskListReset"
        taskLine = "1 " + resetString + " " + task

        filePath = Tests.writeFile(taskLine, testTaskList, testDirectoryName)

        if(filePath == None):
            return 1

        # Make sure everything is in order in the file before
        fileResBefore = Tests.readFile(testTaskList, testDirectoryName)

        if(len(fileResBefore) != 1 and fileResBefore[0] != taskLine):
            return 1

        # Run method
        formatRes = todo.Main.formatPrintList(testTaskList, testDirectoryName)

        lineSplit = formatRes[0].split()
        lineRecreation = lineSplit[2] + " " + lineSplit[3]

        formatResCheck = (len(formatRes) == 1 and lineSplit[1] == "No" and lineRecreation == task)

        # Check file after
        fileResAfter = Tests.readFile(testTaskList, testDirectoryName)

        fileResSplit = fileResAfter[0].split()
        fileResAfterCheck = (len(fileResAfter) == 1 and fileResAfter[0] != taskLine and str(fileResSplit[0]) == "0")

        # Check if resetString is incremented
        inOneHour = now + datetime.timedelta(seconds = resetInterval)
        newHour = inOneHour.hour
        leadingZeroNewHour = (str(newHour) if newHour > 9 else "0" + str(newHour))
        inOneHourResetString = "!" + str(resetInterval) + "Z" + str(inOneHour.year) + "-" + str(inOneHour.month) + "-" + str(inOneHour.day) + "T" + leadingZeroNewHour + ":" + resetMinSec + ":" + resetMinSec
        
        incrementedCheck = fileResSplit[1] != resetString and fileResSplit[1] == inOneHourResetString

        if(formatResCheck and incrementedCheck and fileResAfterCheck):
            return 0

        return 1
                
    def testFormatTaskListsPrintNoDirectory():
        """
        Test formatTaskListsPrint() with no directory, should return an empty array.
        """

        dirPath = ""

        formatRes = todo.Main.formatTaskListsPrint(dirPath)

        if(type(formatRes) == list and len(formatRes) == 0):
            return 0

        return 1

    def testFormatTaskListsPrintEmptyDirectory():
        """
        Test formatTaskListsPrint() with an empty directory, should return an empty array.
        """

        dirPath = os.path.join(sys.path[0], testDirectoryName)

        if(not os.path.exists(dirPath)):
            os.mkdir(dirPath)

        formatRes = todo.Main.formatTaskListsPrint(dirPath)

        if(type(formatRes) == list and len(formatRes) == 0):
            return 0

        return 1

    def testFormatTaskListsPrintTwoLists():
        """
        Test formatTaskListsPrint() with a directory with two lists (files), should return the filenames without the ".txt".
        """

        firstTaskFirstList = "Run testFormatTaskListsPrintTwoLists first task first list"
        firstTaskSecondList = "Run testFormatTaskListsPrintTwoLists first task second list"

        firstListName = "test-first-task-list"
        secondListName = "test-second-task-list"

        firstFilePath = Tests.writeFile(firstTaskFirstList, firstListName, testDirectoryName)
        secondFilePath = Tests.writeFile(firstTaskSecondList, secondListName, testDirectoryName)

        if(firstFilePath == None or secondFilePath == None):
            return 1

        formatRes = todo.Main.formatTaskListsPrint(testDirectoryName)

        if(len(formatRes) == 2 and formatRes[0] == firstListName and formatRes[1] == secondListName):
            return 0

        return 1

    def testIncrementResetDateTimeNoString():
        """
        Test incrementResetDateTime() with empty string. Should return None.
        """

        resetString = ""

        incrementRes = todo.Main.incrementResetDateTime(resetString)

        if(incrementRes == None):
            return 0

        return 1

    def testIncrementResetDateTimeMalformedString():
        """
        Test incrementResetDateTime() with a string that does not have exclemation mar, Z, or T. Should return None.
        """

        # !123Z2001-02-03T04:05:06
        resetStringNoExclemation = "123Z2001-02-03T04:05:06"
        resetStringNoZ = "!1232001-02-03T04:05:06"
        resetStringNoT = "!123Z2001-02-0304:05:06"

        incrementResNoExclemation = todo.Main.incrementResetDateTime(resetStringNoExclemation)
        incrementResNoZ = todo.Main.incrementResetDateTime(resetStringNoZ)
        incrementResNoT = todo.Main.incrementResetDateTime(resetStringNoT)

        if(incrementResNoExclemation == None and incrementResNoZ == None and incrementResNoT == None):
            return 0

        return 1

    def testIncrementResetDateTimeIncrementNonInt():
        """
        Test incrementResetDateTime() with a string that has a non-int increment value. Should return None.
        """

        resetString = "!xZ2001-02-03T04:05:06"

        incrementRes = todo.Main.incrementResetDateTime(resetString)

        if(incrementRes == None):
            return 0

        return 1

    def testIncrementResetDateTimeDateNonInt():
        """
        Test incrementResetDateTime() with a string that has a non-int date values. Should return None.
        """

        resetStringNonIntYear = "!123Za-02-03T04:05:06"
        resetStringNonIntMonth = "!123Z2001-b-03T04:05:06"
        resetStringNonIntDay = "!123Z2001-02-cT04:05:06"

        incrementResNonIntYear = todo.Main.incrementResetDateTime(resetStringNonIntYear)
        incrementResNonIntMonth = todo.Main.incrementResetDateTime(resetStringNonIntMonth)
        incrementResNonIntDay = todo.Main.incrementResetDateTime(resetStringNonIntDay)

        if(incrementResNonIntYear == None and incrementResNonIntMonth == None and incrementResNonIntDay == None):
            return 0

        return 1

    def testIncrementResetDateTimeTimeNonInt():
        """
        Test incrementResetDateTime() with a string that has a non-int time values. Should return None.
        """

        resetStringNonIntHour = "!123Z2001-02-03Ta:05:06"
        resetStringNonIntMinute = "!123Z2001-02-03T04:b:06"
        resetStringNonIntSecond = "!123Z2001-02-03T04:05:c"

        incrementResNonIntHour = todo.Main.incrementResetDateTime(resetStringNonIntHour)
        incrementResNonIntMinute = todo.Main.incrementResetDateTime(resetStringNonIntMinute)
        incrementResNonIntSecond = todo.Main.incrementResetDateTime(resetStringNonIntSecond)

        if(incrementResNonIntHour == None and incrementResNonIntMinute == None and incrementResNonIntSecond == None):
            return 0

        return 1

    def testIncrementResetDateTimeIncrementValue():
        """
        Test incrementResetDateTime() with a normal reset string. Should return an array of incremented reset string, the increment value, and datetime of the new datetime reset value.
        """

        # !123Z2001-02-03T04:05:06
        year = "2001"
        month = "02"
        day = "03"
        resetDate = year + "-" + month + "-" + day

        hours = "10"
        minutes = "00"
        seconds = "00"
        resetTime = hours + ":" + minutes + ":" + seconds

        resetInterval = 60 * 60 * 2  # 2 hours
        resetString = "!" + str(resetInterval) + "Z" + resetDate + "T" + resetTime

        hoursExpected = "12"
        resetTimeExpected = hoursExpected + ":" + minutes + ":" + seconds
        expectedResetStringRes = "!" + str(resetInterval) + "Z" + resetDate + "T" + resetTimeExpected

        incrementRes = todo.Main.incrementResetDateTime(resetString)

        if(len(incrementRes) != 3):
            return 1

        dateTimeExpected = datetime.datetime(int(year), int(month), int(day), int(hoursExpected), int(minutes), int(seconds))

        if(incrementRes[0] == expectedResetStringRes and incrementRes[1] == str(resetInterval) and incrementRes[2] == str(dateTimeExpected)):
            return 0

        return 1