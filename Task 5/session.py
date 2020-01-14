#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import db
import os
from http import cookies


def create_session():
    session_id = db.create_session()
    cookies_object = cookies.SimpleCookie()
    cookies_object["session_id"] = session_id
    cookies_object["collection_id"] = 1
    print (cookies_object.output()) #upisivanje cookie-a u header
    return session_id

def destroy_session():
    session_id = get_session_id()
    destroy_session_id()
    db.destroy_session(session_id)

def get_collection_id(session_id):
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    collection_id = get_all_cookies_object.get("collection_id").value if get_all_cookies_object.get("collection_id") else None
    return collection_id
        
def set_collection_id(collection_id):
    cookies_object = cookies.SimpleCookie()
    cookies_object["collection_id"] = collection_id
    print (cookies_object.output())
    
def get_collection_name(collection_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT collection FROM collections WHERE collection_id = '"+ str(collection_id) + "'")
    result = cursor.fetchone()
    return result[0]

def get_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    return session_id

def destroy_session_id():
    cookies_object = cookies.SimpleCookie()
    cookies_object["session_id"] = ""
    cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    print (cookies_object.output()) #upisivanje cookie-a u header

def add_to_session(dict, session_id=None):
    if session_id is None:
        session_id = get_session_id()
    _, data = db.get_session(session_id)#vracanje do sada odabranih podataka
    for key, value in dict.items():
        data[key] = value
    db.replace_session(session_id, data)

def remove_from_session(dict):
    session_id = get_session_id()
    _, data = db.get_session(session_id)
    for key in dict:
        data.pop(key, None)
    db.replace_session(session_id, data)

def get_session_data():
    session_id = get_session_id()
    if session_id:
        _, data = db.get_session(session_id)
    else:
        data = None
    return data

