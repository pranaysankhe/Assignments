import tkinter as tk
from tkinter import ttk

def show_description():
    selected_column = column_var.get()
    description = data_dictionary.get(selected_column, "Description not found.")
    description_text.config(state=tk.NORMAL)
    description_text.delete(1.0, tk.END)
    description_text.insert(tk.END, description)
    description_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Data Dictionary")

# Data Dictionary
data_dictionary = {
    "student_id": "Unique identifier for each student.",
    "first_name": "Student's first name.",
    "last_name": "Student's last name.",
    "date_of_birth": "Student's date of birth (YYYY-MM-DD).",
    "major": "Student's primary field of study.",
    "gpa": "Student's Grade Point Average.",
    "email": "Student's email address."
}

# UI Elements
# Dropdown for column selection
column_var = tk.StringVar()
column_dropdown = ttk.Combobox(root, textvariable=column_var)
column_dropdown['values'] = list(data_dictionary.keys())
column_dropdown.grid(row=0, column=0, padx=10, pady=10)
column_dropdown.set("Select a column")

# Button to show description
show_button = tk.Button(root, text="Show Description", command=show_description)
show_button.grid(row=0, column=1, padx=10, pady=10)

# Text area for description
description_text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
description_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
description_text.config(state=tk.DISABLED)

# Start the main loop
root.mainloop()
