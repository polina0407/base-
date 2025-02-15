import sqlite3
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

cursor.execute('''SELECT * FROM artists''')
data = cursor.fetchall()
print(len(data))

cursor.execute('''SELECT * FROM artists WHERE gender="Female"''')
data = cursor.fetchall()
print(len(data))

cursor.execute('''SELECT * FROM artists WHERE [birth year] < 1900''')
data = cursor.fetchall()
print(len(data))