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
    
    
