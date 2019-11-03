'''
this will input the word frequency from the word_search.tsv file
to WORD_FREQUENCY table
'''

import cx_Oracle
from getpass import getpass

username = input("Enter Username: ")
password = getpass("Enter Oracle password: ")
servicename = input('Enter your oracle service name: ')

con = cx_Oracle.connect(username+"/"+password+'@localhost/'+servicename)
cur = con.cursor()

with open('word_search.tsv') as file:
    for line in file:
        cur.execute("""
            insert into WORD_FREQUENCY
            values (:1, :2)""", line.split())
    con.commit()
