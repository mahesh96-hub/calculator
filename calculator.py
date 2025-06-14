import tkinter as tk
from tkinter import messagebox

# ---------------------- Calculator ----------------------
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid Expression")

def clear_entry():
    entry.delete(0, tk.END)

def append_character(character):
    entry.insert(tk.END, character)

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)  # Clear button
]
for (text, row, col) in buttons:
    if text == '=':
        action = evaluate_expression
    elif text == 'C':
        action = clear_entry
    else:
        action = lambda x=text: append_character(x)
    tk.Button(root, text=text, command=action, font=("Arial", 18), width=5).grid(row=row, column=col)

root.mainloop()
