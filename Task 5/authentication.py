#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe

import db
import password_utils

def register(username, password, email):
    user_id = db.create_user(username, password, email)
    if user_id:
        return True
    else:
        return False
        
def authenticate(username, password):
    user = db.get_user(username)
    if (user and password_utils.verify_password(password, user[2])):
        return True, user[0]
    else:
        return False, None
        
def change_password(username, old, new, new2):
    user = db.get_user(username)
    if (password_utils.verify_password(old, user[2]) and new==new2):
        success = db.change_user_password(username, new)
        if success:
            
            return True
        else:
            return False
            
    