import sqlite3 

conn = sqlite3.connect("database.db") 
print("Opened database successfully") 

#conn.execute('DROP TABLE student_information') 
#print('table dropped ') 
conn.execute('CREATE TABLE student_information(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT, city TEXT, pin TEXT)')
print("Table created successfully") 
conn.close 


