import tkinter as tk

def toggle_checkbox():
    global checkbox_checked
    checkbox_checked = not checkbox_checked
    update_label()

def update_label():
    text = "[X]" if checkbox_checked else "[ ]"
    label.config(text=text)

# Global variables
checkbox_checked = False

# Create Tkinter window
root = tk.Tk()
root.title("Transparent Label")

# Set the window to be transparent
root.attributes('-alpha', 0.7)

# Create label for displaying text
label = tk.Label(root, text="[ ]", font=("Arial", 20), fg="black")
label.pack()

# Toggle button
toggle_button = tk.Button(root, text="Toggle Checkbox", command=toggle_checkbox)
toggle_button.pack()

# Run Tkinter main loop
root.mainloop()
