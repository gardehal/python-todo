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

        # Run tests
        testGetFullFilePathDirectoryRes = Tests.testGetFullFilePathDirectory()
        Tests.after(useBeforeAfter)
        testGetFullFilePathDirectoryAndFileRes = Tests.testGetFullFilePathDirectoryAndFile()
        Tests.after(useBeforeAfter)
        testAddTaskNewTaskNewTaskListRes = Tests.testAddTaskNewTaskNewTaskList()
        Tests.after(useBeforeAfter)

        finalRes = testGetFullFilePathDirectoryRes + testGetFullFilePathDirectoryAndFileRes + testAddTaskNewTaskNewTaskListRes

        # Print
        print("The results of the tests are: \n")
        print("testGetFullFilePathDirectory \t" + ("passed." if testGetFullFilePathDirectoryRes == 0 else "failed."))
        print("testGetFullFilePathDirectoryAndFile \t" + ("passed." if testGetFullFilePathDirectoryAndFileRes == 0 else "failed."))
        print("testAddTaskNewTaskNewTaskList \t" + ("passed." if testAddTaskNewTaskNewTaskListRes == 0 else "failed."))

        print("\n" + ("All tests passed." if finalRes == 0 else "Some tests failed."))
        if(useBeforeAfter == 0):
            print("If some tests fail, try to run with before/after methods enabled, they are currently not; $ python todo.py -test")

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
            #  https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
            try:
                shutil.rmtree(fullDirPath)
                return 0
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))

        return 1

    def testGetFullFilePathDirectory():
        """
        Test getFullFilePath with directory name only. This should produce a string from C to the root of the python script pluss the directory name appened.
        """

        path = todo.Main.getFullFilePath(testDirectoryName) 
        sysPath = sys.path[0]

        if(path.__contains__(sysPath) and path.__contains__(testDirectoryName)):
            return 0

        return 1

    def testGetFullFilePathDirectoryAndFile():
        """
        Test getFullFilePath with directory and file. This should produce a string from C to the root of the python script pluss the directory name, 
        file name, and ".txt" appened.
        """

        path = todo.Main.getFullFilePath(testDirectoryName, testTaskList) 
        sysPath = sys.path[0]

        if(path.__contains__(sysPath) and path.__contains__(testDirectoryName) and path.__contains__(testTaskList) and path.__contains__(".txt")):
            return 0

        return 1

    def testAddTaskNewTaskNewTaskList():
        """
        Test addTask with task, testTaskList, and testDirectoryName. This should return True and make direcotry testDirectoryName and file testTaskList (.txt).
        The line inside the file should be task, with a 0 to indicate it's not a completed task, without any newlines.
        """

        task = "Run tests"
        taskRes = todo.Main.addTask(task, testTaskList, testDirectoryName)

        # Check if the directory was created
        testDirPath = os.path.join(sys.path[0], testDirectoryName)
        isTestDirPath = os.path.isdir(testDirPath)

        # Check if the file was created
        testFilePath = os.path.join(testDirPath, testTaskList + ".txt")
        isTestFilePath = os.path.isfile(testFilePath)

        print("pre fileread")
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