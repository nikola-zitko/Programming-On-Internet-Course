#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import _html
import os,cgi
import session
import authentication
from http import cookies

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = authentication.authenticate(username, password)
    if(success):
        session_id = session.create_session()
        session.add_to_session({"user_id": user_id, "collection_id": 1, "username": username}, session_id=session_id)
        cookies_object = cookies.SimpleCookie()
        cookies_object["username"] = username
        print (cookies_object.output())
        print("Location: index.py")

print("")


_html.start_html()
print ('''<form method="POST">
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Login"/>
<a href="register.py">Register</a>
</form>''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print ("<div>Login Error</div>")
_html.finish_html()