import sys
import os
import json

# rootPath = os.path.dirname(os.path.abspath(__file__))
# os.chdir(rootPath)
# filename = "username.json"

# try:
#     with open(filename) as fileObject:
#         username = json.load(fileObject)
# except:
#     username = input("What is your name? ")
#     with open(filename, 'w') as fileObject:
#         json.dump(username, fileObject)
#         print("We'll remember you when you come back, {0}".format(username))
# else:
#     print("Welcome back, {0}".format(username))

# a = None
# if a:
#     print(True)
# else:
#     print(False)

def get_stored_username(filename):
    """This is a description"""

    try:
        with open(filename) as fileObejct:
            username = json.load(fileObejct)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    """This is a description"""

    username = input("Please Enter Your Name: ")
    with open(filename, 'w') as fileObject:
        json.dump(username, fileObject)
    return username


def greet_user(filename):
    """This is a description"""
    
    username = get_stored_username(filename)
    if username:
        print("Welcome back, {0}".format(username))
    else:
        username = get_new_username(filename)
        print("We'll remember you when you come back, {0}".format(username))


if __name__ == '__main__':
    rootPath = os.path.dirname(os.path.abspath(__file__))
    os.chdir(rootPath)

    filename = "username.json"
    greet_user(filename)