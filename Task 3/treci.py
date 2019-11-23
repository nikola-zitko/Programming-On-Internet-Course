#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi

form = cgi.FieldStorage()

ime = form.getvalue("ime")
radio1 = form.getvalue("radio1")
email = form.getvalue("email")
smjer = form.getvalue("smjer")
if(form.getvalue("zavrsni")):
    zavrsni = form.getvalue("zavrsni")
else:
    zavrsni = "Ne"
print ("Content-type: text/html\n")
print()

print('''<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
       
        <form action = "ispis.py" method="post">
            <table>
                <tr>
                    <td>Napomene:</td>
                    <td><textarea rows="4" cols="30" name="napomena"></textarea></td>
                </tr>
                    <input type="hidden" name="ime" value="{ime}">
                    <input type="hidden" name="email" value="{email}">
                    <input type="hidden" name="radio1" value="{radio1}">
                    <input type="hidden" name="smjer" value="{smjer}">
                    <input type="hidden" name="zavrsni" value="{zavrsni}">
                <tr>
                    <td><input type="submit" value="Next" name="treci"/></td>
                </tr>
            </table>
        </form>
    </body>
</html>'''.format(ime=ime, email=email, radio1=radio1, smjer=smjer, zavrsni=zavrsni))