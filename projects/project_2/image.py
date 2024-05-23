from PIL import Image,ImageDraw,ImageFont
from tkinter import *

im=Image.open(NONE)

#draw=ImageDraw.Draw(im)
draw=ImageDraw.Draw(im)
fon=ImageFont.truetype("arial.ttf",100)
points=500,500
st="nyfa"
color="black"

draw.text(points,st,color,font=fon)
im.show()
