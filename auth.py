#register
# - first name, last name, password, email
# - generate user account


#login
# - account number & password

#bank operations

#Initializing the system
import random 
import validation
import database
from getpass import getpass

def init():
    print("Welcome to bankPhP")
      
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    
    elif(haveAccount ==2):
        
        register()

    else:
        print("You have selected invalid option")
        init()
   


def login():
    print("****** Login *****")

    accountNumberFromUser = input("What is your account number? \n")

    isValidAccountNumber= validation.accountNumberValidation(accountNumberFromUser)
    
    if isValidAccountNumber: 

        password = getpass("What is your password \n ")

        user = database.authenticate_user(accountNumberFromUser, password)

        if user:

            database.user_auth_session(accountNumberFromUser, user)
            bankOperation(user, accountNumberFromUser)
    
        print("Invalid  account or password")
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()



def register():
    print(" ******Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    accountNumber =generateAccountNumber()
         
    isUserCreated = database.create(accountNumber, email, first_name, last_name, password)
    
    if isUserCreated:

        print("Your Account Has been created")
        print("== ==== ===== ===== ===")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print("== ==== ===== ===== ===")

        login()

    else:
        print("something went wrong, please try again")
        register()

    print("Your Account Has Been Created")

    login()

def bankOperation(user, accountNumberFromUser):
    print("Welcome %s %s" % (user[0], user [1]))
   
    selectedOption = int(input("what would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    
    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout(accountNumberFromUser)
    elif(selectedOption == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user, accountNumberFromUser)

def withdrawalOperation():
    print("withdrawal")

def depositOperation():
    print("Deposit Operations")


def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance 

def getCurrentBalance(userDetails):
    return userDetails[4]

def logout(accountNumberFromUser):
    database.delete_auth_session(accountNumberFromUser)
    login()
    

#### ACTUAL BANKING SYSTEM ####
init()
