import mysql.connector as mys
mycon=mys.connect(host='localhost', user='root', passwd='pass', database='mental_health')
if mycon.is_connected():
    print("\n\tSuccessfully Connected")
mycursor = mycon.cursor()



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
    
    
    

def add(table):
    if table == "students":
        Adno = int(input("Enter Student's Admission Number: "))
        stuname = input("Enter Student's Name: ")
        clas = input("Enter "+stuname+"'s Class (like 09-C): ")
        
        houselist = ['Flames', 'Tornadoes', 'Rockies', 'Rapids']
        house = input("Enter "+stuname+"'s House: ")
        while house not in houselist:
            print("\nInvalid House given. Please re-enter." )
            house = input("Enter "+stuname+"'s House: ") 
        
        email = input("Enter "+stuname+"'s E-mail Address: ")
        query = "insert into students values({0}, '{1}', '{2}', '{3}', '{4}')".format(Adno, stuname, clas, house, email)
        mycursor.execute(query)
        mycon.commit()
        print("Record saved.")
            
        
        
    elif table == "counsellor":
        guideno = int(input("Enter Counsellor's Number: "))
        couname = input("Enter Counsellor's Name: ")
        pos = input(couname+"'s Position: ")
        clas = input("Enter "+couname+"'s Class (like 09-C or NULL): ")
        stuno = int(input("Number of students assigned: "))
        email = input("Enter "+couname+"'s E-mail Address: ")
    
        query = "insert into counsellor values({0}, '{1}', '{2}', '{3}', {4}, '{5}')".format(guideno, couname, pos, clas, stuno, email)
        mycursor.execute(query)
        mycon.commit()
        print("Record saved.")
        
        
        
    elif table == "duty":
        maybeno = int(input("Enter Admission Number: "))
        
        while searchforexistence("students", maybeno) == 0:
            maybeno = int(input("Sorry, this student does not exist in records. Please re-enter: "))
        stuno = maybeno
    
        mycursor.execute("select Name from students where Admno = "+str(stuno))
        stuname = mycursor.fetchone()
        stuname = stuname[0]
        
        maybecounsellor = input("Enter Name of Assigned Counsellor: ")
        
        while searchforexistence("counsellor", maybecounsellor) == 0:
            maybecounsellor = input("Sorry, this counsellor does not exist in records. Please re-enter: ")  
        couname = maybecounsellor
    
        mycursor.execute("select Guideno from counsellor where Name = '"+(couname)+"'")
        guideno = mycursor.fetchone()
        guideno = guideno[0]
        
        mycursor.execute("select Students from counsellor where Name = '"+(couname)+"'")
        occupied = mycursor.fetchone()
        if occupied[0] < 4:
            newoccupied = occupied[0] + 1
            vacan = 4 - newoccupied
            mycursor.execute("update counsellor set Students = "+str(newoccupied)+" where Name = '"+(couname)+"'")
            flag = 1
        else:
            print("Sorry, this counsellor isn't available for duty.")
            vacan = 0
            flag = 0
        
        if flag == 1:
            sdate = input("Enter Starting Date (YYYY-MM-DD): ")
            query = "insert into duty values({0}, '{1}', {2}, '{3}', '{4}', {5})".format(guideno, couname, stuno, stuname, sdate, vacan)
            mycursor.execute(query)
            mycon.commit()
            print("Record saved.")
        elif flag == 0:
            pass
        
    ans = input("\n\tDo you wish to add more records (y/n)? ")
    if ans == 'y':
        add(table)
    elif ans == 'n':
        print()
        display(table)
    
    
    
    
def searchforexistence(table, identity):
    if table == "students":
        mycursor.execute("select * from students where Admno ="+str(identity))
    elif table == "counsellor":
        mycursor.execute("select * from counsellor where Name = '"+(identity)+"'")
    elif table == "duty":
        mycursor.execute("select * from duty where StudentNo ="+str(identity))
    record = mycursor.fetchone()
    if record != None:
        return 1
    else:
        return 0
        
    
    
    
