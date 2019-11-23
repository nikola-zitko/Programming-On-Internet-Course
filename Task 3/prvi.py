#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe
import cgitb
cgitb.enable(display=0, logdir="")

print ("Content-type: text/html\n")
print()

print('''<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action = "drugi.py" method="post">
            <table>
            <tr>
                <td>Ime:</td>
                <td>
                    <input type = "text" name = "ime"/>
                </td>
            </tr>
            <tr>
                <td>Lozinka:</td>
                <td>
                    <input type = "password" name="lozinka" required/>
                </td>
            </tr>
            <tr>
                <td>Ponovi lozinku:</td>
                <td>
                    <input type = "password" name="lozinka2" required/>
                </td>
            </tr>
            <tr>
                <td>
                    <input type = "submit" name="submit" value="Next"/>
                </td>
            </tr>
        </table>
        </form>
    </body>

</html>''')