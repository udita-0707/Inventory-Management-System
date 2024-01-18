from datetime import datetime
import mysql.connector
import sys
def giveconnection():    
    con=mysql.connector.connect(host='localhost',database='practical',password='1234',user='root')
    if con.is_connected():        
        return con    
    else:        
        return None
def addprod():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        pid=int(input('Enter product Id'))        
        pname=input('Enter product name')        
        price=int(input('Enter selling price'))        
        qty=int(input('Enter quantity to be purchased'))        
        dor=str(input('enter date(yyyy-mm-dd):'))        
        dr=datetime.strptime(dor, "%Y-%m-%d")        
        qry1="insert into receive values({},'{}',{},{},'{}')".format(pid,pname,price,qty,dr)        
        qry2="update stock set qty=qty+{} where pid={}".format(qty,pid)        
        cursor.execute(qry1)        
        cursor.execute(qry2)        
        con.commit()        
        con.close()
def removeprod():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('Enter product Id'))        
        qty=int(input('Enter quantity to be sold'))        
        qry = "update issue set qty=qty-{} where pid={}".format(qty,pd)        
        qry2="update stock set qty=qty-{} where pid={}".format(qty,pd)        
        cursor.execute(qry)        
        cursor.execute(qry2)        
        con.commit()        
        con.close()
def displayall():    
        con=giveconnection()    
        if con==None:        
            print('Not connected')    
        else:       
            cursor=con.cursor()        
            qry="select * from stock"        
            cursor.execute(qry)       
            x=cursor.fetchall()        
            for i in x:            
                print("product Id is",i[0])            
                print("product Name is",i[1])            
                print("Available Product Quantity is",i[2])            
                print("product price is",i[3])            
                print('='*50)        
            con.commit()        
            con.close()
def displayrec():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        quan=int(input('enter quantity for checking'))        
        qry="select * from stock where qty<{}".format(quan)        
        cursor.execute(qry)        
        x=cursor.fetchall()        
        for i in x:            
            print("product Id is",i[0])            
            print("product Name is",i[1])            
            print("Available Product Quantity is",i[2])            
            print("product price is",i[3])            
            print('product quantity running out of stock')            
            print('='*50)        
        con.commit()        
        con.close()
def searchrec():    
    con=giveconnection()    
    if con==None:       
         print('Not connected')    
    else:        
        cursor=con.cursor()        
        id=int(input('enter Id to be searched'))        
        qry="select * from stock where pid={}".format(id)        
        cursor.execute(qry)        
        x=cursor.fetchone()        
        print("product Id is",x[0])       
        print("product Name is",x[1])        
        print("Available Product Quantity is",x[2])        
        print("product price is",x[3])        
    con.commit()        
    con.close()
def modifyid():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('enter id to be changed'))        
        new= int(input('enter new id'))        
        qry= "update stock set pid={} where pid={}".format(new,pd)        
        cursor.execute(qry)        
    con.commit()        
    con.close()
def modifyname():    
    con=giveconnection()    
    if con==None:       
         print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('enter id to be changed'))        
        new=input('enter new name')        
        qry="update stock set pname='{}' where pid={}".format(new,pd)        
        cursor.execute(qry)        
    con.commit()        
    con.close()
def modifyprice():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('enter id to be changed'))        
        new= int(input('enter new price'))        
        qry= "update stock set price={} where pid={}".format(new,pd)        
        cursor.execute(qry)        
    con.commit()        
    con.close()
def modifyqty():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('enter id to be changed'))        
        new= int(input('enter new quantity'))        
        qry= "update stock set qty={} where pid={}".format(new,pd)        
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
            print('1.MODIFY PRODUCT ID')            
            print('2.MODIFY PRODUCT NAME')            
            print('3.MODIFY PRODUCT PRICE')            
            print('4.MODIFY PRODUCT QUANTITY')            
            print('5.EXIT')            
            x=int(input('enter your choice'))            
            if x==1:                
                modifyid()            
            elif x==2:                
                modifyname()            
            elif x==3:                
                modifyprice()            
            elif x==4:                
                modifyqty()            
            elif x==5:                
                break            
            else:                
                print('option not available cannot be modified')
def purchasetrans():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor=con.cursor()        
        qry="select * from receive"        
        cursor.execute(qry)        
        x = cursor.fetchall()        
        for i in x:            
            print("product Id is", i[0])            
            print("product Name is", i[1])            
            print("product price is", i[2])            
            print("available Product Quantity is", i[3])            
            print('date of receiving is',i[4])        
        con.commit()        
        con.close()
def selltrans():    
    con = giveconnection()    
    if con == None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        qry = "select * from issue"        
        cursor.execute(qry)        
        x = cursor.fetchall()        
        for i in x:            
            print("product Id is", i[0])            
            print("product Name is", i[1])            
            print("Available Product Quantity is", i[2])            
            print("product price is", i[3])        
        con.commit()        
        con.close()
def transaction():    
    con = giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        while True:            
            print('SUB MENU')            
            print('1.DISPLAY PURCHASING TRANSACTIONS')            
            print('2.DISPLAY SELLING TRANSACTION')            
            print('3.exit')            
            x=int(input('enter your choice'))            
            if x==1:                
                purchasetrans()            
            elif x==2:                
                selltrans()            
            elif x==3:                
                break            
            else:                
                print('invalid choice')
while True:    
    print('MAIN MENU')    
    print('1.ADD PRODUCT')    
    print('2.REMOVE PRODUCT')    
    print('3.DISPLAY ALL PRODUCT RECORDS')    
    print('4.DISPLAY PRODUCT WITH LESS QUANTITY')    
    print('5.SEARCH FOR A SPECIFIC PRODUCT')    
    print('6.MODIFY PRODUCT RECORDS')    
    print('7.GO TO TRANSACTIONS')    
    print('8.LOG OUT')    
    x=int(input('ENTER CHOICE'))    
    if x==1:        
        addprod()    
    elif x == 2:        
        removeprod()    
    elif x == 3:        
        displayall()    
    elif x == 4:        
        displayrec()    
    elif x == 5:        
        searchrec()    
    elif x == 6:        
        modify()    
    elif x == 7:        
        transaction()    
    elif x == 8:        
        sys.exit(0)    
    else:        
        print('invalid choice')