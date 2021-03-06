from tkinter import *
from sys import *

root = Tk()
root.minsize(width=800, height=500)
root.title("Movie Collection Assistant")

help ="""
---Help Commands:---

add = Add new movie to Database
close = Close the program.
list = Print a list of currently owned movies
remove = Remove movie from Database
search = Look up movie to see if it is already in database

"""
def addMovie():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, '---Congratulations on your new movie!---')
    newMovie = input('---What is the name of the movie?---')
    with open("Movie Data.txt", 'r') as f:
        if newMovie in f.read():
            print('---That movie is already in the database.---')
        else:
            if newMovie.startswith('The ' or 'the '):
                newMovie = newMovie.lstrip('The ' or 'the ')
                newMovie = newMovie + ', The'
                movieData = open('Movie Data.txt', 'a')
                movieData.write(newMovie + "\n")
                movieData.close()
                print('---New movie successfully added to database! Thank you!---')
            else:
                movieData = open('Movie Data.txt', 'a')
                movieData.write(newMovie + "\n")
                movieData.close()
                print('---New movie successfully added to database! Thank you!---')



def getHelp():
    outputBox.delete(1.0, END)
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

def goHome():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, "---Welcome to the Movie Collection Assistant!---")


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Help", command=getHelp)
subMenu.add_command(label="Close", command=movieClose)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=getHelp)

#separator = Frame(height=2, bd=1, relief=RAISED)
#separator.pack(fill=X)


inputFrame = Frame(root).pack(side=BOTTOM)

#Main input box
outputBox = Text(inputFrame)
outputBox.insert(INSERT, "-----Welcome to the Movie Collection Assistant!-----")
outputBox.pack(side=RIGHT, padx=10, pady=10)

#Left Side Navigation Ribbon
navFrame = Frame(inputFrame).pack(side=LEFT)
home = add = Button(navFrame, text="Home", command=goHome, height=5).pack(side=TOP, padx=5, anchor=E, fill=X)
add = Button(navFrame, text="Add", height=5, command=addMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
remove = Button(navFrame, text="Remove", height=5, command=removeMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
collection = Button(navFrame, text="Collection", height=5, command=getMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
#more buttons can go here

#User input bar
#Search Bar


root.mainloop()





