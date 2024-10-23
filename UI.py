
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Create an entry field for entering tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=35, height=10)
task_listbox.pack(pady=10)

# Define button action functions
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of the selected task
        task_listbox.delete(selected_task_index)  # Remove the task from the listbox
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def exit_app():
    root.quit()

# Create buttons for adding, deleting tasks, and exiting the app
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
