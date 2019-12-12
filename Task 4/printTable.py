#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe
import subject


def printTable(subjects, godina, data):
    print('<table>')
    print('<tr><td>'+ str(godina) +'. Godina</td><td></td></tr><tr><td>Predmet</td><td>Status</td></tr>')
    for key, predmet in subjects.items():
        if(predmet.get('year','n/a') == godina):
            print('<tr><td>')
            subject.printName(key, predmet)
            print('</td><td>')
            subject.displaySubjectRadio(key, data)
            print('</td></tr>')

    print('</table>')


def printPaper(subjects, data):
      
    suma = 0
    print('<table>')
    print('''<tr><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>''')
    for key, predmet in subjects.items():
        if(data[key] == "enr"):
            suma += predmet.get('ects', 'n/a')
        print('<tr><td>')
        subject.printName(key, predmet)
        print('</td><td>')
        print(subject.status_names.get(data[key]))
        print('</td><td>')
        print(predmet.get('ects','n/a'))
        print('</td></tr>')
        
    print('<tr><td></td><td>Ukupno bodova:</td><td>' + str(suma) + '</td></tr>')    
    print('</table>')
    
