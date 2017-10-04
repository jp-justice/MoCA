import sqlite3
import time
import datetime
import csv

#DB Init and Connection
conn = sqlite3.connect('RcbBoardMembers.db')
c = conn.cursor()

#Functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RcbBoardMembers(mid REAL, name TEXT, surname TEXT, email TEXT)')

def dynamic_data_entry():
    name = input('Member name?')
    email = input('Member email?')
    contactNumber = input('Telephone number?')
    instrument = input('Instrument?')                      
    addTime = time.time()
    timeStamp = str(datetime.datetime.fromtimestamp(addTime).strftime('%m-%d-%Y %H:%M:%S'))
    c.execute("INSERT INTO RcbBoardMembers(name, email, contactNumber, instrument, timeStamp) VALUES(?, ?, ?, ?, ?)",
              (name, email, contactNumber, instrument, timeStamp))
    conn.commit()

def file_read():
    with open('rcbboard.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO RcbBoardMembers VALUES(?,?,?,?);", [row])
    conn.commit()
    
def db_view():
    c.execute("SELECT * FROM RcbBoardMembers")
    print(c.fetchone())

#Actions
create_table()
#dynamic_data_entry()
file_read()
#db_view()

c.close()
conn.close()



