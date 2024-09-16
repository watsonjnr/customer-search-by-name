import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# function to handle MYSQL connection
def DBCONNECT():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mypass",
            database="database"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database connection error", f"Error connecting to DB: {err}")
        return None

def customer_detals():
    conn = DBCONNECT()
    if conn:
        cursor=conn.cursor()
        cursor.execute("SELECT first_name,last_name,email FROM customer")
        results=cursor.fetchall()

        for result in results:
            tree.insert("",tk.END,values=result)
        conn.close()

#funtion to hold the search process
def customer_search():
    search_term1=search_var1.get()
    search_term2=search_var2.get()
    conn=DBCONNECT()
    if conn:
        cursor=conn.cursor()
        sql="""
        SELECT first_name,last_name,email 
        FROM customer 
        WHERE first_name LIKE %s AND last_name LIKE %s 
        LIMIT 10 
        """
        cursor.execute(sql,(f'%{search_term1}%',f'%{search_term2}%'))
        results=cursor.fetchall()

        for item in tree2.get_children():
            tree2.delete(item)

        for result in results:
            tree2.insert("",tk.END,values=result)

        conn.close()

def clear():

    for item in tree2.get_children():
        tree2.delete(item)

    for item2 in search_entry1:
        search_entry1.delete(item2)

    for item in search_entry2:
        search_entry2.delete(item)

#creating the main shell
root=tk.Tk()
root.title("Shehu1i Customer Application")
root.geometry("800x800")

#Frame for Customer rec.
frame1=tk.LabelFrame(root, text="Customer Records")
frame1.pack()

frame2=tk.LabelFrame(root, text="Search Records")
frame2.pack()

record_button=tk.Button(frame1,text="View all customers", command=customer_detals)
record_button.pack()

#customer records tree view
columns=("first_name","last_name","email")
tree=ttk.Treeview(frame1, columns=columns,show="headings")
tree.heading("first_name", text="First Name")
tree.heading("last_name", text="Last Name")
tree.heading("email", text="Email")
tree.pack(pady=20, fill="both", expand=True)

#searching customer by name
#Entry fields
search_var1=tk.StringVar()
search_var2=tk.StringVar()

search_lable=tk.Label(frame2, text="First Name:")
search_lable.pack()

search_entry1=tk.Entry(frame2, textvariable=search_var1)
search_entry1.pack()

search_lable=tk.Label(frame2, text="Last Name:")
search_lable.pack()

search_entry2=tk.Entry(frame2, textvariable=search_var2)
search_entry2.pack()



#buttons
search_button=tk.Button(frame2, text="Click to Search" ,command=customer_search)
search_button.pack()
clear_button=tk.Button(frame2,text="Clear", fg="red", command=clear)
clear_button.pack()


#search record tree view area
columns=("first_name","last_name","email")
tree2=ttk.Treeview(frame2, columns=columns,show="headings")
tree2.heading("first_name", text="First Name")
tree2.heading("last_name", text="Last Name")
tree2.heading("email", text="Email")
tree2.pack(pady=20, fill="both", expand=True)



root.mainloop()
