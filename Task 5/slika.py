#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe

import cgi
import _html
import db
import os
from datetime import datetime
from http import cookies


http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)


params = cgi.FieldStorage()
request_type = os.environ.get('REQUEST_METHOD', '')
img = params.getvalue("image")
img_id = params.getvalue("id_img")
image = db.get_image_by_path(img)
image_id = img_id
cookies_object = cookies.SimpleCookie()
cookies_object["image_id"] = image_id
cookies_object["last_visited"] = datetime.now()
cookies_object["image_id"]['expires'] = 12 * 30 * 24 * 60 * 60
db.visit_image(image[0])
print(cookies_object.output())

last_time = get_all_cookies_object.get("last_visited")

if (request_type == "POST"):
  img_id = params.getvalue("id_img")
  success = db.delete_image(img_id)
  if success:  
    print("Location: index.py")

print("Content-type:text/html")
print("")
_html.start_html()
print('<img src="../slike/%s" width=130 height=200>' % image[1])
print('<form method="POST">')
print('<input type="submit" value="DELETE"/>')
print('<input type="hidden" name="id_img" value="%s"/>' % image[0])
print('<input type="hidden" name="image" value="%s"/>' % image[1])
print('</form>')
_html.finish_html()

