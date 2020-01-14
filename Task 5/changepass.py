#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe

import _html
import os
import cgi
import session
import authentication
import db
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("username").value
params = cgi.FieldStorage()
user = db.get_user(username)


if os.environ["REQUEST_METHOD"].upper() == "POST":
    old = params.getvalue("oldpass")
    new = params.getvalue("password")
    new2 = params.getvalue("password2")
    success = authentication.change_password(
                str(username), old, new, new2)
    if success:
        print('Location: login.py')


print("Content-type:text/html")
print("")
_html.start_html()
print('''<form method="POST">
<h2>Change Password</h2>
<p>''' + str(username) + ''' </p>
Old password <input type="password" name="oldpass"/>
New password <input type="password" name="password"/>
Repeat password <input type="password" name="password2"/>
<input type="submit" value="Change"/>
</form>''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print("<div>Change Error</div>")
_html.finish_html()
