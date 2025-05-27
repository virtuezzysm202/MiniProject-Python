import tkinter as tk
from tkinter import ttk
import math

class Calculator: 
    def __init__(self, root): 
        self.root = root
        self.root.title("Calculator with History")
        self.root.geometry("350x550")
        self.expression = "" #+, -, *, /
        self.history = []

        self.create_widgets()

    def create_widgets(self): 
        # Display
        self.display_var = tk.StringVar()
        self.display_entry = ttk.Entry(self.root, textvariable=self.display_var, font=("Arial", 24), justify="right")
        self.display_entry.pack(fill="x", padx=10, pady=10)

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '√', '=', '+'),
            ('C', 'Clear History')
        ]

        for row in buttons:
            row_frame = ttk.Frame(btn_frame)
            row_frame.pack(fill="x", pady=2)
            for btn_text in row:
                ttk.Button(
                    row_frame, text=btn_text, width=12 if btn_text == 'Clear History' else 6,
                    command=lambda t=btn_text: self.on_button_click(t)  #Button click
                ).pack(side="left", padx=5)

        # History Text Box
        self.history_box = tk.Text(self.root, height=8, state="disabled", font=("Arial", 10))
        self.history_box.pack(fill="both", padx=10, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "Clear History":
            self.history.clear()
            self.update_history()
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.update_history()
                self.expression = result
            except Exception as e:
                self.expression = "Error"
        elif char == "√":
            try:
                value = eval(self.expression)
                if value < 0:
                    self.expression = "Error"
                else:
                    result = str(math.sqrt(value))
                    self.history.append(f"√({self.expression}) = {result}")
                    self.update_history()
                    self.expression = result
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.display_var.set(self.expression)

    def update_history(self):
        self.history_box.config(state="normal")
        self.history_box.delete(1.0, tk.END)
        for entry in self.history[-10:]:  # Show last 10 entries
            self.history_box.insert(tk.END, entry + "\n")
        self.history_box.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
