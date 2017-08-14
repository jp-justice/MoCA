from tkinter import *

root = Tk()
root.minsize(width=800, height=600)

fileFrame = Frame(root).pack(fill=X)

file = Button(fileFrame, text="File").pack(anchor=W)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X)


inputFrame = Frame(root).pack(side=BOTTOM)

#Main input box
outputBox = Text(inputFrame)
outputBox.insert(INSERT, "-----Welcome to the Movie Collection Assistant!-----")
outputBox.pack(side=RIGHT, padx=10, pady=10)

#Left Side Navigation Ribbon
navFrame = Frame(inputFrame).pack(side=LEFT)
add = Button(navFrame, text="ADD").pack(side=TOP, pady=0, anchor=E)
remove = Button(navFrame, text="REMOVE").pack(side=TOP, pady=0, anchor=E)
collection = Button(navFrame, text="Collection").pack(side=TOP, pady=0, anchor=E)
#more buttons can go here

#User input bar
#Search Bar

root.title("Movie Collection Assistant")
root.mainloop()