def search(table, identity):
    if searchforexistence(table, identity) == 1:
        if table == "students":
            mycursor.execute('select * from students where Admno ='+str(identity))
        elif table == "counsellor":
            mycursor.execute('select * from counsellor where Name = "'+identity+'"')
        elif table == "duty":
            mycursor.execute('select * from duty where StudentNo = '+str(identity))

        rec = mycursor.fetchone()
        print()
        for r in rec:
            r = str(r)
            if ord(r[0])>47 and ord(r[0])<58 and len(r) < 4:
                space = 6-len(r)
            elif len(r)<10:
                space = 15-len(r)
            else:
                space = 30-len(r)
            print(r, end=space*" ")
                
    else:
        print("\n\tSorry, this record does not exist.")
        
    ans = input("\n\tDo you wish to search for more records (y/n)? ")
    if ans == 'y':
        if table == 'students':
            identity = int(input("\tEnter Admission Number: "))
        elif table == 'counsellor':
            identity = input("\tEnter Counsellor's Name: ")
        elif table == 'duty':
            identity = int(input("\tEnter Student ID: "))
        search(table, identity)
        
            
    
    

def delete(table, identity):
    if searchforexistence(table, identity) == 1:
        if table == "students":
            mycursor.execute('delete from students where Admno ='+str(identity))
        elif table == "counsellor":
            mycursor.execute('delete from counsellor where Name ="'+(identity)+'"')
        mycon.commit()
    else:
        print("\tThis record does not exist.")
        
    ans = input("\n\tDo you wish to delete more records (y/n)? ")
    if ans == 'y':
        if table == 'students':
            identity = int(input("\tEnter Admission Number: "))
        elif table == 'counsellor':
            identity = input("\tEnter Counsellor's Name: ")
        delete(table, identity)
    elif ans == 'n':
        print("\n\tThe new table is: ")
        display(table)
    
    
    
    
def modify(table, identity):
    if searchforexistence(table, identity) == 1:
        if table == "students":
            mycursor.execute('delete from students where admission_no ='+str(identity))
            stuname = input("Enter Student's New Name: ")
            clas = input("Enter "+stuname+"'s Class (like 09-C): ")
            
            houselist = ['Flames', 'Tornadoes', 'Rockies', 'Rapids']
            house = input("Enter "+stuname+"'s House: ")
            while house not in houselist:
                print("\nInvalid House given. Please re-enter." )
                house = input("Enter "+stuname+"'s House: ") 
        
            email = input("Enter "+stuname+"'s E-mail Address: ")
        
            query = "insert into students values({0}, '{1}', '{2}', '{3}', '{4}')".format(identity, stuname, clas, house, email)
            mycursor.execute(query)
            mycon.commit()
            print("Record modified.")
            
        elif table == "counsellor":
            mycursor.execute('select * from counsellor where Name = "'+(identity)+'"')
            rec = mycursor.fetchone()
            guideno = rec[0]
            mycursor.execute('delete from counsellor where Name ="'+(identity)+'"')
            couname = input("Enter Counsellor's New Name: ")
            pos = input(couname+"'s Position: ")
            clas = input("Enter "+couname+"'s Class (like 09-C or NULL): ")
            stuno = int(input("Number of students assigned: "))
            email = input("Enter "+couname+"'s E-mail Address: ")
        
            query = "insert into counsellor values({0}, '{1}', '{2}', '{3}', {4}, '{5}')".format(guideno, couname, pos, clas, stuno, email)
            mycursor.execute(query)
            mycon.commit()
            print("Record saved.")
            
        ans = input("\n\tDo you wish to modify more records (y/n)? ")
        if ans == 'y':
            if table == 'students':
                identity = int(input("\tEnter Admission Number: "))
            elif table == 'counsellor':
                identity = input("\tEnter Counsellor's Name: ")
            search(table, identity)



def done(identity):
    if searchforexistence("students", identity) == 1:
        
        stuno = identity
        
        mycursor.execute("select * from duty where StudentNo = "+str(stuno))
        rec = mycursor.fetchone()
        couno = rec[0]
        couname = rec[1]
        stuname = rec[3]
        sdate = str(rec[4])
        
        mycursor.execute("select curdate()")
        edate = mycursor.fetchone()
        edate = str(edate[0])
        query = "insert into done values({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(couno, couname, stuno, stuname, sdate, edate)
        mycursor.execute(query)
        mycon.commit()
        
        mycursor.execute("update counsellor set Students = Students-1 where Name = '"+(couname)+"'")
        mycon.commit()
        
        mycursor.execute('delete from duty where StudentNo ='+str(identity))
        mycon.commit()
    
    
    
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
