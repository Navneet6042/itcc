from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display the result
        self.result_display = Entry(master, width=20, justify='right', font=('Arial', 16))
        self.result_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons for calculator operations
        button_list = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "C", "/"
        ]
        row, col = 1, 0
        for label in button_list:
            self.create_button(label, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # create equal button
        equal_button = Button(master, text="=", width=20, height=2, command=self.calculate)
        equal_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def create_button(self, label, row, col):
        button = Button(self.master, text=label, width=5, height=2, command=lambda: self.button_click(label))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, label):
        if label == "C":
            self.result_display.delete(0, END)
        else:
            self.result_display.insert(END, label)

    def calculate(self):
        try:
            result = eval(self.result_display.get())
            self.result_display.delete(0, END)
            self.result_display.insert(END, result)
        except:
            self.result_display.delete(0, END)
            self.result_display.insert(END, "Error")


root = Tk()
calculator = Calculator(root)
root.mainloop()
