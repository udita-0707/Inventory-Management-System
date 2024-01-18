from datetime import datetime
import mysql.connector
import sys
def giveconnection():    
    con=mysql.connector.connect(host='localhost',database='practical',password='1234',user='root')    
    if con.is_connected():        
        return con    
    else:        
        return None
def removeprod():    
    con=giveconnection()    
    if con==None:        
        print('Not connected')    
    else:        
        cursor = con.cursor()        
        pd=int(input('Enter product Id'))        
        qty=int(input('Enter quantity to be sold'))        
        qry = "update issue set qty={} where pid={}".format(qty,pd)        
        cursor.execute(qry)        
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
            print("product price is", i[2])            
            print("product Quantity is", i[3])            
            print('='*50)        
        con.commit()        
        con.close()
while True:    
    print('MAIN MENU')    
    print('1.REMOVE SOLD PRODUCT')    
    print('2.GO TO SELLING TRANSACTIONS')    
    print('3.LOG OUT')    
    x = int(input('ENTER CHOICE'))    
    if x==1:        
        removeprod()    
    elif x==2:        
        selltrans()    
    elif x==3:        
        sys.exit(0)    
    else:        
        print('invalid choice')
