import sqlite3

#define connection and cursor

connection = sqlite3.connect("store_transactions")

cursor = connection.cursor()\

#create stores table

command1 = '''CREATE TABLE IF NOT EXISTS stores(stored_id INTEGER PRIMARY KEY, location TEXT)'''

cursor.execute(command1)

#create purchases table

command2 = '''CREATE TABLE IF NOT EXISTS purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id))'''

cursor.execute(command2)

#add to stores


cursor.execute("INSERT INTO stores VALUES (95, 'Melbourne,Victoria')")
cursor.execute("INSERT INTO stores VALUES (21, 'Sydney,NSW')")
cursor.execute("INSERT INTO stores VALUES (69, 'Brisbane, QLD')")


#add to purchases


cursor.execute("INSERT INTO purchases VALUES(51,21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES(23,62, 21.29)")

#get results

cursor.execute("SELECT * FROM purchases")

#updating

cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")

results = cursor.fetchall()
print(results)