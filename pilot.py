def add_item():
    name=input("Enter Item name ")
    query="insert into item(it_name) values('{}')".format(name)
    cur.execute(query)
    con.commit()
    
def transactions_inward():
    item=input("Enter Item id ")
    qty=input("Enter quantity in kgs")
    query="insert into transactions(tr_date,tr_process,tr_qty,tr_itid) values(now(),'i',{},{})".format(qty,item)
    cur.execute(query)
    con.commit()

def transactions_outward():
    item=input("Enter Item id ")
    qty=float(input("Enter quantity in kgs"))
    queryv="select sum(if (tr_process='i', tr_qty, -tr_qty)) as current_stock from transactions where tr_itid={} group by tr_itid".format(item)
    cur.execute(queryv)
    data=cur.fetchall()
    for i in data:
        stock=(i[0])
    fstock=float(stock)
    if fstock>qty:
        query="insert into transactions(tr_date,tr_process,tr_qty,tr_itid) values(now(),'o',{},{})".format(qty,item)
        cur.execute(query)
        con.commit()
    else:
        print("Current stock is ", stock, "less then given outward value")
    
def show_item():
    query="select it_id as serial_number,it_name as item from item;"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)
    
def show_total_inward():
    query="select it_name as name,sum(tr_qty) as inward_quantity from item,transactions where tr_itid=it_id and tr_process='i' group by it_name;"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)
        
def show_total_outward():
    query="select it_name as name,sum(tr_qty) as outward_quantity from item,transactions where tr_itid=it_id and tr_process='o' group by it_name;"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)

def stock():
    query="select it_name as Item, sum(if (tr_process='i', tr_qty, -tr_qty)) as current_stock from transactions,item where tr_itid=it_id group by it_name;"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)

import mysql.connector as sql
con=sql.connect(host='localhost', user='[USERNAME]', password='[PASSWORD]', database='inventory')
if con.is_connected():
    print("Connection to database is successful")
cur=con.cursor()
print("--------------")
print("Welcome to inventory management")

while True:
    print("1. Add item")
    print("2. Transactions")
    print("3. Reports")
    print("4. Quit")
    inp=int(input("What would you like to do today (enter serial number) "))
    if inp==1:
          add_item()
    elif inp==2:
        tr=input("Is it an inward or outward transaction (i/o) ")
        if tr=='i':
            transactions_inward()
        elif tr=='o':
            transactions_outward()
        else:
            print("invalid input  2")
    elif inp==3:
        print("Which report would you like to see")
        print("1. List of all items")
        print("2. Total inward processes")
        print("3. Total outward processes")
        print("4. Current stock")
        tr=int(input("Enter serial number of Report required "))
        if tr==1:
            show_item()
        elif tr==2:
            show_total_inward()
        elif tr==3:
            show_total_outward()
        elif tr==4:
            stock()
        else:
            print("invalid input  3")
    elif inp==4:
        break
    else:
        print("invalid input")
print("Thank you")
