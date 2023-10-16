# CODSOFT

## To-Do List Application

### Overview
This is a simple To-Do List application built in Python. It allows users to manage and organize their tasks efficiently through a graphical user interface (GUI) created using the Tkinter library.

### Technologies Used
- **Python:** The core programming language used to develop the application.
- **Tkinter:** A standard Python interface to the Tk GUI toolkit. It provides the elements (like buttons, labels, and entry fields) required to build the GUI.
- **JSON:** Used for persistent storage of tasks. Tasks are stored in a JSON file ([tasks.json](tasks.json)) which allows for data retrieval between sessions.

### How It Works
**1. Launching the Application:**
- Run the Python script ([todolist.py](todolist.py)).
- The main window of the application will appear.

**2. Adding a Task:**
- Type the task name in the provided input field.
- Click the "Add Task" button.
- The task will be added to the list.

**3. Marking a Task as Complete:**
- Select a task from the list.
- Click the "Mark as Complete" button.
- The selected task will be marked as complete.

**4. Deleting a Task:**
- Select a task from the list.
- Click the "Delete Task" button.
- The selected task will be removed from the list.

**5. Saving and Loading Tasks:**
- Tasks are stored in a JSON file ([tasks.json](tasks.json)) in the same directory as the script. This allows tasks to persist between sessions.

**6. Exiting the Application:**
- Click the close button on the application window.

### How to Use
**1. Clone the Repository:**
- Clone this repository to your local machine.

**2. Install Dependencies:**
- Ensure you have Python installed on your machine.
- No additional packages are required as Tkinter is a standard library in Python.

**3. Run the Application:**
- Execute the Python script [todolist.py](todolist.py) to launch the application.

**4. Interact with the GUI:**
- Follow the instructions provided in the "How It Works" section above to add, complete, and delete tasks.

**5. Closing the Application:**
- Simply close the application window to exit.

### Future Enhancements
- Implement additional features such as task prioritization, due dates, and categories.
- Add user authentication and the ability to have multiple user accounts.
- Improve the UI/UX with more advanced GUI components and styles.
