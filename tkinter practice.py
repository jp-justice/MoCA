from tkinter import *
from sys import *
import bs4 as bs
import urllib.request
import sqlite3
import time
import datetime

#initial tk stuff
root = Tk()
root.configure(background="#696c70")
root.minsize(height=550, width=900)
root.title("Movie Collection Assistant")

#color stuff
outputBox_color= "#161616"

#db connections
conn = sqlite3.connect('movie.db')
c = conn.cursor()

#functions
help ="""
---Help Commands:---

add = Add new movie to Database
close = Close the program.
list = Print a list of currently owned movies
remove = Remove movie from Database
search = Look up movie to see if it is already in database

"""

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS MovieCollection(name TEXT, timeStamp REAL)')
    
def read_all_from_db():
    outputBox.delete(1.0, END)
    c.execute("SELECT name FROM MovieCollection")
    outputBox.insert(INSERT, c.fetchall())
    
def getHelp():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, help)

def goHome():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, '-----Welcome to the Movie Collection Assistant!-----')

def close():
    outputBox.delete(1.0, END)
    outputBox.insert(INSERT, "---Thank you for using MoCA!---")
    root.after(500)
    root.destroy()

##def getMovie():
##    with open("Movie Data.txt", 'r+') as f:
##        outputBox.delete(1.0, END)
##        mylist = f.read().splitlines()
##        mylist = sorted(set(mylist))
##        f.truncate()
##        outputBox.insert(INSERT, "---Movie Collection---\n")
##        for i in mylist:
##            outputBox.insert(INSERT, i + "\n")
##        outputBox.insert(INSERT, '\n---END OF LIST---')
##        f.close()

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

#frames
top_frame = Frame(root)
input_frame = Frame(root)
bottom_frame = Frame(root)

#grid layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#frame layout
top_frame.grid(row=0)
input_frame.grid(row=1)
bottom_frame.grid(row=2)

#file menu
menu = Menu(root)
menu.config(bg=outputBox_color)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Help", command=getHelp)
subMenu.add_command(label="Close", command=close)


#top buttons
home = Button(top_frame, text="Home", height=2, width=10, command=goHome, bg=outputBox_color, fg="white").grid(row=0, column=0)
add = Button(top_frame, text="Add", height=2, width=10, command=addMovie, bg=outputBox_color, fg="white").grid(row=0, column=1)
remove = Button(top_frame, text="Remove", height=2, width=10, command=removeMovie, bg=outputBox_color, fg="white").grid(row=0, column=2)
collection = Button(top_frame, text="Collection", height=2, width=10, command=read_all_from_db, bg=outputBox_color, fg="white").grid(row=0, column=3)
info = Button(top_frame, text="Info", height=2, width=10, bg=outputBox_color, fg="white").grid(row=0, column=4)


#output
outputBox = Text(input_frame, width=75, bd=2, background=outputBox_color, fg="white")
outputBox.grid()
outputBox.insert(INSERT, '-----Welcome to the Movie Collection Assistant!-----')

#input
inputBar = Entry(bottom_frame, width=100, bd=2, background=outputBox_color, fg="white").grid()

root.mainloop()
