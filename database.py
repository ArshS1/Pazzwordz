#import modules
import mysql.connector
import random
import sys

#make a function for user to choose their designated option
def main_menu():
    print("\nWelcome to passwordManager\n")
    print("Choice 1 is for adding new password")
    print("Choice 2 is to navigate through previously saved passwords")
    print("Choice 3 is to generate a secure password")
    print("Choice 4 is to quit the password manager\n")
main_menu()

#ask user's for the choice and then return the choice
def input_check():
    choice = int(input("Please enter your choice number: ")) 
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        return choice

    while choice >= 5 or choice <= 0:
        print("Invalid choice of action\nTry Again\n")
        choice = int(input("Please enter your choice number: ")) 

userChoice = input_check()

#set up the mysql database
db = mysql.connector.connect(
user = 'root',
password = '1219$arsh5$',
host = 'localhost',
database = 'PASSWORD_MANAGER')
mycursor = db.cursor()

def createTable():
    #comment out after the table was created once to avoid replication
    mycursor.execute("CREATE TABLE passwords")   
    
    #comment out after the table and variables have been created to keep data inside one table
    mycursor.execute("CREATE TABLE passwords(website VARCHAR(255), email VARCHAR(255), username VARCHAR(255), password VARCHAR(255))")
#comment out after first call in order to avoid table duplication
createTable()

#choice 4 is to exit the password manager
def exitFunction():
    print("...Exiting the program...\n")
    sys.exit()

#choice 1 ask the user for input so they data can be stored in the database
def choice1():
    website = input("Enter website name: ")
    email = input("Enter email associated with this website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    #plug in the given data into the database          #put values as %s as they are going to be filled in later
    insertDATA = "INSERT INTO passwords (website, email, username, password) VALUES (%s, %s, %s, %s)"
    loginINFORMATION = (website, email, username, password)
    mycursor.execute(insertDATA, loginINFORMATION)

    #commit the changes to make sure that data is pushed to mysql database
    db.commit()

    print("\nThe provided information was added to the database successfully\n")


#choice 2 show the user the data stored inside the database
def choice2():
    mycursor.execute("SELECT * FROM passwords")
    result = mycursor.fetchall()
    column_name = [i[0]
        for i in mycursor.description ]
    print(column_name)
    for row in result:
        print(row)

#choice 3 create a random password 
def choice3():
    randomPassword = ""
    for i in range(3): 
        passwordSymbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", ",", "?", "/"]
        passwordLetters = ["q", "w", "e", "r", "t", "y", "u", "i", "u", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
        passwordNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        #randomly pick out values from different lists created above

        w = random.choice(passwordSymbols)
        x = random.choice(passwordLetters)
        y = random.choice(passwordLetters).upper()
        z = random.choice(passwordNumbers)
        randomPassword +=  w + x + y + z 

    #print out the value created within the randomPassword variable
    print("The following is a secure password that has been generated for you: " + randomPassword + "\n")

#call the function based on user's input
def callingAction(userchoice):
    if userChoice == 1:
        choice1()
    elif userChoice == 2:
        choice2()
    elif userChoice == 3:
        choice3()
    else: 
        exitFunction()

#call the action in order to get start with the designated action
callingAction(userChoice)

