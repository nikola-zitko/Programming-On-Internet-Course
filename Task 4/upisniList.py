#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe

import _html
import subject
import os
import cgi
import printTable
import session
import db

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

print()
data = session.get_session_data()
_html.start_html()
_html.print_nav()

subjects = subject.getSubjects()
printTable.printPaper(subjects, data)

_html.finish_html()
