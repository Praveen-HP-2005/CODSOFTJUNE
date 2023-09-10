import customtkinter as ctk

task_widgets = {}

def add_todo():
    todo = entry.get()
    if todo:
        task_text.configure(state="normal")  # Enable editing
        task_text.insert("end", "\u2713 " + todo + "\n")  # Add a checkmark (tick) to the text
        task_text.configure(state="disabled")  # Disable editing
        entry.delete(0, ctk.END)

def delete_selected_task():
    selected_indices = task_text.tag_ranges("sel")
    if selected_indices:
        task_text.configure(state="normal")  # Enable editing
        task_text.delete(selected_indices[0], selected_indices[1])  # Delete selected text
        task_text.configure(state="disabled")  # Disable editing

def add_todo_on_enter(event):
    if event.keysym == 'Return':
        add_todo()

root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")
entry.bind("<Return>", add_todo_on_enter)

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=10)

# Create a Delete button outside the scrollable frame
delete_button = ctk.CTkButton(root, text="Delete", width=500, command=delete_selected_task)
delete_button.pack(pady=10)

# Create a CTkText widget for displaying tasks
task_text = ctk.CTkTextbox(scrollable_frame, wrap="none", state="disabled", width=40, height=10)
task_text.pack(fill="both", expand=True)

root.mainloop()






