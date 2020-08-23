import sqlite3

class newUser():
    def __init__ (self, userName, password):
        database = '/Users/vjain/subs.db'
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()

        cursor.execute("INSERT INTO user(userID, userName, password) VALUES (1, userName, password);")
        print("Successfully added new user:", userName)
        
        #cursor.execute("SELECT * FROM user;")
        #print(cursor.fetchall())

        sqliteConnection.commit()
        cursor.close()