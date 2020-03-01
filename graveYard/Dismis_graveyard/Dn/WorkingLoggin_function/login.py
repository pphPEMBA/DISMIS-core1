import sqlite3
import time

def login():
    while True:
        #for i in range(3)
        username = input("username")
        password = input("password")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username), (password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("welcome"+i[2])
            #return("exit")
            break
        else:
            print("Username and password not recognised")
            again = input("Do you want to try again? (y/n): ")
            if again.lower() == "n":
                print("good bye")
            time.sleep(1)
                #return("exit")
                break

def newUser():
    found = 0
    while found == 0:
        username = input("username")
        #password = input("password")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username Taken, please try another")
        else:
            found = 1

    firstName = input()
    surname = input("surname")
    password = input("paassword")
    password1 = input("password")
    while password != password1:
        print('password not match')
        password = input("paassword")
        password1 = input("password")
    insertData = ''' INSERT INTO user(username, firstname, surname, password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[ (username), (firstName), (surname), (password)])
    db.commit()
