#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe

import _html
import os
import cgi
import session
import authentication
import db
from http import cookies

params = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == "POST":

  user = params.getvalue("username")
  if not user:
    print("Location: change_pass_first.py")
  else:
    cookies_object = cookies.SimpleCookie()
    cookies_object["username"] = user
    print(cookies_object.output())
    print("Location: changepass.py")


print("")
_html.start_html()
print('''<form class="register-form" method="POST">
<h2>Change Password</h2>
Username <input type="text" name="username"/>
<input type="submit" value="Next"/>
</form>''')
_html.finish_html()
