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
    
    
