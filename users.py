import sqlite3

class newUser():
    def __init__ (self, userName, password):
        sqliteConnection = sqlite3.connect('subs.db')
        cursor = sqliteConnection.cursor()
        # subs2.db = '/Users/Vinathi/Downloads/subs2.db'

        cursor.execute("INSERT INTO user (userID, userName, password) VALUES (1, userName, password)")
        print("Successfully added new user:", userName)

        sqliteConnection.commit()
        cursor.close()