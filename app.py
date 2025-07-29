import tkinter as tk
from main import Employee,CRUD


def create():
    name = name_entry.get()
    email = email_entry.get()
    # session = Session()
    creating = CRUD(name,email)
    user = creating.create


def search():
    pass

def update():
    pass

def delete():
    pass


    
    

root = tk.Tk()
root.geometry("400x200")

# Name Label and Entry
name_label = tk.Label(root, text="Name:")
name_label.place(x=50, y=30)

name_entry = tk.Entry(root, width=30)
name_entry.place(x=50, y=55)

# Email Label and Entry
email_label = tk.Label(root, text="Email:")
email_label.place(x=50, y=90)

email_entry = tk.Entry(root, width=30)
email_entry.place(x=50, y=115)

# Button to get data
submit_button = tk.Button(root, text="Create", command=create)
submit_button.place(x=50, y=150)
submit_button = tk.Button(root, text="Search", command=search)
submit_button.place(x=50, y=200)
submit_button = tk.Button(root, text="Delete", command=delete)
submit_button.place(x=50, y=250)
submit_button = tk.Button(root, text="Update", command=update)
submit_button.place(x=50, y=300)

root.mainloop()
