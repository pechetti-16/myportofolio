from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

def draw_checkbox():
    # Draw checkbox
    checkbox_size = 20
    checkbox_position = (500, 500)
    checkbox_color = "black"
    draw.rectangle([checkbox_position, (checkbox_position[0] + checkbox_size, checkbox_position[1] + checkbox_size)], outline=checkbox_color, width=2)

def toggle_checkbox():
    global checkbox_checked
    checkbox_checked = not checkbox_checked
    draw_image()

def draw_image():
    # Open the image
    im = Image.open(image_path)

    # Create a drawing object
    global draw
    draw = ImageDraw.Draw(im)

    # Set font and size
    font = ImageFont.truetype("arial.ttf", 100)

    # Set text parameters
    text = "nyfa"
    text_color = "black"
    text_position = (530, 500)

    # Draw text
    draw.text(text_position, text, text_color, font=font)

    # Draw checkbox if checked
    if checkbox_checked:
        draw_checkbox()

    # Show the image
    im.show()

def open_file_dialog():
    global image_path
    image_path = filedialog.askopenfilename()
    draw_image()

# Global variables
checkbox_checked = False
image_path = ""

# Create Tkinter window
root = tk.Tk()
root.title("Image with Checkbox")

# Create buttons
open_button = tk.Button(root, text="Open Image", command=open_file_dialog)
toggle_button = tk.Button(root, text="Toggle Checkbox", command=toggle_checkbox)

# Pack buttons
open_button.pack()
toggle_button.pack()

# Run Tkinter main loop
root.mainloop()
