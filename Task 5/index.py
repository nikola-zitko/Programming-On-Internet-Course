#!C:\Users\nikol\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe
import _html
import os,cgi
import session
import authentication
import db

if not os.path.isdir('../slike'): #inace ce batiti gresku svaki put kad se post-a
    os.mkdir('../slike')
 
request_type = os.environ.get('REQUEST_METHOD', '')
params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    if "create" in params:
        collection = db.create_collection(params.getvalue("name"))
    elif "upload" in params:
        
        file_item = params["slika"]
        if file_item.filename:
            fn = ('../slike/')
            fn += os.path.basename(file_item.filename)
            db.save_image(file_item, session.get_collection_id(session.get_session_id()))
            open(fn, 'wb').write(file_item.file.read(250000))
            message = 'The file "' + fn + '" was uploaded successfully'
            collection = session.get_collection_id(session.get_session_id())
        
        else:
            message = "No file was uploaded"
    else:
        collection = params.getvalue("collection")
    session.set_collection_id(collection)
    name = session.get_collection_name(session.get_collection_id(collection))
    print("Location: index.py")

print()
_html.start_html()
name = session.get_collection_name(session.get_collection_id(session.get_session_id))

print("Selected collection: " + name)
print("<br>")

print("<form method="'POST'">")
print("<select name="'collection'">")     
for i in db.get_collections():
    print("<option value='"+str(i[0])+"'>"+i[1]+"</option>")
print("</select>")
print("<input type='submit' value='Submit'>")
print("</form>")

print('''<form method="POST">
    New collection:<br>
    <input type="text" name="name">
    <input type="submit" value="Create" name="create">
    </form>
    ''')


c_id = session.get_collection_id(session.get_session_id)
for path in db.get_paths(c_id):
    print('<form action="slika.py" method="POST" target="_blank" style="display: inline;">')
    print('<button type="submit">')
    print('<img  src="../slike/' + path[0] +  '" width=130 height=200>' + path[0])
    print('<input type="hidden" name="image" value="%s"/>' % path[0])
    print('</button>')
    print("</form>")

print('<form enctype="multipart/form-data" method="POST">')
print('<input type="file"  name="slika" accept="image/png, image/jpeg">')
print('<input type="submit" name="upload" value="Upload">')
print('</form>')
print('<br>')
print('<a href="pregled.py">Counter</a>')
print('<br><br>')
print('<a href="logout.py">Logout</a>')
print('<br><br>')
print('<a href="setname.py">Change password</a>')


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    collection = params.getvalue("collection")
    name = session.get_collection_name(session.get_collection_id(collection))

_html.finish_html()