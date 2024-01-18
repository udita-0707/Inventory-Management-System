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
            price=int(input('Enter buying price'))
            qty=int(input('Enter quantity to be purchased'))
            dor=str(input('enter date(yyyy-mm-dd):'))
            dr=datetime.strptime(dor, "%Y-%m-%d")
            qry1="insert into receive values({},'{}',{},{},'{}')".format(pid,pname,price,qty,dr)
            qry2="update stock set qty=qty+{}".format(qty)
            cursor.execute(qry1)
            cursor.execute(qry2)
            con.commit()
            con.close()
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
                print("available Product Quantity is",i[3])
                print('date of receiving is',i[4])
                print('='*50)
            con.commit()
            con.close()
while True:
    print('MAIN MENU')
    print('1.ADD PURCHASED PRODUCT')
    print('2.GO TO PURCHASING TRANSACTIONS')
    print('3.LOG OUT')
    x = int(input('ENTER CHOICE'))
    if x == 1:
        addprod()    
    elif x==2:
        purchasetrans()    
    elif x==3:
        sys.exit(0)
    else:
        print('invalid choice')
