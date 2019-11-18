#!/usr/bin/python3
from tkinter import *
root = Tk()
label = Label( root, text="esto es un label" )
button = Button( root, text="texto del boton" )
label.pack()
button.pack()
root.mainloop()