import sqlite3
import time
import datetime
import csv

#db connections
conn = sqlite3.connect('MPAA.db')
c = conn.cursor()

#db creation
c.execute('CREATE TABLE IF NOT EXISTS MPAA_DB(Release Year REAL, ID REAL, Name TEXT)')

#Functions
with open("MPAA.csv", 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        c.execute("INSERT INTO MPAA_DB(Release Year, ID, Name) VALUES (?,?,?);", row)
    conn.commit()
    conn.close()

#Actions

    

conn.commit()
conn.close()
