import sqlite3
import os
import numpy as np



    # Define clear_console() outside of login()

def clear_console():
    if os.name == 'nt':  # for Windows OS
        os.system('cls')
    ''' login function  '''
    
print("Press Enter to login:")
def login(log='enter'):  # add default value for log
    log=input()
    if log == 'enter':
        clear_console()

login()

class user:
    u_name=str()
    u_phone=float()
    u_age=int()
    account=1000
    pin=1010
    
''' input the card  '''

def pincard():
    print("please enter the card and enter the pin ")
    pin=int(input())
    clear_console()
    if pin==user.pin:
        print("welcom sir \n \n")
    else:
        print("your pin thant you enter it was wronge ")
        pincard()

pincard()

''' data of the user  '''

print("Enter your information\n(1) Name\n(2) Phone\n(3) Age")
user.u_name = str(input("Enter your name: "))
clear_console()
user.u_phone =float( input("Enter your phone number: "))
clear_console()
user.u_age = int(input("Enter your age: "))
clear_console()


''' function witdraw '''

def witdraw():
    print("please enter the amount you want")
    pull=int(input())

    if pull>=1000:
        print("fail")
    elif pull<50:
        print("not allow minmum is = 50")
    else:
        user.account=user.account-pull
        print("you pull from your account =",pull,"now your account plance is = ",user.account)

    ''' function deposite '''

def deposite():
    print("please enter the amount")
    push=int(input())
    user.account=user.account+push
    print("the amount you enter into your account = ",push,"now your amount is =",user.account)

''' function to check the plance of user account  '''

def checkplance():
    print("for this servise we will take from your acount 1$ \n do you wana to continue \n please chose \n (1) yes \n (2) no ")
    chose=int(input())
    if chose==1:
        print("your acount plance now is = ",user.account-1," \n thank you for chose us ")
    elif chose==2:
        print("thank you sir have anice day ")


''' function contact us  '''

def contact():
    print(" if ther any problem sir pleace leave your measage here  ")
    message=str(input())
    print(" your message it will be relplay soon thank you for choose us sir ")

''' contition for the chose the servise '''
 

print("please chose the servise you want \n","(1) deposite \n (2) withdraw \n (3) checkplance \n (4) contact us ")
servise=int(input())
if servise==1:
    deposite()
elif servise==2:
    witdraw()
elif servise==3:
    checkplance()
elif servise==4:
    contact()

clear_console()


