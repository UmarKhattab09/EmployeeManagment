import tkinter as tk
from tkinter import ttk
from Tables.tableslist import Employee, Department
from EmployeeDatabase import DepartmentCRUD
from EmployeeDatabase import CRUD
import mysql.connector


def fetch_data():
    for row in tree.get_children():
        tree.delete(row)

    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="employee_managment"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")  # change to your table
        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

        cursor.close()
        connection.close()
    except Exception as e:
        print("Error fetching data:", e)









def create():
    name = name_entry.get()
    email = email_entry.get()
    dept = dept_entry.get()

    if name and email and dept:
        try:
            creating = CRUD(name, email, dept)
            creating.create()  # Actually call the method
            print(f"User '{name}' created.")
            fetch_data()  # Refresh table after creating
        except Exception as e:
            print("Error creating user:", e)
    else:
        print("Please fill all fields")

def search():
    name = name_entry.get()
    email=email_entry.get()

    for row in tree.get_children():
        tree.delete(row)
    try:
        searching = CRUD()
        users   = searching.search(name,email)
        print("USERS HAVE BEEN SEARCHED")
        if users:
            print("inside first if")
            for user in users:
                print("isndie for")
                tree.insert("",tk.END,values=user)
                # tree.insert("",tk.END,values=(user,))
        else:
            print("No user fund")
    except Exception as e:
        print("ERROR")



def update():
    name = name_entry.get()
    email=email_entry.get()
    department = dept_entry.get()
    for row in tree.get_children():
        tree.delete(row)

    
    print("update functionality is adding")

def delete():
    name = name_entry.get()
    email=email_entry.get()
    for row in tree.get_children():
        tree.delete(row)

    if name and email:
        try:
            deleteing = CRUD()
            deleteing.delete(name=name,email=email)  # Actually call the method
            # print(f"User '{name}' Deleted.")
            fetch_data()  # Refresh table after creating
        except Exception as e:
            print("Error Deletign User", e)
    else:
        print("Please fill all fields")    

    # print("Delete functionality coming soon.")

root = tk.Tk()
root.geometry("800x600")
root.title("Employee Management System")

# Top Frame for Table
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = ("ID", "Name", "Email", "Department_ID")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=150)

tree.pack(fill=tk.BOTH, expand=True)

# Load Data Button
tk.Button(root, text="Load Data", command=fetch_data).pack(pady=10)

# Bottom Frame for Form
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(form_frame, width=20)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Email:").grid(row=0, column=2, padx=5)
email_entry = tk.Entry(form_frame, width=20)
email_entry.grid(row=0, column=3, padx=5)

tk.Label(form_frame, text="Dept ID:").grid(row=0, column=4, padx=5)
dept_entry = tk.Entry(form_frame, width=10)
dept_entry.grid(row=0, column=5, padx=5)

# Button Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Create", command=create).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Search", command=search).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Delete", command=delete).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="Update", command=update).grid(row=0, column=3, padx=10)

root.mainloop()
