import mysql.connector as mys
mycon=mys.connect(host='localhost', user='root', passwd='pass', database='mental_health')
if mycon.is_connected():
    print("\n\tSuccessfully Connected")
mycursor = mycon.cursor()

from AddDel import *
from SearchModifyMove import *



def display(table):
    mycursor.execute('select * from '+str(table))
    recordset = mycursor.fetchall()
    for record in recordset:
        record_list = list(record)
        print()
        for r in record_list:
            r = str(r)
            if ord(r[0])>47 and ord(r[0])<58 and len(r) < 4:
                space = 6-len(r)
            elif len(r)<10:
                space = 15-len(r)
            else:
                space = 30-len(r)
            print(r, end=space*" ")
    
    
    
    
coun_create = 'counsellor(Guideno int NOT NULL PRIMARY KEY, Name varchar(25), Position varchar(10), Class varchar(5), Students int, Email varchar(30))'
stu_create = 'students(Admno int NOT NULL PRIMARY KEY, Name varchar(25), Class varchar(5), House varchar(10), Email varchar(30))'
duty_create = 'duty(Guidenum int, Guidename varchar(25), StudentNo int, StudentName varchar(25), StartDate date, Vacancies int, foreign key(Guidenum) references counsellor(Guideno), foreign key(StudentNo) references students(Admno))'
done_create = 'done(Guidenum int, Guidename varchar(25), StudentNo int, StudentName varchar(25), StartDate date, EndDate date)'
creation = [coun_create, stu_create, duty_create, done_create]

create_tables = input("Do you need to create new tables (yes | no)? ")
if (create_tables == 'yes'):
    for c in creation:
        mycursor.execute('create table ' + c)
        mycon.commit()



        
choice = 'yes'
while choice == 'yes':
    
    print("\n\tWelcome to Records. \n\t1. Display All Records.")
    print("\t2. Add New Records.")
    print("\t3. Delete Record.")
    print("\t4. Search for a Record.")
    print("\t5. Modify a Record.")
    print("\t6. Update on Culmination of Duty.")
    
    number = int(input("\tChoose Option: "))
    print()
    
    if number == 1:
        print("\n\tAvailable tables: ")
        print("\tA. Students\n\tB. Counsellors\n\tC. Currently Assigned\n\tD. Previous Records")
        tablechoice = input("\tWhich table do you wish to see? ")
        if tablechoice.upper() == "A":
            display("students")
        elif tablechoice.upper() == "B":
            display("counsellor")
        elif tablechoice.upper() == "C":
            display("duty")
        elif tablechoice.upper() == "D":
            display("done")
        else:
            print("Please select a valid option.")
            
            
    elif number == 2:
        print("\n\tAvailable tables: ")
        print("\tA. Students\n\tB. Counsellors\n\tC. Currently Assigned")
        tablechoice = input("\tWhich table do you wish to add records to? ")
        if tablechoice.upper() == "A":
            add("students")
        elif tablechoice.upper() == "B":
            add("counsellor")
        elif tablechoice.upper() == "C":
            add("duty")
        else:
            print("Please select a valid option.")
            
            
    elif number == 3:
        print("\n\tAvailable tables: ")
        print("\tA. Students\n\tB. Counsellors")
        tablechoice = input("\tWhich table do you wish to delete records from? ")
        if tablechoice.upper() == "A":
            admno = int(input("Enter Student's Admission Number: "))
            delete("students", admno)
        elif tablechoice.upper() == "B":
            couname = input("Enter Name of Counsellor: ")
            delete("counsellor", couname)
        else:
            print("Please select a valid option.")


    elif number == 4:
        print("\n\tAvailable tables: ")
        print("\tA. Students\n\tB. Counsellors \n\tC. Currently Assigned\n\tD. Previous Records")
        tablechoice = input("\tWhich table do you wish to search records from? ")
        if tablechoice.upper() == "A":
            admno = int(input("Enter Student's Admission Number: "))
            search("students", admno)
        elif tablechoice.upper() == "B":
            couname = input("Enter Name of Counsellor: ")
            search("counsellor", couname)
        elif tablechoice.upper() == "C":
            stuno = int(input("Enter Student ID: "))
            search("duty", stuno)
        elif tablechoice.upper() == "D":
            stuno = int(input("Enter Student ID: "))
            search("done", stuno)
        else:
            print("Please select a valid option.")
            
            
    elif number == 5:
        print("\n\tAvailable tables: ")
        print("\tA. Students\n\tB. Counsellors\n\tC. Currently Assigned")
        tablechoice = input("\tWhich table do you wish to modify records from? ")
        if tablechoice.upper() == "A":
            admno = int(input("Enter Student's Admission Number: "))
            modify("students", admno)
        elif tablechoice.upper() == "B":
            bookname = input("Enter Name of Counsellor: ")
            modify("counsellor", bookname)
        else:
            print("Please select a valid option.")
            
            
    elif number == 6:
        studentid = int(input("Enter the Student ID: "))
        done(studentid)
            
    else:
        print("\nInvalid Option - please try again.")
        
    choice = input("\n\tDo you wish to try again ( yes | no )? ")
    
mycursor.close
mycon.close()
