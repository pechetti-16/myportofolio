import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
root = tk.Tk()
root.title("Image Insertion Example")

# Load the image file
image = Image.open("home.jpg")
# Resize the image if necessary
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
