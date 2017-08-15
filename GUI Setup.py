from tkinter import *

root = Tk()
root.minsize(width=800, height=600)

def doNothing():
    print("ok ok I won't...")

def getMovie():
    with open("Movie Data.txt", 'r+') as f:
        mylist = f.read().splitlines()
        mylist = sorted(set(mylist))
        f.truncate()        
        for i in mylist:
            print(i)
        print('---END OF LIST---')
        f.close()

menu = Menu(root)

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Help", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Close", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

separator = Frame(height=2, bd=1, relief=RAISED)
separator.pack(fill=X)


inputFrame = Frame(root).pack(side=BOTTOM)

#Main input box
outputBox = Text(inputFrame)
outputBox.insert(INSERT, "-----Welcome to the Movie Collection Assistant!-----")
outputBox.pack(side=RIGHT, padx=10, pady=10)

#Left Side Navigation Ribbon
navFrame = Frame(inputFrame).pack(side=LEFT)
add = Button(navFrame, text="Add", height=5).pack(side=TOP, pady=0, anchor=E, fill=X)
remove = Button(navFrame, text="Remove", height=5).pack(side=TOP, pady=0, anchor=E, fill=X)
collection = Button(navFrame, text="Collection", height=5, command=getMovie).pack(side=TOP, pady=0, anchor=E, fill=X)
#more buttons can go here

#User input bar
#Search Bar

root.title("Movie Collection Assistant")
root.mainloop()





