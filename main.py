# import customtkinter as ctk
#
# task_widgets = {}
#
# def add_todo():
#     todo = entry.get()
#     if todo:
#         label = ctk.CTkLabel(scrollable_frame, text=todo)
#         label.pack()
#         delete_button = ctk.CTkButton(scrollable_frame, text="Delete", command=lambda label=label: delete_todo(label))
#         delete_button.pack()
#         task_widgets[label] = delete_button
#         entry.delete(0, ctk.END)
#
# def delete_todo(label_to_delete):
#     delete_button = task_widgets.get(label_to_delete)
#     if delete_button:
#         delete_button.destroy()
#         label_to_delete.destroy()
#         del task_widgets[label_to_delete]
#
# def add_todo_on_enter(event):
#     if event.keysym == 'Return':
#         add_todo()
#
# root = ctk.CTk()
# root.geometry("750x450")
# root.title("Todo App")
#
# title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
# title_label.pack(padx=10, pady=(40, 20))
#
# scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
# scrollable_frame.pack()
#
# entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
# entry.pack(fill="x")
# entry.bind("<Return>", add_todo_on_enter)
#
# add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
# add_button.pack(pady=20)
#
# root.mainloop()

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






