#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import mysql.connector  
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name":"zadatak5",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb
def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def get_collections():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM collections")
    myresult = cursor.fetchall()
    return myresult

def get_paths(collection_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT path FROM image WHERE collection_id=" + str(collection_id))
    myresult = cursor.fetchall()
    return myresult

def upload(path, collection_id):
    query = "INSERT INTO image (path, collection_id) VALUES (%s, %s)"
    values = (path,collection_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def create_collection(collection):
    query = "INSERT INTO collections (collection) VALUES (%s)"
    values = (collection,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def create_user(username, password, email):
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password, email)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + str(username) + "'")
    myresult = cursor.fetchone()
    return myresult

def change_user_password(name, password):
    
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    hashed_password = password_utils.hash_password(password)
    query = "UPDATE users SET password=%s WHERE username=%s"
    values = (hashed_password, name)
    try:
        cursor.execute(query, values)
        mydb.commit()
        return True
    except:
        
        return False

def get_hash(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT password FROM users WHERE username='" + str(username) + "'")
    myresult = cursor.fetchone()
    return myresult