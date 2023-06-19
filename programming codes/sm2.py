import tkinter as tk

def calculate_sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text="Sum: {}".format(result))

root = tk.Tk()
root.title("Sum Calculator")

# Create input labels and entry fields
label1 = tk.Label(root, text="Number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create button to calculate the sum
calculate_button = tk.Button(root, text="Calculate", command=calculate_sum)
calculate_button.pack()

# Create label to display the result
result_label = tk.Label(root, text="Sum: ")
result_label.pack()

root.mainloop()