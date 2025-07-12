import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x500") 
window.resizable(False, False) 
expression = ""

def click(value):
    global expression
    expression += value
    entry.delete(0, tk.END)
    entry.insert(0,expression)

def calculate():
    global expression
    try:
        result = str(eval(expression)) 
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result  
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

entry = tk.Entry(window, font=("Arial", 24), bd=5, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),("%",5,1),(" ",5,2),(" ",5,3)
]
for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda val=text: click(val)

    tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.mainloop()
