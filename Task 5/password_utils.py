#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import os
import hashlib
import bcrypt
import six
import base64

salt = bcrypt.gensalt()
def hash_password(password):
    
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password (password, hash):
    password = password.encode('utf-8')
    hash = hash.encode('utf-8')
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False
