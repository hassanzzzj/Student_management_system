# 🎓 University Management System

This is a desktop application developed using Python's **Tkinter** for the Graphical User Interface (GUI) and **MySQL** (via `pymysql`) for database management. The system allows authorized users to manage student records efficiently, including adding, searching, deleting, updating, viewing, and exporting student data.

## ✨ Features

This system provides a comprehensive set of features for managing student data:

* **Database Connectivity:** Connects to a MySQL database where all student records are stored. It can automatically create the necessary database (`University_management_system1`) and table (`student_data1`) if they don't exist.
* **Add Student (Create):** Allows the entry of new student details (ID, Name, Mobile, Email, Address, Gender, DOB) into the database, along with automatic recording of the date and time of entry.
* **Search Student (Read):** Users can search for students based on multiple criteria: ID, Name, Mobile, Email, DOB, Gender, Address, or Added Date.
* **Delete Student (Delete):** Allows deletion of a student record by selecting an entry from the displayed table.
* **Update Student (Update):** Allows modification of existing student details after selecting a record from the table.
* **Show All:** Displays all student records currently in the database table.
* **Export Data:** Exports all displayed student data into a CSV file using the **pandas** library.
* **Dynamic UI:** Includes an introductory sliding text and a real-time clock.

---

## 🛠️ Prerequisites

Before running the application, you need to have the following installed:

1.  **Python 3.x:** The core programming language.
2.  **MySQL Server:** The database where the student data will be stored.
3.  **Required Python Libraries:** You will need to install `tkinter` (usually built-in), `pymysql`, and `pandas`.

You can install the Python libraries using `pip`:

```bash
pip install pymysql pandas

🚀 Getting Started
Follow these steps to set up and run the project locally.
1. Database Setup
Ensure your MySQL server is running. You will need the Host, User, and Password credentials to connect the application to the database.
2. Run the Application
Execute the Python script to start the GUI:
python your_script_name.py  # Replace with the actual filename

3. Connect to Database
 * When the application launches, click the 'Connect to Database' button at the top right.
 * A new window will appear asking for your MySQL credentials.
 * Enter the Host (e.g., localhost), User (e.g., root), and Password for your MySQL server.
 * Click 'Log In'.
   * If successful, the system will either create the database/table or connect to the existing one, and you will see a success notification.
   * If connection fails, check your credentials and ensure the MySQL server is running.
🖥️ Usage
Once connected, you can use the buttons on the left panel (Data Entry Frame) to manage student records:
| Button | Functionality |
|---|---|
| 1. Add Student | Opens a new window to enter and save new student details. |
| 2. Search Student | Opens a new window where you can input criteria (ID, Name, etc.) to filter the displayed records. |
| 3. Delete Student | Deletes the student record currently selected in the main table. |
| 4. Update Student | Opens a new window pre-filled with the selected student's data for modification. |
| 5. Show All | Fetches and displays all records from the database in the main table. |
| 6. Export Data | Saves the currently displayed data in the table to a CSV file. |
| 7. Exit | Closes the application. |
🖼️ User Interface Overview
The application is divided into three main sections:
 * Top Bar: Contains the Real-time Clock, Introductory Slider Text, and the Connect to Database button.
 * Data Entry Frame (Left): Houses all the main functionality buttons (Add, Search, Delete, Update, Show All, Export, Exit).
 * Data View Frame (Right): A Treeview widget that displays student records retrieved from the database.
📄 Database Schema
The student_data1 table structure is as follows:
| Column Name | Data Type | Constraint | Description |
|---|---|---|---|
| id | INT | Primary Key, Not Null | Unique Student Identifier. |
| name | VARCHAR(20) |  | Student's Name. |
| mobile | VARCHAR(20) |  | Student's Mobile Number. |
| email | VARCHAR(30) |  | Student's Email Address. |
| address | VARCHAR(100) |  | Student's Address. |
| gender | VARCHAR(50) |  | Student's Gender. |
| dob | VARCHAR(50) |  | Student's Date of Birth. |
| date | VARCHAR(50) |  | Date the record was added. |
| time | VARCHAR(50) |  | Time the record was added. |

