import tkinter as tk
from tkinter import messagebox

# List to keep track of open windows
windows = []

def show_checked():
    if var1.get() == 1:
        second_window("Checkbox 1 Window", 1)
    if var2.get() == 1:
        second_window("Checkbox 2 Window", 2)
    if var3.get() == 1:
        second_window("Checkbox 3 Window", 3)

def second_window(title, num):
    second_window = tk.Toplevel(root)
    windows.append(second_window)
    second_window.title(title)

    canvas = tk.Canvas(second_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(second_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    second_frame = tk.Frame(canvas)
    second_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=second_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Variables to store checkbox states for the second window
    second_vars = []
    second_checkboxes = []

    for i in range(1, 7):
        var = tk.IntVar()
        second_vars.append(var)
        chk = tk.Checkbutton(second_frame, text=f"Checkbox {num}.{i}", variable=var)
        chk.grid(row=i-1, column=0, sticky=tk.W)
        second_checkboxes.append(chk)

    def show_checked_second():
        message = ""
        for i, var in enumerate(second_vars):
            if var.get() == 1:
                message += f"Checkbox {num}.{i+1} is checked\n"

        if message == "":
            message = "No checkboxes are checked"

        messagebox.showinfo(f"Checked Boxes - {title}", message)

    def go_back():
        if len(windows) > 1:
            windows[-1].destroy()
            windows.pop()

    def cancel():
        root.quit()

    def go_next():
        if len(windows) < 4:
            second_window(f"Checkbox {len(windows) + 1} Window", len(windows) + 1)

    show_button_second = tk.Button(second_window, text="Show Checked", command=show_checked_second)
    show_button_second.pack(pady=10)

    button_frame = tk.Frame(second_window)
    button_frame.pack(pady=10)

    back_button = tk.Button(button_frame, text="Back", command=go_back)
    back_button.grid(row=0, column=0, padx=5)

    ok_button = tk.Button(button_frame, text="OK", command=go_next)
    ok_button.grid(row=0, column=1, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=cancel)
    cancel_button.grid(row=0, column=2, padx=5)

def main_ok():
    show_checked()

def main_cancel():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Checkbox Example")

# Variables to store checkbox states
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Create checkboxes for the main window
checkbox1 = tk.Checkbutton(root, text="Checkbox 1", variable=var1)
checkbox1.grid(row=0, column=0, sticky=tk.W)

checkbox2 = tk.Checkbutton(root, text="Checkbox 2", variable=var2)
checkbox2.grid(row=1, column=0, sticky=tk.W)

checkbox3 = tk.Checkbutton(root, text="Checkbox 3", variable=var3)
checkbox3.grid(row=2, column=0, sticky=tk.W)

# Create OK and Cancel buttons for the main window
main_button_frame = tk.Frame(root)
main_button_frame.grid(row=3, column=0, pady=10)

main_ok_button = tk.Button(main_button_frame, text="OK", command=main_ok)
main_ok_button.grid(row=0, column=0, padx=5)

main_cancel_button = tk.Button(main_button_frame, text="Cancel", command=main_cancel)
main_cancel_button.grid(row=0, column=1, padx=5)

# Start the main loop
root.mainloop()
