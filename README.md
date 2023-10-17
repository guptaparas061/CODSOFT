# To-Do List Application

[![powered by](https://img.shields.io/badge/Powered%20by-Python%203-blue)](https://www.python.org/)
[![powered by](https://img.shields.io/badge/Powered%20by-Tkinter-red)](https://docs.python.org/3/library/tkinter.html)

## Overview
This is a simple To-Do List application built in Python. It allows users to manage and organize their tasks efficiently through a graphical user interface (GUI) created using the Tkinter library.

## Technologies Used
- **Python:** The core programming language used to develop the application.
- **Tkinter:** A standard Python interface to the Tk GUI toolkit. It provides the elements (like buttons, labels, and entry fields) required to build the GUI.
- **JSON:** Used for persistent storage of tasks. Tasks are stored in a JSON file ([tasks.json](tasks.json)) which allows for data retrieval between sessions.

## How It Works
**1.  Launching the Application**
- Run the Python script **([todolist.py](todolist.py))**.
- The main window of the application will appear.

**2.  Adding a Task**
- Type the task name in the provided input field.
- Click the "Add Task" button.
- The task will be added to the list.

**3.  Marking a Task as Complete**
- Select a task from the list.
- Click the "Mark as Complete" button.
- The selected task will be marked as complete.

**4.  Deleting a Task**
- Select a task from the list.
- Click the "Delete Task" button.
- The selected task will be removed from the list.

**5.  Saving and Loading Tasks**
- Tasks are stored in a JSON file ([tasks.json](tasks.json)) in the same directory as the script. This allows tasks to persist between sessions.

**6.  Exiting the Application**
- Click the close button on the application window.

## How to Use
**1.  Clone the Repository**
- Clone this repository to your local machine.

**2.  Install Dependencies**
- Ensure you have Python installed on your machine.
- No additional packages are required as Tkinter is a standard library in Python.

**3.  Run the Application**
- Execute the Python script **[todolist.py](todolist.py)** to launch the application.

**4.  Interact with the GUI**
- Follow the instructions provided in the "[How It Works](https://github.com/guptaparas061/CODSOFT/edit/main/README.md#how-it-works)" section above to add, complete, and delete tasks.

**5.  Closing the Application**
- Simply close the application window to exit.

## Screenshot
![To-Do List](https://github.com/guptaparas061/CODSOFT/blob/main/imgs/todolist.png)

## Future Enhancements
- Implement additional features such as task prioritization, due dates, and categories.
- Add user authentication and the ability to have multiple user accounts.
- Improve the UI/UX with more advanced GUI components and styles. <br>

# GUI Calculator Application

[![powered by](https://img.shields.io/badge/Powered%20by-Python%203-blue)](https://www.python.org/)
[![powered by](https://img.shields.io/badge/Powered%20by-Tkinter-red)](https://docs.python.org/3/library/tkinter.html)

## Technologies Used
- **Python:** The entire application is written in Python, a versatile programming language known for its simplicity and readability.
- **Tkinter:** Tkinter is the standard GUI library for Python. It provides tools for creating graphical user interfaces.

## Description
This project is a simple GUI-based calculator application built using Python and Tkinter. It provides a visually appealing interface with buttons for each digit and basic arithmetic operations (addition, subtraction, multiplication, division).

## Features
- User-Friendly Interface: The calculator has a clean and intuitive graphical interface that allows users to input numbers and perform calculations with ease.
- Basic Arithmetic Operations: The calculator supports addition, subtraction, multiplication, and division of numbers.
- Error Handling: The application is equipped to handle errors such as division by zero or invalid expressions.
- Clear Function: There is a 'C' button to clear the display, making it convenient for users to start a new calculation.

## How to Use
**1.  Launching the Application**
- Run the Python script **[calculator.py](calculator.py)**.

**2.  Performing Calculations**
- Use the buttons to input numbers and select operations.
- Click the **'='** button to get the result.

**3.  Clearing Display**
- Click the **'C'** button to clear the display.

## Usage Example
1. Input: **'5 + 3 ='** <br>
Output: **'8'**

2. Input: **'10 / 0 ='** <br>
Output: **'Error'**

## Snapshot
<img src="https://github.com/guptaparas061/CODSOFT/blob/main/imgs/calculator.gif" width="300">

## Development
If you'd like to contribute or modify this project, feel free to fork the repository and submit a pull request.

# Password Generator Application

[![powered by](https://img.shields.io/badge/Powered%20by-Python%203-blue)](https://www.python.org/)

## Overview
This Python application generates strong and random passwords based on user-defined parameters such as length and complexity. It provides a user-friendly interface for creating secure passwords for various online accounts.

## Technologies Used
- **Python:** The core programming language used to build the application.
- **Random Module:** Used to generate random characters for the password.
- **String Module:** Utilized for accessing different sets of characters (e.g., letters, digits, punctuation) to construct passwords.

## How it Works
**1.  User Input**
- The application prompts the user to specify the desired length and complexity of the password.

**2.  Generate Password**
- Depending on the user's specified complexity level, the application selects an appropriate set of characters (e.g., lowercase letters, digits, punctuation) to use in generating the password.

**3.  Creating the Password**
- The application uses a combination of random characters from the selected character set to generate a password of the specified length.

**4.  Display the Password**
- The generated password is then displayed on the screen for the user to use.

## Complexity Levels
**1.  Low Complexity**
- Uses lowercase letters and digits.

**2.  Medium Complexity**
- Includes lowercase letters, digits, and punctuation.

**3.  High Complexity**
- Utilizes lowercase letters, uppercase letters, digits, and punctuation.

## How to Use
1. Run the **[passwordgenerator.py](passwordgenerator.py)** script using Python.
2. Follow the prompts to specify the desired length and complexity of the password.
3. The generated password will be displayed on the screen.

## Example Usage
```mathematica
Welcome to the Password Generator!

Enter the desired length of the password: 12
Enter the complexity (low, medium, high): medium

Generated Password: Xy7b$Zp!3v@
```

## Contributing
If you'd like to contribute to this project, please follow these steps:<br>
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

# Contact Book Application

[![powered by](https://img.shields.io/badge/Powered%20by-Python%203-blue)](https://www.python.org/)

## Overview
The Contact Book Application is a Python-based console program that allows users to manage their contacts efficiently. It provides features for adding, viewing, searching, updating, and deleting contacts.

## Technologies Used
This application is built using the following technologies:<br>
- **Python:** The core programming language used for development.
- **Object-Oriented Programming (OOP):** Utilized for structuring the code using classes and objects.
- **Console Interface:** The application operates through a console-based interface for user interaction.

## Working of the Application
The Contact Book Application offers the following functionalities:<br>
1. **Add Contact:** Users can add a new contact with details such as name, phone number, email, and address.
2. **View Contacts:** Displays a list of all saved contacts along with their names and phone numbers.
3. **Search Contact:** Allows users to search for contacts by name or phone number, and displays matching results.
4. **Update Contact:** Enables users to update contact details, including name, phone number, email, and address.
5. **Delete Contact:** Provides an option to delete a contact from the contact list.

The application maintains a list of **'Contact'** objects within a **'ContactBook'**. Each Contact has attributes for name, phone number, email, and address.

## How To Use
**1. Clone the repository**
```bash
git clone https://github.com/guptaparas061/CODSOFT.git
cd contactbook
```

**2. Run the application**
```
python contactbook.py
```

**3. Interact with the application**
- The application will display a menu with options numbered from 1 to 6.
- Enter the number corresponding to the action you want to perform.

**Example Usage**<br><br>
**3.1. Adding a Contact**
```mathematica
Enter your choice: 1
Enter name: John Doe
Enter phone number: 123-456-7890
Enter email: john.doe@example.com
Enter address: 123 Main St, Cityville
```

**3.2. Viewing Contacts**
```yaml
Enter your choice: 2
Name: John Doe, Phone: 123-456-7890
```

**3.3. Searching for a contact**
```yaml
Enter your choice: 3
Enter name or phone number to search: Doe
Name: John Doe, Phone: 123-456-7890
```

**3.4. Updating a contact**
```mathematica
Enter your choice: 4
Enter the name of the contact to update: John Doe
Enter new name: John Doe Jr.
Enter new phone number: 987-654-3210
Enter new email: john.jr@example.com
Enter new address: 456 Oak St, Townsville
```

**3.5. Deleting a contact**
```mathematica
Enter your choice: 5
Enter the name of the contact to delete: John Doe Jr.
```

## Future Enhancements
While the current version of the application provides a basic functionality for managing contacts, there are several potential enhancements that can be considered for future development:<br>
1. **Data Persistence:** Implement a mechanism to store contacts persistently, such as using a database or file storage, allowing users to access their contacts across sessions.
2. **Graphical User Interface (GUI):** Create a user-friendly graphical interface for a more intuitive user experience.
3. **Data Validation and Error Handling:** Incorporate robust input validation and error handling mechanisms to enhance the reliability of the application.
4. **Contact Categories or Groups:** Allow users to categorize contacts into groups or categories for better organization.
5. **Import/Export Contacts:** Add features to import contacts from external sources (e.g., CSV files) and export contacts to various formats.
6. **Additional Contact Information:** Extend the Contact class to include more details like birthdate, organization, etc.
7. **User Authentication:** Implement user authentication for secure access and management of contacts.

## Contributing
If you'd like to contribute to this project, please follow these steps:<br>
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes with clear commit messages.
5. Create a pull request to submit your changes.
