#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe

import _html
import subject
import os
import cgi
import printTable
import session

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)
data = session.get_session_data()
print()
_html.start_html()
_html.print_nav()
print('<form action="upisniList.py" method="post">')
subjects = subject.getSubjects()
printTable.printTable(subjects, 3, data)
print('<input type="submit" value="Submit"></form>')

_html.finish_html()
