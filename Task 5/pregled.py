#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import _html
import os,cgi
import session
import authentication
import db
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("username").value
params = cgi.FieldStorage()
user = db.get_user(username)
data = session.get_session_data()
if data is None:
    print("Location: splash.py")

if  user[4] != "admin":
    print("Location: index.py")

   
slike = db.get_images()

print()
_html.start_html()
for slika in slike:
    print("<p>"+str(slika[1])+" - Count number: "+str(slika[2])+"</p>")
print('<a href="index.py">Back</a>')


_html.finish_html()
