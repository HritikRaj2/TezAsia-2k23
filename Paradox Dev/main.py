def records():
    print("\t------------------------------------")
    print("\tProvide information to login")
    U=input("\t\tenter user=")
    D=input("\t\tenter database name=")
    P=input("\t\tenter password=")
    import mysql.connector as c
    mydb=c.connect(host='localhost', user=U , password=P, database=D)
    cur=mydb.cursor()
    def selection():
        print("\t------------------------------------")
        print("\t##welcome to data saver##")
        print("\tEnter your choice ")
        print("\t1- Create table")
        print("\t2- Insert data in record ")
        print("\t3- Update records")
        print("\t4- Delete data from record")
        print("\t5- To logout")
        ch=int(input("Enter your choice="))
        if ch==1:
           global nm, sn, pn, pr, qt
           print("\t------------------------------------")
           nm = input("\tEnter table name: ")
           sn = input("\tEnter first column: ")
           pn = input("\tEnter second column: ")
           pr = input("\tEnter third column: ")
           qt = input("\tEnter fourth column: ")
           t = "CREATE TABLE %s (%s VARCHAR(20), %s VARCHAR(20), %s VARCHAR(20), %s VARCHAR(20))" % (nm, sn, pn, pr, qt)
           cur.execute(t)
           selection()
        elif ch==2:
            print("\t------------------------------------")
            while True:
                a=input("\t\tenter the name of table=")
                b=eval(input('\t\tenter {} data='.format(sn)))
                c=input("\t\tenter {} data=".format(pn))
                d=eval(input("\t\tenter {} data=" .format(pr)))
                e=eval(input("\tenter {} data=" .format(qt)))
                p="insert into %s values ('%s', '%s', '%s', '%s')" % (a,b,c,d,e)
                cur.execute(p)
                mydb.commit()
                ch=input("press y/Y to enter more data and n/N to back to manu=")
                if ch in 'N/n':
                     selection()
        elif ch==3:
             print("\t------------------------------------")
             k=input("enter name of table=")
             a=input("enter Name of column=")
             b=eval(input("enter new value in that column="))
             m="update %s set %s=%s" % (k,a,b)
             cur.execute(m)
             mydb.commit()
             selection()
        elif ch==4:
             print("\t------------------------------------")
             a=input('enter name of table=')
             b=input("enter name of column where to delete data=")
             c=eval(input("enter data to delete="))
             m="delete from %s where %s=%s" % (a,b,c)
             cur.execute(m)
             mydb.commit()
             selection()
        else:
             records()
    selection()
records()