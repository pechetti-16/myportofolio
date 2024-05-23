import tkinter as tk

root = tk.Tk()
root.title("Shades of Orange")

colors = [
    "#FFA07A",  # Light Orange
    "#FF7F50",  # Coral
    "#FFA07A",  # Light Salmon
    "#FFDAB9",  # Peach
    "#FFEFD5",  # Papaya Whip
    "#F08080",
       "steel blue"   # Light Coral
]

for i, color in enumerate(colors):
    tk.Label(root, text=f"Color {i+1}", bg=color, padx=20, pady=10).pack(fill=tk.X)

root.mainloop()
