import sqlite3
import time
import datetime
import random
import bs4 as bs
import urllib.request
import sys

conn = sqlite3.connect('movie.db')
c = conn.cursor()

##movie_url = input("What is your movie's URL?\n")
##sauce = urllib.request.urlopen(movie_url).read
##soup = bs.BeautifulSoup(sauce(), "lxml")

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS MovieCollection(name TEXT, timeStamp REAL')

def data_entry():
    c.execute("INSERT INTO MovieCollection VALUES(1, 'Hot Fuzz', 'Edgar Wright')")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    name = line
    addTime = time.time()
    timeStamp = str(datetime.datetime.fromtimestamp(addTime).strftime('%m-%d-%Y %H:%M:%S'))
    c.execute("INSERT INTO MovieCollection (name, timeStamp) VALUES(?, ?)",
              (name, timeStamp))
    conn.commit()

def read_from_db():
    fetch = input('What movie would you like info on?\n')
    c.execute("SELECT * FROM MovieCollection WHERE name = (?);" (fetch,))
    print(c.fetchall())
    conn.close()
    




create_table()
##with open('Movie Data.txt', 'r+') as f:
##    for line in f:
##        dynamic_data_entry()
##        #time.sleep(1)
read_from_db()
c.close()
conn.close()
