# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 08:00:59 2018

@author: Papun Mohanty
"""
from faker import Faker
import sqlite3
import time

# Creating Faker Object
faker_factory = Faker()

try:
    conn = sqlite3.connect('human.db')
    cursor = conn.cursor()
    print("Opened database successfully")
    cursor.execute("""CREATE TABLE human (
            NAME CHAR(250),
            DOB CHAR(250),
            ADDRESS CHAR(250),
            EMAIL CHAR(250),
            COMPANY_EMAIL CHAR(250),
            CIGARATES_SMOKES INT,
            NUMBER_OF_CHILDREN INT,
            PHONE_NUMBER CHAR(250),
            FAVOURITE_COLOR CHAR(250),
            JOB CHAR(250)
            )""")
    conn.commit()
    conn.close()
except:
    print('There is some problem creating the Database')


number_of_human = int(input("Enter how many numbers of Human you want to insert in the Database: "))
number_of_db_entries = 0
list_humam = []
t1 = time.time()

# Iterating over the number of database entries.
for human in range(number_of_human):
    # Creating fake Data.
    name                = faker_factory.name()
    dob                 = str(faker_factory.date_of_birth())
    address             = faker_factory.address()
    email               =  faker_factory.email()
    company_email       = faker_factory.company_email()
    cigarates_smokes    = faker_factory.random_digit()
    number_of_childeren = faker_factory.random_digit()
    phone_number        = faker_factory.phone_number()
    favourite_color     = faker_factory.color_name()
    job                 = faker_factory.job()

    # Connecting to the Database.
    conn = sqlite3.connect('human.db')
    cursor = conn.cursor()

    # Inserting Fake Data into the table.
    list_humam.append((name, dob, address, email, company_email, cigarates_smokes, number_of_childeren, phone_number, favourite_color, job))



    # cursor.execute("INSERT INTO human VALUES ('{}', '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}')".format(name, dob, address, email, company_email, cigarates_smokes, number_of_childeren, phone_number, favourite_color, job))
    
    number_of_db_entries += 1
    print("Running for {}th human".format(number_of_db_entries))
    
    
cursor.executemany("INSERT INTO human (NAME, DOB, ADDRESS, EMAIL, COMPANY_EMAIL, CIGARATES_SMOKES, NUMBER_OF_CHILDREN, PHONE_NUMBER, FAVOURITE_COLOR, JOB) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list_humam)
print("Inserted database successfully")

# Commiting the data for the connection.
conn.commit()

# Closing the connection.
conn.close()

t2 = time.time() - t1
print("Total number of Database entries is: ", number_of_db_entries)
print("To insert {} number of Human entry, this machine took {} seconds.".format(number_of_human, t2))