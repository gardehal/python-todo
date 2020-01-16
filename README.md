# python-todo
 
Python console program for managing TODO-tasks.
 
## Usage (Windows)
1. [Install Python](https://www.python.org/downloads/)
2. Make sure Python is defined on PATH
3. Navigate to folder in CLI
4. $ python todo.py [arguments...]
 
## Help
- Arguments marked with ? are optional.
- All arguments that triggers a function start with dash(-).
- All arguments must be separated by space only.
- To submit sentences with spaces between words, use quotation marks (", '), otherwise they will be counted as separate arguments.
-         e.g.: $ python todo.py -add "This is a sentence." 
 
- To apply the automatic reset for a task, it must be added with an string as the third argument, which is the interval between reset,
- simply "[int]", or "[char][int]". The char can be "h" for hours (default), "d" for days, "w" for weeks, or "m" for months. Maximum 3.5 months.
- To give a time of day or date for when the interval should trigger from, add a custom string as the fourth argument, which is "[time of day, hours]:[date of month]-- [month]-[year]",
- each of which are optional, but require the value before (i.e. day require hour, month require day and so on). Minimum on year into the past, 5 years into the future.
-         e.g.: $ python todo.py -add "Daily watering plants" d1 12:30-01-2020
 
- ['-tasks', '-t']: prints an indexed list of tasks in the current task list.
- ['-lists', '-l']: prints a list of all task lists.
- ['-add', '-a'] + string + ?string + ?string: adds the following string to the current task list.
- ['-delete', '-d'] + number: deletes the corresponding task in the current task list.
- ['-check', '-c', '-x'] + number: toggle the completion of the corresponding task in the current task list.
- ['-switch', '-s']+ number + number: switches the position of the two corresponding tasks in the current task list.
- ['-insert', '-i']+ number + number: inserts the task (first number) into position of the second number.
- ['-setlist', '-sl']: string: sets the current task list to the string given.
- ['-help', '-h']: prints this information about input arguments.
- ['-test']: runs unit tests and prints the result.
 
## My Thoughts
I wanted a way to manage some tasks I had to do that sometime repeated daily and the mental list got out of hand. I needed a way to write them down and keep them handy without having to plaster my wall with post-it notes, which is why I thought about making this program. I am aware that there are programs like this out there, as with some of the other projects I have done, but I need some specific functions to help me manage my lists. 
 
This is not the first time I've made a TODO list, but the previous one is dated and it would be more work and less beneficial rewriting  the old code (PHP). I was unsure what language to choose for this project, but I'm going with Python as I enjoy writing  it and have no need for a online version just yet. I did consider learning Ember or Vue or something similar to cultivate my frontend skills, and might redo this project with that in the future.
 
## Conclusion
As the project comes to an ending, I think back to what I have accomplished and what I did wrong. The following list is a short summation in no order and includes good and bad things.
 
1. Better commenting in function
2. Can be better at catching errors
3. try-except overuse? better to let it fail in try-except than if statement? (see addTask filename sanitation before try-except)
4. Wrapping return data
5. Good program argument parsing
6. Testing framework
7. Less complex function, distribute tasks to small function
8. Minor issues and improvements
9. Documentation
10. Git structure
 
1. Overall I think the commenting of the code has improved a lot, mostly due to the function comments which shows up (at least in Visual Studio Code) when you hover the function. I found it is also a good way give more information about arguments that may not show up otherwise. I will continue to use this and improve on the information given, so the comments will be more useful.
2. During this project I put more effort into limiting the error that a user may inflict though standard usage and also file tampering or even corruption of the file. This has been a mixed bag, as sometime I see a sea of if-statements wondering if it is too much. Could be streamlined or defer error catching. This should improve as I delegate tasks to other, smaller methods.
3. This point is similar to the one above, but with try-except.
4. Sometime through the project I realized the tests and some methods could benefit from an object-like response, which could include a function result (Finished as expected: True/False), a message in case of errors (simple string, instead of printing from the place the function failed), and some sort of payload which is some altered information that is the actual return value. I'm not sure how this would fit in with less centralized structure from points 2 and 7.
5. Comparing the user input parsing I feel I have improved somewhat from previous projects. Still room for improvement, but not entirely sure whether it's better to cast before function call or make all methods accept strings as arguments and then cast them.
6. For this project I have not used a testing framework, rather I have made methods that returns 0 for success and 1 for fail, adding the result of all tests and displaying an success/fail for each function and one for all the tests. As one can see from the code, adding all that manually takes time and care one could do without.
7. The biggest regret I have from this project is that I fell into the trap of making a few, complex functions. A lot of the function in [todo.py](todo.py) should be split up into smaller methods, which makes the code more modular, more reusable, easier to test, and overall less complex. The reasons why I did no do this is mainly due to a lack of testing framework, as I would have to add all the tests manually to the main test function. I also did not like the idea of expanding the number of functions in the project as I already had extended the scope more than expected.
8. When doing the project I came up with more improvements as I went along, as I did not pre-plan or structure the project. For such a small project I don't see any problems with this, but the natural result is that the scope grows a little every day. I could go on and make the ultimate todo program, but by now it's a reasonable size. There are minor improvements I have written down in the TODO section, which I may or may not do sometime in the future.
9. I should work on my documentation, cite more reasons and patterns from the code. Even some simple visual models or more detailed examples could be useful for people with problems that are not addressed by the Help section. Easy to do later.
10. I intentionally did not try to emulate a more realistic git version as the focus was on the code.
 
### TODO:
 
- when setting up on a new computer, default tasklist may not be initialized. Empty print spam, check for tasklist name in all-task-list and default name set (setlist "default" fixed it)
- "Fatal Python error: Cannot recover from stack overflow." + spam on change to default list (might be related to set up on new computer)
- when printing all lists, add check (0/1 similar to task) to check if all tasks in list are completed
- delete all
- delete all checked tasks
- uncheck all
- rename formatPrintList to formatTasksPrint?
- formatPrintList when empty should return an array of one line: ["The current list (listname) is empty."] or object
- float reset interval