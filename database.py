# create record
# update record
# read record
# delete record 
# CRUD

#find user

import os
import validation
import datetime

x = datetime.datetime.now()

user_db_path ="data/user_record/"
user_auth_path ="data/auth_session/"

def create(accountNumber, email, first_name, last_name, password):

    userData = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    
    if DoesAccountNumberExist(accountNumber):
        return False

    if doesEmailExist(email):  
        print("User already exists")
        return False     

    completionState = False

    
    try:
        
        f = open(user_db_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:

        doesFileContainData = read(user_db_path + str(accountNumber)+ ".txt")
        
        if not doesFileContainData:
            delete(accountNumber)

    else:
        f.write(str(userData))
        completionState = True
            

    finally:
        f.close()
        return completionState
    

    #create a file
    #name of the file would be accountNumber.txt
    # add user details to the file
    # return true
    #if saving to file fails, then delete created file 

def read(userAccountNumber):
    
    #find user with account number
    #fetch content of the file
    is_account_number_valid = validation.accountNumberValidation(userAccountNumber)

    try:
        if is_account_number_valid:
        
            f = open(user_db_path + str(userAccountNumber)+ ".txt", "r")
        
        else:
            pass

    except FileNotFoundError:
        print("User not found")

    except FileExistsError:
        print("User doesn't exist")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()

    return False

def update(userAccountNumber):
    print("update user record")
    #find user with account number
    #fetch the content of the file 
    #update the content of the file 
    #save the file 
    #return true

def delete(userAccountNumber):
    
    isDeleteSuccessful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + ".txt"):
      
        try:
            os.remove(user_db_path + str(userAccountNumber) + ".txt")
            isDeleteSuccessful = True

        except FileNotFoundError:
            print(" User not found")

        finally: 

            return isDeleteSuccessful
    #find user with account number
    #delete the user record(file)
    #return true

def doesEmailExist(email):
    
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
       userList = str.split(read(user), ',')
       if email in userList:
           return True 
    return False

def DoesAccountNumberExist(accountNumber):
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
        if user == str(accountNumber) + ".txt":
           return True  
    return False

def authenticate_user(accountNumber, password):
    
    if DoesAccountNumberExist(accountNumber):
        
        user = str.split(read(accountNumber), ',')
        if password == user[3]:
            return user
            
    return False

def user_auth_session(accountNumber, userdetails):

    data_to_save = "{} {} logged in at {}".format(userdetails[0], userdetails[1], x)

    try:

        f = open(user_auth_path + str(accountNumber) + ".txt", "w")

        f.write(data_to_save)

    except:

        pass
    
    return True


def delete_auth_session(accountNumber):

    if os.path.exists(user_auth_path + str(accountNumber) + ".txt"):
        try:
            os.remove(user_auth_path + accountNumber + ".txt")
        
        except FileNotFoundError:

            print("User session not found")

    return True



# print(doesEmailExist(7898941159,"agv1225@hotmail.com"))

#print(read(7898941159))
