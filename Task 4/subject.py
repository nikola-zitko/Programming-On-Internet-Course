#!C:\Users\SwiftNICK\AppData\Local\Programs\Python\Python38-32\python.exe
import session
subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    }
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    }

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
}

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
}

def getSubjects():
    return subjects
def getNames():
    return status_names

def printName(key, predmet):
    print(predmet.get('name', 'n/a') + '&nbsp;')


def displaySubjectRadio(key, data):
    if(data.get(key,"not") == "not"):
            print('<input type="radio" name="' + key + '" value=''not'' checked>' + status_names.get('not'))
            print('<input type="radio" name="' + key + '" value=''enr''>' + status_names.get('enr'))
            print('<input type="radio" name="' + key + '" value=''pass''>' + status_names.get('pass'))
    elif(data[key] == "enr"):
            print('<input type="radio" name="' + key + '" value=''not''>' + status_names.get('not'))
            print('<input type="radio" name="' + key + '" value=''enr'' checked>' + status_names.get('enr'))
            print('<input type="radio" name="' + key + '" value=''pass''>' + status_names.get('pass'))
    elif(data[key] == "pass"):
            print('<input type="radio" name="' + key + '" value=''not''>' + status_names.get('not'))
            print('<input type="radio" name="' + key + '" value=''enr''>' + status_names.get('enr'))
            print('<input type="radio" name="' + key + '" value=''pass'' checked>' + status_names.get('pass'))
    else:
        print('<input type="radio" name="' + key + '" value=''not'' >' + status_names.get('not'))
        print('<input type="radio" name="' + key + '" value=''enr''>' + status_names.get('enr'))
        print('<input type="radio" name="' + key + '" value=''pass''>' + status_names.get('pass'))
    