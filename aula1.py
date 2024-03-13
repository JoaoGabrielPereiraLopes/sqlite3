import numbers
import sqlite3#import the library sqlite3, this library is a database library
import random#import the library ramdom, this library is a  ramdomizer number library

conection=sqlite3.connect("database")#criate database
cursor=conection.cursor()#'criate a cursor'
try:
    cursor.execute(
        'Create Table My_Table( Data text, Name text, Old real )'
    )# crete three coluns Data(text column), Name(text column) and Old(real number column)
except:
    pass
conection.commit()#finally creation

#insert values in table
cursor.execute( 'INSERT INTO My_Table VALUES ( "13/03/2024","Joao Gabriel Pereira Lopes","15")' )
cursor.execute( 'INSERT INTO My_Table VALUES ( "06/02/1970","Monica","65")' )

print(random.randint(0,10))
#one loop for returning all number in range for 0 and 10
for loop in range(10):
    
    #returning a number in range for 0 and 10
    number=random.randint(10,20)
    
    #inser numbers in table
    cursor.execute( f'INSERT INTO My_Table VALUES ( "{number**2+2*number+1}/02/1970","Monica",{number})' )