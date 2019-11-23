#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
import os

form = cgi.FieldStorage()

ime = form.getvalue("ime")
lozinka = form.getvalue("lozinka")
lozinka2 = form.getvalue("lozinka2")

if(lozinka != lozinka2):
    print("Location: prvi.py")

print ("Content-type: text/html\n")
print()

print('''<html>
    <head>
        
        <meta charset="utf-8">
    </head>
    <body>
        <form action="treci.py" method="post">
        <table>
            <tr>
                <td>Status:</td>
                <td>
                    Redovan: <input type="radio" name="radio1" value="Redovan" checked="checked"/> Izvanredan:<input type="radio" name="radio1" value="Izvanredan"/>
                </td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td>
                    <input type = "email" name = "email"/>
                </td>
            </tr>
            <tr>
                <td>Smjer:</td>
                <td>
                    <select name="smjer">
                        <option value="Programiranje">Programiranje</option>
                        <option value="Baze Podataka">Baze Podataka</option>
                        <option value="Racunalne mreze">Racunalne mreze</option>
                        <option value="Informacijski sustavi">Informacijski sustavi</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Zavrsni:</td>
                <td><input type="checkbox" name="zavrsni" value="Da"/></td>
            </tr>
            <input type="hidden" name="ime" value="{ime}">
            <tr>
                <td>
                    <input type = "submit" value = "Next" name="drugi"/>
                </td>
            </tr>
        </table>
        </form>
    </body>

</html>
'''.format(ime=ime, lozinka=lozinka, lozinka2=lozinka2))