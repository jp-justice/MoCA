from tkinter import *
from sys import *
import bs4 as bs
import urllib.request


root = Tk()
root.minsize(height=600, width=900)
root.title("Movie Collection Assistant")

help ="""
---Help Commands:---

add = Add new movie to Database
close = Close the program.
list = Print a list of currently owned movies
remove = Remove movie from Database
search = Look up movie to see if it is already in database

"""

def itemInfo():
    outputBox.delete(1.0, END)
    movie_url = input('---What is the IMDB URL for your movie?---\n')
    sauce = urllib.request.urlopen(movie_url).read
    soup = bs.BeautifulSoup(sauce(), "lxml")
    director = soup.find('span', {'class': 'itemprop', 'itemprop': 'name'})
    year = soup.find('a', {'title': 'See more release dates'})
    name = soup.title.string
    name = name.replace('*', '')[:-8]
    name = name.replace('*', '')[:len(name)-5]
    outputBox.insert(INSERT, "Your movie's name is " + name + "\n")
    outputBox.insert(INSERT, "Your movie's director is " + director.text + "\n")
    outputBox.insert(INSERT, "Your movie's release date was "+ year.text + "\n")
    

def addMovie():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, '---Congratulations on your new movie!---')
    newMovie = input('---What is the name of the movie?---')
    with open("Movie Data.txt", 'r') as f:
        if newMovie == '':
            outputBox.delete(1.0, END)
            outputBox.insert(INSERT, '---Please input a valid movie to continue.---')
            
        if newMovie in f.read() and newMovie != '':
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
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, "---Thank you for using MoCA!---")
    root.after(500)
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


inputFrame = Frame(root).pack(side=BOTTOM)

#Main input box
outputBox = Text(inputFrame)
outputBox.insert(INSERT, "-----Welcome to the Movie Collection Assistant!-----")
outputBox.pack(side=RIGHT, padx=10, pady=10)
usertext = StringVar()
e = Entry(inputFrame, textvariable=usertext)
e.pack(side=BOTTOM)

#Left Side Navigation Ribbon
navFrame = Frame(root).pack(side=LEFT)
home = add = Button(navFrame, text="Home", command=goHome, height=5).pack(side=TOP, padx=5, anchor=E, fill=X)
add = Button(navFrame, text="Add", height=5, command=addMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
remove = Button(navFrame, text="Remove", height=5, command=removeMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
collection = Button(navFrame, text="Collection", height=5, command=getMovie).pack(side=TOP, padx=5, anchor=E, fill=X)
info = Button(navFrame, text="Info", height=5, command=itemInfo).pack(side=TOP, padx=5, anchor=E, fill=X)
#more buttons can go here

#User input bar

#Search Bar


root.mainloop()





