from tkinter import *
from sys import *
import bs4 as bs
import urllib.request

root = Tk()
root.minsize(height=600, width=900)
root.title("Movie Collection Assistant")

home = Button(text="Home", height=5, width=10).grid(row=0, column=0)
add = Button(text="Add", height=5, width=10).grid(row=0, column=1)
remove = Button(text="Remove", height=5, width=10).grid(row=0, column=2)
collection = Button(text="Collection", height=5, width=10).grid(row=0, column=3)
info = Button(text="Info", height=5, width=10).grid(row=0, column=4)

output = Text().grid(row=1, column=0)

root.mainloop()
