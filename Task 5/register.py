#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import _html
import authentication
import cgi, os
import six


params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    
    username = params.getvalue("username")
    email = params.getvalue("email")
    password = params.getvalue("password")
    password2 = params.getvalue("password2")
    if(password==password2):
        success = authentication.register(username, password, email)
        if success:
            print('Location: login.py')
print()
_html.start_html()
print ('''<form method="POST">
username <input type="text" name="username" />
email <input type="email" name="email" />
password <input type="password" name="password"/>
repeat password <input type="password" name="password2"/>

<input type="submit" value="Register"/>
</form>''')
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error</div>")
_html.finish_html()