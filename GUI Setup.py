from tkinter import *
from sys import *

root = Tk()
root.minsize(width=800, height=500)

help ="""

add = Add new movie to Database
close = Close the program.
list = Print a list of currently owned movies
remove = Remove movie from Database
search = Look up movie to see if it is already in database

"""

def getHelp():
    outputBox.insert(INSERT, help)

def getMovie():
    with open("Movie Data.txt", 'r+') as f:
        outputBox.delete(1.0, END)
        mylist = f.read().splitlines()
        mylist = sorted(set(mylist))
        f.truncate()
        outputBox.insert(INSERT, "---Movie Collection---\n")
        for i in mylist:
            outputBox.insert(INSERT, i + "\n")
        outputBox.insert(INSERT, '\n---END OF LIST---')
        f.close()

def keepGoing():
    while True:
        validAnswer =('yes', 'no')
        keepGoing = input('---Is there anything else that you would like to do? Yes/No---\n')
        if keepGoing.lower() not in validAnswer:
            print('---Please input a valid command.---')
        else:
            if keepGoing.lower() == 'yes':
                movieMain()
            else:
                print('---Thank you for using movie database!---')
                print('---Goodbye.---')
                sys.exit()


def removeMovie():
    name = input('---Please input the name of the movie that you would like to remove.---')
    confirm = input('---Are you sure you want to remove %s from your database? Yes/No---' %name)
    if confirm.lower() == 'yes':
        with open("Movie Data.txt", "r+") as f:
            t = f.read()
            to_delete = name.strip()
            f.seek(0)
            for line in t.split('\n'):
                if line != to_delete:
                    f.write(line + '\n')
            f.truncate()
    else:
        keepGoing()
        
def movieClose():
    root.after(1000)
    root.destroy()
    
menu = Menu(root)

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Help", command=getHelp)
subMenu.add_separator()
subMenu.add_command(label="Close", command=movieClose)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=getHelp)

separator = Frame(height=2, bd=1, relief=RAISED)
separator.pack(fill=X)


inputFrame = Frame(root).pack(side=BOTTOM)

#Main input box
outputBox = Text(inputFrame)
outputBox.insert(INSERT, "-----Welcome to the Movie Collection Assistant!-----")
outputBox.pack(side=RIGHT, padx=10, pady=10)

#Left Side Navigation Ribbon
navFrame = Frame(inputFrame).pack(side=LEFT)
add = Button(navFrame, text="Add", height=5).pack(side=TOP, padx=5, anchor=E, fill=X)
remove = Button(navFrame, text="Remove", height=5, command=removeMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
collection = Button(navFrame, text="Collection", height=5, command=getMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
#more buttons can go here

#User input bar
#Search Bar

root.title("Movie Collection Assistant")
root.mainloop()





