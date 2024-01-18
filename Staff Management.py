from datetime import datetime
import mysql.connector
import sys
def giveconnection():    
    con=mysql.connector.connect(host='localhost',database='practical',password='1234',user='root')    
    if con.is_connected():        
        return con    
    else:        
        return None
def addstaff():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        sid=int(input('Enter staff Id'))        
        sname=input('enter staff name')        
        doj=str(input('enter date of joining(yyyy-mm-dd):'))        
        dj=datetime.strptime(doj, "%Y-%m-%d")        
        salary=int(input ('enter salary'))        
        qry= "insert into staff values({},'{}','{}',{})".format(sid,sname,dj,salary)        
        cursor.execute(qry)        
        con.commit()        
        con.close()
def delstaff():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        sd=int(input('Enter staff Id'))        
        qry="delete from staff where sid={}".format(sd)        
        cursor.execute(qry)        
        con.commit()        
        con.close()
def modifyid():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        sd=int(input('enter id to be changed'))        
        new= int(input('enter new id'))        
        qry= "update staff set sid={} where sid={}".format(new,sd)        
        cursor.execute(qry)        
        con.commit()        
        con.close()
def modifyname():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        sd=int(input('enter id to be changed'))        
        new=input('enter new name')        
        qry="update staff set sname='{}' where sid={}".format(new,sd)        
        cursor.execute(qry)        
        con.commit()        
        con.close()
def modifysal():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        sd=int(input('enter id to be changed'))        
        new= int(input('enter new salary'))        
        qry= "update staff set salary={} where sid={}".format(new,sd)        
        cursor.execute(qry)        
        con.commit()        
        con.close()
def modify():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        while True:            
            print('SUB MENU')            
            print('1.MODIFY STAFF ID')            
            print('2.MODIFY STAFF NAME')            
            print('3.MODIFY STAFF SALARY')            
            print('4.EXIT')            
            x=int(input('enter your choice'))            
            if x==1:                
                modifyid()            
            elif x==2:                
                modifyname()            
            elif x==3:                
                modifysal()            
            elif x==4:                
                sys.exit(0)           
            else:                
                print('Invalid choice')
while True:    
    print('MAIN MENU')    
    print('1.ADD STAFF')    
    print('2.REMOVE STAFF')    
    print('3,MODIFY STAFF')    
    print('4.LOG OUT')    
    ch=int(input('ENTER YOUR CHOICE'))    
    if ch==1:        
        addstaff()    
    elif ch==2:        
        delstaff()    
    elif ch==3:        
        modify()    
    else:        
        sys.exit(0)
