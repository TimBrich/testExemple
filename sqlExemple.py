import sqlite3

#Пример взят с https://pythonru.com/osnovy/sqlite-v-python

conn = sqlite3.connect('testBD.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
if 1 not in [i[0] for i in all_results] or 2 not in [i[0] for i in all_results] or 3 not in [i[0] for i in all_results] or 4 not in [i[0] for i in all_results]:
    cur.execute("""INSERT INTO users(userid, fname, lname, gender)
       VALUES('00001', 'Alex', 'Smith', 'male');""")
    conn.commit()

    user = ('00002', 'Lois', 'Lane', 'Female')
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
    conn.commit()

    more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
    conn.commit()

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)
