Study Planner and Performance Analyzer
Overview
The Study Planner and Performance Analyzer is a Python-based application designed to help students organize their study tasks and analyze their academic performance through a simple Command Line Interface (CLI).
It allows users to:
View their current study tasks.
Add new study tasks with subject and study duration.
Remove completed or unwanted tasks.
Record marks obtained in subjects.
Calculate average marks and analyze overall performance.
The system uses Python lists and basic programming concepts to temporarily store study and performance information during the runtime of the program.
Features
View Study Tasks
Displays a numbered list of all planned study tasks along with their subject and duration. If the study plan is empty, it notifies the user.
Add Study Task
Allows users to enter a subject, topic, and planned study duration. It includes validation to ensure that empty task details are not added.
Remove Study Task
Allows users to remove a study task using its specific number. It checks whether the list is empty and validates the entered task number.
Performance Analysis
Allows users to enter marks obtained in different subjects. The system calculates the average marks and provides a simple performance analysis.
User Interface
Provides a clean and repetitive menu to guide users through different options until they choose to exit.
Technologies/Tools Used
Python 3.x
Programming language used to develop the application and implement its logic.
Python Lists
Used as the primary data structure to store study tasks and performance information dynamically in memory.
Functions
Used to divide the program into smaller and reusable sections such as adding tasks, viewing tasks, removing tasks, and analyzing performance.
Input/Output Operations
Standard Python `input()` and `print()` functions are used for interaction with the user.
Conditional Statements and Loops
Used to control the program flow, validate user input, display menus, and perform calculations.
Steps to Install & Run the Project
Install Python
Ensure that Python 3.x is installed on your computer.
Download the Project
Download or clone the project files and save them in a suitable folder.
Save the Code
Save the Python source code in a file named:
`study_planner.py`
Run the Program
Open the terminal or command prompt, navigate to the folder containing the Python file, and run:
```bash
python study_planner.py
```
Instructions for Testing
Viewing Study Tasks
Run the program and choose the option for viewing study tasks.
Expected Output:
If tasks exist, they will be displayed with their subject, topic, and duration.
If no tasks exist, the program will display:
`No study tasks available.`
Adding a Study Task
Choose the option for adding a study task.
Enter the subject, topic, and planned study duration when prompted.
Expected Output:
`Study task added successfully.`
The task can then be viewed using the View Study Tasks option.
Removing a Study Task
Choose the option for removing a study task.
The system will display the current study tasks.
Enter the number corresponding to the task that you want to remove.
Expected Output:
`Study task removed successfully.`
If an invalid number is entered, the program will display an appropriate error message.
Analyzing Performance
Choose the performance analysis option.
Enter the marks obtained in the required subjects.
The program calculates the average marks and displays the performance result.
Expected Output:
`Average Marks: [calculated average]`
The program then displays a suitable performance message based on the calculated average.
Exiting the Program
Choose the Exit option.
Expected Output:
`Thank you for using Study Planner and Performance Analyzer.`
The program will then terminate.
