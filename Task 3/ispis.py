#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi

form = cgi.FieldStorage()

ime = form.getvalue("ime")
radio1 = form.getvalue("radio1")
email = form.getvalue("email")
smjer = form.getvalue("smjer")
zavrsni = form.getvalue("zavrsni")
if(form.getvalue("napomena")):
    napomena = form.getvalue("napomena")
else:
    napomena = "Nema napomene..."

print ("Content-type: text/html\n")
print()

print('''
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <table>
            <tr><td>Ime:</td><td>{ime}</td></tr>
            <tr><td>email:</td><td>{email}</td></tr>
            <tr><td>Status:</td><td>{radio1}</td></tr>
            <tr><td>Smjer:</td><td>{smjer}</td></tr>
            <tr><td>Zavrsni:</td><td>{zavrsni}</td></tr>
            <tr><td>Napomene:</td><td>{napomena}</td></tr>
        </table>
        <a href='prvi.py'>Na pocetak...</a>
    </body>
</html>
'''.format(ime=ime, email=email, radio1=radio1, smjer=smjer, zavrsni=zavrsni, napomena=napomena))

