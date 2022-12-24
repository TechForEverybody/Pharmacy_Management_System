from logging import info
from tkinter import *
import mysql.connector

def connect():
    global con,query
    con=mysql.connector.connect(username='root',password="",host='127.0.0.1',port=3307,database='')
    print(con)
    query=con.cursor()
# connect()



sk=Tk()
sk.geometry("1900x1050")
sk.title("Pharmacy Management")

background=PhotoImage(file='./bg.png')
bg=Canvas(sk,width=1900,height=950)
bg.pack(fill=BOTH,expand=True)
bg.create_image(0,0,image=background,anchor='nw')

label=Label(sk,text="Pharmacy Management",font="ROMEN 50 bold")
label.place(y=0,x=600)
# sk.attributes('-alpha',0.5)
# sk.wm_attributes("-transparentcolor", 'grey')

frame_parent=Frame(sk,bg="White")
child_frame=Frame(frame_parent)

input_frame=Frame(sk)

pdt_id=StringVar()
pdt_name=StringVar()
pdt_manfacture=StringVar()
expiry_date=StringVar()
count=StringVar()
price=StringVar()
used_for=StringVar()
sort_sql=""
sort_type=1


def sort_the_data_by_id(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by pdt_id desc"
        sort_type=0
    else:
        sql=sort_sql+" order by pdt_id asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass
def sort_the_data_by_name(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by pdt_name desc"
        sort_type=0
    else:
        sql=sort_sql+" order by pdt_name asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass
def sort_the_data_by_munfacture(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by pdt_manfacture desc"
        sort_type=0
    else:
        sql=sort_sql+" order by pdt_manfacture asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass
def sort_the_data_by_expiry_date(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by expiry_date desc"
        sort_type=0
    else:
        sql=sort_sql+" order by expiry_date asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass
def sort_the_data_by_count(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by count desc"
        sort_type=0
    else:
        sql=sort_sql+" order by count asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass
def sort_the_data_by_price(event):
    global sort_sql,sort_type
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    if sort_type==1:
        sql=sort_sql+" order by price desc"
        sort_type=0
    else:
        sql=sort_sql+" order by price asc"
        sort_type=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
    pass

def view_all(event):
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    global sort_sql
    sql="SELECT * FROM pharmacy_managaement"
    sort_sql=sql
    query.execute(sql)
    result=query.fetchall()
    print(result)
    i=1
    for data in result:
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3
        pass


def searchevent(enevt):
    global sort_sql
    for widgets in child_frame.winfo_children():
        widgets.destroy()
    global pdt_id,pdt_name,pdt_manfacture,expiry_date,used_for;
    sql="SELECT * FROM pharmacy_managaement WHERE "
    concat=0
    if pdt_id.get()!="":
        sql=sql+" pdt_id={}".format(pdt_id.get())
        concat=1
    if pdt_name.get()!="":
        if concat==1:
            sql=sql+" and"
        sql=sql+" pdt_name like '%{}%'".format(pdt_name.get())
        concat=1
    if pdt_manfacture.get()!="":
        if concat==1:
            sql=sql+" and"
        sql=sql+" pdt_manfacture like '%{}%'".format(pdt_manfacture.get())
        concat=1
    if expiry_date.get()!="":
        if concat==1:
            sql=sql+" and"
        sql=sql+" expiry_date='{}'".format(expiry_date.get())
        concat=1
    if used_for.get()!="":
        if concat==1:
            sql=sql+" and"
        sql=sql+" used_for like '%{}%'".format(used_for.get())
        concat=1
    i=1
    query.execute(sql)
    result=query.fetchall()
    print(result)
    sort_sql=sql
    for data in result:
        print(i)
        label=Label(child_frame,text=data[0],bd=0).place(x=10,y=10*i)
        label=Label(child_frame,text=data[1],bd=0).place(x=100,y=10*i)
        label=Label(child_frame,text=data[2],bd=0).place(x=300,y=10*i)
        label=Label(child_frame,text=data[3],bd=0).place(x=520,y=10*i)
        label=Label(child_frame,text=data[4],bd=0).place(x=670,y=10*i)
        label=Label(child_frame,text=data[5],bd=0).place(x=850,y=10*i)
        label=Label(child_frame,text=data[6],bd=0).place(x=1000,y=10*i)
        i=i+3

    
def search(event):
    for widgets in input_frame.winfo_children():
            widgets.destroy()
    input_frame.place_forget()
    input_frame.place(x=150,y=250,height=400,width=400)
    label=Label(input_frame,text="Enter data here",font="ROMEN 20 bold").place(x=100,y=5)
    label=Label(input_frame,text="Enter id").place(x=10,y=70)
    entry=Entry(input_frame,textvariable=pdt_id).place(x=150,y=70)
    label=Label(input_frame,text="Enter name").place(x=10,y=130)
    entry=Entry(input_frame,textvariable=pdt_name).place(x=150,y=130)
    label=Label(input_frame,text="Enter manfacture").place(x=10,y=190)
    entry=Entry(input_frame,textvariable=pdt_manfacture).place(x=150,y=190)
    label=Label(input_frame,text="Enter Expiry date").place(x=10,y=250)
    entry=Entry(input_frame,textvariable=expiry_date).place(x=150,y=250)
    label=Label(input_frame,text="used for").place(x=10,y=310)
    entry=Entry(input_frame,textvariable=used_for).place(x=150,y=310)
    button10=Button(input_frame,text="Search",font="ROMEN 12 bold",bg="aqua")
    button10.bind("<Button-1>",searchevent)
    button10.place(x=160,y=350)
    pass


def insertevent(event):
    print(event)
    global pdt_id,pdt_name,pdt_manfacture,expiry_date,used_for,count,price;
    if pdt_id.get()!="" and pdt_name.get()!="" and pdt_manfacture.get()!="" and expiry_date.get()!="" and count.get()!="" and price.get()!="" and used_for.get()!="":
        sql="INSERT INTO pharmacy_managaement Values({},'{}','{}','{}',{},{},'{}')".format(pdt_id.get(),pdt_name.get(),pdt_manfacture.get(),expiry_date.get(),count.get(),price.get(),used_for.get(),)
        query.execute(sql)
        con.commit()
    else:
        print("Please Fill all the values")
    pass




def insert(event):
    for widgets in input_frame.winfo_children():
        widgets.destroy()
    input_frame.place_forget()
    input_frame.place(x=150,y=250,height=520,width=400)
    label=Label(input_frame,text="Enter data here",font="ROMEN 20 bold").place(x=100,y=5)
    label=Label(input_frame,text="Enter id").place(x=10,y=70)
    entry=Entry(input_frame,textvariable=pdt_id).place(x=150,y=70)
    label=Label(input_frame,text="Enter name").place(x=10,y=130)
    entry=Entry(input_frame,textvariable=pdt_name).place(x=150,y=130)
    label=Label(input_frame,text="Enter manfacture").place(x=10,y=190)
    entry=Entry(input_frame,textvariable=pdt_manfacture).place(x=150,y=190)
    label=Label(input_frame,text="Enter Expiry date").place(x=10,y=250)
    entry=Entry(input_frame,textvariable=expiry_date).place(x=150,y=250)
    label=Label(input_frame,text="Enter price").place(x=10,y=310)
    entry=Entry(input_frame,textvariable=price).place(x=150,y=310)
    label=Label(input_frame,text="Enter count").place(x=10,y=370)
    entry=Entry(input_frame,textvariable=count).place(x=150,y=370)
    label=Label(input_frame,text="used for").place(x=10,y=430)
    entry=Entry(input_frame,textvariable=used_for).place(x=150,y=430)
    button11=Button(input_frame,text="Insert",font="ROMEN 12 bold",bg="aqua")
    button11.bind("<Button-1>",insertevent)
    button11.place(x=160,y=470)



def updateevent(event):
    global pdt_id,pdt_name,pdt_manfacture,expiry_date,used_for,count,price;
    sql="UPDATE pharmacy_managaement SET  "
    concat=0
    if pdt_id.get()!="":
        if pdt_name.get()!="":
            sql=sql+" pdt_name='{}'".format(pdt_name.get())
            concat=1
        if pdt_manfacture.get()!="":
            if concat==1:
                sql=sql+" ,"
            sql=sql+" pdt_manfacture='{}'".format(pdt_manfacture.get())
            concat=1
        if expiry_date.get()!="":
            if concat==1:
                sql=sql+" ,"
            sql=sql+" expiry_date='{}'".format(expiry_date.get())
            concat=1
        if price.get()!="":
            if concat==1:
                sql=sql+" ,"
            sql=sql+" price={}".format(price.get())
            concat=1
        if count.get()!="":
            if concat==1:
                sql=sql+" ,"
            sql=sql+" count=count+{}".format(count.get())
            concat=1
        sql=sql+" WHERE pdt_id={}".format(pdt_id.get())
        print(sql)
        query.execute(sql)
        con.commit()
    else:
        print("id is neccesert=y to chenge data")


def update(event):
    for widgets in input_frame.winfo_children():
            widgets.destroy()
    input_frame.place_forget()
    input_frame.place(x=150,y=250,height=480,width=400)
    label=Label(input_frame,text="Enter data here",font="ROMEN 20 bold").place(x=100,y=5)
    label=Label(input_frame,text="Enter id").place(x=10,y=70)
    entry=Entry(input_frame,textvariable=pdt_id).place(x=150,y=70)
    label=Label(input_frame,text="Enter name").place(x=10,y=130)
    entry=Entry(input_frame,textvariable=pdt_name).place(x=150,y=130)
    label=Label(input_frame,text="Enter manfacture").place(x=10,y=190)
    entry=Entry(input_frame,textvariable=pdt_manfacture).place(x=150,y=190)
    label=Label(input_frame,text="Enter Expiry date").place(x=10,y=250)
    entry=Entry(input_frame,textvariable=expiry_date).place(x=150,y=250)
    label=Label(input_frame,text="Enter price").place(x=10,y=310)
    entry=Entry(input_frame,textvariable=price).place(x=150,y=310)
    label=Label(input_frame,text="Enter count").place(x=10,y=370)
    entry=Entry(input_frame,textvariable=count).place(x=150,y=370)
    button12=Button(input_frame,text="Update",font="ROMEN 12 bold",bg="aqua")
    button12.bind("<Button-1>",updateevent)
    button12.place(x=160,y=420)


def deleteevent(event):
    global pdt_id,pdt_name,pdt_manfacture,expiry_date,used_for,count,price;
    if pdt_id.get()!="" and count.get()!="":
        sql="SELECt count"
    pass



def delete(event):
    for widgets in input_frame.winfo_children():
            widgets.destroy()
    input_frame.place_forget()
    input_frame.place(x=150,y=250,height=250,width=400)
    label=Label(input_frame,text="Enter data here",font="ROMEN 20 bold").place(x=100,y=5)
    label=Label(input_frame,text="Enter id").place(x=10,y=70)
    entry=Entry(input_frame,textvariable=pdt_id).place(x=150,y=70)
    label=Label(input_frame,text="count").place(x=10,y=130)
    entry=Entry(input_frame,textvariable=count).place(x=150,y=130)
    button13=Button(input_frame,text="Delete",font="ROMEN 12 bold",bg="aqua")
    button13.bind("<Button-1>",deleteevent)
    button13.place(x=160,y=200)


button1=Button(sk,text="Insert",font="ROMEN 15 bold")
button1.bind("<Button-1>",insert)
button1.place(x=650,y=120)
button2=Button(sk,text="Update",font="ROMEN 15 bold")
button2.bind("<Button-1>",update)
button2.place(x=850,y=120)
button3=Button(sk,text="Delete",font="ROMEN 15 bold")
button3.bind("<Button-1>",delete)
button3.place(x=1050,y=120)
button4=Button(sk,text="Search",font="ROMEN 15 bold")
button4.bind("<Button-1>",search)
button4.place(x=1250,y=120)
button5=Button(sk,text="View all",font="ROMEN 15 bold")
button5.bind("<Button-1>",view_all)
button5.place(x=1450,y=120)


button21=Button(frame_parent,text="productID",background="White",bd=0)
button21.bind('<Button-1>',sort_the_data_by_id)
button21.place(x=10,y=10)
button22=Button(frame_parent,text="Product Name",background="White",bd=0)
button22.bind('<Button-1>',sort_the_data_by_name)
button22.place(x=100,y=10)
button23=Button(frame_parent,text="Product Manfacturer",background="White",bd=0)
button23.bind('<Button-1>',sort_the_data_by_munfacture)
button23.place(x=300,y=10)
button24=Button(frame_parent,text="Expiry Date",background="White",bd=0)
button24.bind('<Button-1>',sort_the_data_by_expiry_date)
button24.place(x=520,y=10)
button25=Button(frame_parent,text="Count",background="White",bd=0)
button25.bind('<Button-1>',sort_the_data_by_count)
button25.place(x=670,y=10)
button26=Button(frame_parent,text="price",background="White",bd=0)
button26.bind('<Button-1>',sort_the_data_by_price)
button26.place(x=850,y=10)
button27=Button(frame_parent,text="Used For",background="White",bd=0)
# button27.bind('<Button-1>',)
button27.place(x=1000,y=10)



child_frame.place(x=0,y=40,height=650,width=1250)
frame_parent.place(x=600,y=200,height=700,width=1250)










sk.mainloop()
