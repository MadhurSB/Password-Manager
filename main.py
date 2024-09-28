import random
import pandas as pd
import os
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%'
    password = ''.join(random.choice(letters) for _ in range(12))  # Generating a 12-character password
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:
        # Create a dictionary with the data
        data = {'Website': [website], 'Email': [email], 'Password': [password]}
        new_data = pd.DataFrame(data)
        
        # Get the current directory where the script is located
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "passwords.xlsx")

        # Try to read the existing Excel file, or create a new DataFrame if it doesn't exist
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Website', 'Email', 'Password'])  # Create file if not present

        # Append new data to the DataFrame using pd.concat
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(file_path, index=False)  # Save the DataFrame to the Excel file

        # Clear the entry fields
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        print("Please don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")

email_label = Label(text="Email:")
email_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
