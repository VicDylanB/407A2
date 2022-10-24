"""
Password Managewr
Dylan Brown
11/10/22
"""
import os
from turtle import clear
import sys

    

#Defines the Text menu
def menu():
    print (10 * "-" , "MENU" , 10 * "-")
    print('[1] New Credentials')
    print('[2] Read Credentials')
    print('[3] Exit')
    print (27 * "-")

#Adds new credentials
def NewCreds():
    file = open("creds.txt", 'a')
    WebURL = 'Website URL: ' + input('Enter Website URL: ') + "\n"
    UserName = 'Username: ' + input('Enter Username Login: ') + "\n"
    NewPass = 'Password: ' + input('Enter Password: ') + "\n"
    print()

    file.write(WebURL)
    file.write(UserName)
    file.write(NewPass)
    file.write('\n')
    file.close
    print('Credentials Added')
    print()


#Reads credentials from file 
def ReadCreds():
    check = os.path.getsize('creds.txt')
    if check == 0:
        print('File is empty please input credentials')
    else:
        file = open("creds.txt", 'r') 
        StoredCreds = file.read()
        print("Reading Credentials\n")
        print(StoredCreds)
        file.close()

#Checks if file exists and if not creates one
if os.path.exists("creds.txt"):
    print('File exists\n')
else:
    with open('creds.txt', 'w') as f:
        print('File Created')
        file = 'creds.txt'
        file.close


#Begins while loop for choice in menu system
while True:
    menu()
    try:
       choice = float(input("Pick Menu [1-3]: "))
    except ValueError:
        os.system('cls')
        print('Invalid option') 

#Creates the choices for the menu
    if choice==1:
        os.system('cls')
        print('Add New Credentials')
        NewCreds()
    elif choice == 2:
        os.system('cls')
        ReadCreds()
    elif choice==3:
        print('Goodbye exiting')
        sys.exit
        break
    elif choice > 3:
        os.system('cls')
        print('Invalid option')

"""
Hettige Jayatissa
22/10/22
Version 3
This code stores and reads Usernames and Passwords for inputted Websites
1 = select menu 1
A help section could be added to enhance the functionality of the program if users get confused
"""