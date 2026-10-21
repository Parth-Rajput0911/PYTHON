# Simple calculator using Tkinter

import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x300")

# Heading
heading = tk.Label(
    root,
    text="Simple Calculator",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame, text="+",
    command=lambda: calculate("+"), width=5
).grid(row=0, column=0, padx=3)

tk.Button(
    button_frame, text="-",
    command=lambda: calculate("-"), width=5
).grid(row=0, column=1, padx=3)

tk.Button(
    button_frame, text="*",
    command=lambda: calculate("*"), width=5
).grid(row=0, column=2, padx=3)

tk.Button(
    button_frame, text="/",
    command=lambda: calculate("/"), width=5
).grid(row=0, column=3, padx=3)

# Display result
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 12)
)
result_label.pack(pady=10)

# Run the application
root.mainloop()