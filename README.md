#This system is a Python-based desktop application developed using the Tkinter library for the graphical user interface (GUI) and mysql-connector-python to interact with a MySQL database. It serves as a phase in the Customer Management Application that allows users to retrieve and search customer records from the customer table of the Sakila database.

Key Features:

	1.	View All Customer Records:
	•	The system can fetch and display all customer records from the customer table in the database.
	•	Customers’ first name, last name, and email are shown in a structured table (using Treeview).
	•	Users can view the complete list of customers by clicking the “View all customers” button.
	2.	Search Functionality:
	•	The application provides an interface to search for customers by their first name and last name.
	•	Users can enter search terms into input fields for both first and last names. The system queries the database for matching records after clicking the “Click to Search” button.
	•	Search results are limited to 10 records and displayed in a separate Treeview widget.
	•	The system uses SQL’s LIKE operator to perform a partial match search, allowing users to search by a portion of the names.
	3.	Clear Search Results:
	•	After a search, users can clear the search results by clicking the “Clear” button. This also resets the input fields for new searches.

Architecture Overview:

	•	Database Interaction:
	•	The system connects to a MySQL database hosted at 141.209.241.57 using credentials provided in the connection function (DBCONNECT). The application interacts with the Sakila database, specifically the customer table, to retrieve customer details.
	•	Queries include fetching all customer records and searching for customers by first and last names with LIKE filters.
	•	User Interface:
	•	The GUI is divided into two sections using LabelFrame widgets:
	1.	Customer Records Section: Displays all customer records when a user clicks “View all customers”.
	2.	Search Records Section: Contains input fields for the first name and last name, along with search and clear buttons, and displays search results in a table.
	•	The Treeview widget displays both full customer records and search results in tabular format, with columns for First Name, Last Name, and Email.

Key Functions:

	1.	DBCONNECT():
	•	Establishes a connection to the MySQL database. If the connection fails, an error message is displayed using messagebox.showerror(). ** NB you will need to have MySQL running. **
	2.	customer_detals():
	•	Fetches all customer records from the database and inserts them into the Treeview for display in the Customer Records section.
	3.	customer_search():
	•	Takes user input for first and last names, performs a search in the customer table using a SQL query with LIKE filters, and displays matching results in the Treeview.
	4.	clear():
	•	Clears the search results and resets the input fields to allow for new searches.

User Interaction Flow:

	1.	View All Customers:
	•	The user clicks the “View all customers” button to load and view the complete list of customers.
	2.	Search for Customers:
	•	The user inputs the first name and/or last name into the search fields and clicks “Click to Search”.
	•	The system retrieves and displays the matching records in the search results table.
	3.	Clear Search Results:
	•	The user can click the “Clear” button to clear search results and reset the input fields for new searches.

Conclusion:

This application can be a function in a management tool for interacting with data, allowing users to view all records and search for specific records by name or letter word.
