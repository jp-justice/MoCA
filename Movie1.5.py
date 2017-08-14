import sys

title ="""
********************
*----Movie List----*
********************
"""

help = """

add = Add new movie to Database
close = Close the program.
list = Print a list of currently owned movies
remove = Remove movie from Database
search = Look up movie to see if it is already in database

"""

#Function to print list of movies
def getMovie():
    with open('Movie Data.txt', 'r+') as f:
        mylist = f.read().splitlines()
        mylist = sorted(set(mylist))
        f.truncate()        
        for i in mylist:
            print(i)
        print('---END OF LIST---')
        f.close()
        
        
#Function to add new movies
def addMovie():
    print('---Congratulations on your new movie!---')
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

#Function to continue
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
                
#Function to remove movies
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
    

def searchMovie():
        searchMovie = input("---Please input your movie.---\n").lower()
        if searchMovie =='':
            print('---Please input a valid name.---')
            keepGoing()
        print('---Search Results---')
        with open('Movie Data.txt', 'r') as f:
            for line in f:
                if searchMovie in line.lower():
                    print(line)
                else:
                    continue             

def movieClose():
    print('---Thank you for using movie database!---')
    print('---Goodbye!---')
    sys.exit()
                          
#Initialize app to start program
def movieMain():
    while True:
        command = input('---What would you like to do? Type HELP for a list of commands.---\n')
        validCommand = ['add', 'close', 'help', 'list', 'search', 'remove']
        if command not in validCommand:
            print('---Your command is not valid. Please input a valid command.---')
        else:
            if command.lower() == 'help':
                print(help)
            if command.lower() == 'close':
                movieClose()
                break
            if command.lower() == 'list':
                getMovie()
                keepGoing()
                break
            if command.lower() == 'search':
                searchMovie()
                keepGoing()
                break
            if command.lower() == 'add':
                addMovie()
                keepGoing()
                break
            if command.lower() == 'remove':
                removeMovie()
                keepGoing()
                break

print(title)
movieMain()



        
    
    

