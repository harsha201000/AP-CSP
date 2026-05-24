# Import Required Libraries
from tkinter import *
from tkinter import messagebox

# A list to store history of calculations to manage complexity by combining past information
calc_history = []

# A function to evaluate a mathematical expression and to update history
def process_calc(exp):
    # Sequencing, Selection, Iteration
    global calc_history
    # Start processing logic - sequencing
    try:
        # check if expression is empty before evaluating - selection
        if not exp:
            return "Empty"
        
        # Replace percentage sign with division for calculation
        if '%' in exp:
            exp = exp.replace('%', '/100')
        
        # Built in evaluation handles the math; result is stored
        res = str(eval(exp))
        full_record = f"{exp} = {res}"

        # manage complexity by searching through history to ensure that there are no duplicate entries stored - iteration
        is_duplicate = False
        for entry in calc_history:
            if entry == full_record:
                is_duplicate = True
                break

        if not is_duplicate:
            calc_history.append(full_record)

        return res
    
    except ZeroDivisionError as e:
        return "Zero Division Error"
    except Exception:
        return "Syntax Error"
    
# GUI Application Window Setup using Tk
app = Tk()
app.title("Calculator")
app.config(bg="#202020")

app.iconbitmap("calc.ico") # Calc Window Icon Bitmap

display = Entry(app, font=("Arial", 25), fg="white", bg="black", borderwidth=5, relief="flat", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button Click Functions
def button_click(char):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(char))

def clear_screen():
    # AC: Clear all text
    display.delete(0, END)

def backspace():
    # Delete one: remove last character
    current = display.get()
    if len(current) > 0:
        display.delete(len(current) - 1, END)

def calculate():
    # Procedure Call: Executes logic
    current_val = display.get()
    res = process_calc(current_val)
    # Update GUI based on procedure result - Output
    display.delete(0, END)
    display.insert(0, res)

def show_history():
    # Demonstrates list usage in output
    history_str = "\n".join(calc_history) if calc_history else "No History"
    messagebox.showinfo("Calculation History", history_str)

def negate_number():
    current = display.get()
    if current and current != "0":
        if current.startswith('-'):
            display.delete(0)
        else:
            display.insert(0, '-')

# UI Buttons
buttons = [
    ('AC', 1, 0), ('(', 1, 1), (')', 1, 2), ('%', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+/-', 5, 2), ('+', 5, 3), 
    ('=', 6, 0), ('Del', 6, 2)
]

# Create and place buttons
for (text, row, col) in buttons:
    cmd = lambda x=text: button_click(x)
    
    # Commands for special buttons
    if text == '=':
        cmd = calculate
    elif text == 'AC':
        cmd = clear_screen
    elif text == 'Del':
        cmd = backspace
    elif text == '+/-':
        cmd = negate_number
        
    button = Button(app, text=text, font=("Arial", 15), fg="white", bg="#333333", command=cmd, relief="flat", padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew")
    
    # Span equals buttons
    if text == '=':
        button.grid(columnspan=2, column=0)
    if text == 'Del':
        button.grid(columnspan=2, column=2)

# Configure Grid
for i in range(7):
    app.rowconfigure(i, weight=1)
for i in range(4):
    app.columnconfigure(i, weight=4)

# Extra Feature to fullfill program complexity management
view_history_button = Button(app, text="View History", fg="white", bg="gray", command=show_history)
view_history_button.grid(row=7, column=0, columnspan=4, sticky="nsew")

app.mainloop()
