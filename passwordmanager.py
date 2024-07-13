from cryptography.fernet import Fernet


# we use crytography module for encryption 
# for installing this go to terminal
#pip install cryptography

master_pwd = input("what is the master password? ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
# In Python, the "wb" mode is used when opening a file for writing in binary mode. This is particularly useful when you are working with binary data, such as images or other non-text files. When you open a file in "wb" mode

def view():
     with open('passwords.txt','r') as f:
         for line in f.readlines():
             data = line.rstrip()
             user , passw = data.split(" | ")
             print("user:",user," | password:",passw)
# rstrip() removes all the trailing whitespaces      

def add():
    name = input('Account Name: ')
    pwd = input("Password:")
# a  is appending.This helps us to write things in the existing file or helps us to create the new file in which we can write 
# w is for writing file and if you open it w it will clear the passowrds.txt file and make it a entirely new one 
# r is simply read mode and it is used for reading the file 
    with open('passwords.txt','a') as f:
        f.write(name + " " + pwd + "/n")
         



while True:
    mode = input("Would you like to add a new password or view the existing ones(view/add),press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue






































