from tkinter import *
from tkinter import ttk
from turtle import end_fill
import sqlite3 as sq
from tkinter import messagebox
from database import *
from datacollect import *
from testmodelfromback import *
from testmodelfromfront import * 
from PIL import ImageTk,Image
import customtkinter as CTk


root = Tk()

big_frame=ttk.Frame(root)
big_frame.pack(fill="both",expand=True)

root.tk.call("source","azure.tcl")
root.tk.call("set_theme","dark")
# 
root.tk.call("set_theme","dark")

#set title
root.title("Employee attendance System")
        
#set display size        
root.geometry("1366x768+0+0")

#declasre variable for get data from UI
id_var = StringVar()
fname_var = StringVar()
lname_var = StringVar()
address = StringVar()
wh_phone = StringVar()
gmailid = StringVar()

# emp_deptid_var = StringVar()
# emp_deptname_var = StringVar()
#navigation bar
navigation_frame = Frame( root,bd=2,relief=SOLID,bg="#638692")
navigation_frame.place(x=0,y=68,width=300,height=700)

#button for chnaging window
    #chnage window function


#style for treeview
style=ttk.Style()
style.configure("mystyle.Treeview",highlightthickness=0,bd=0,font=('Calibar',12))
style.configure("mystyle.Treeview.Heading",font=("Calibar",13,'bold'))
style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
           
#function

def view_data(record_view):
                conn=sq.connect("Face_details.db")

                curobj = conn.cursor()
                curobj.execute(f"select * from Emp_details")
        
                result = curobj.fetchall()
            # if len(result)!=0:
                #  record_view.delete(* record_view.get_children())
                for record in result:
                    record_view.insert("",END,values=record)
        
                conn.commit()
                conn.close()

def view_data_avaible(record_view):
                conn=sq.connect("Face_details.db")

                curobj = conn.cursor()
                curobj.execute("select * from Emp_avaible")
        
                result = curobj.fetchall()
            # if len(result)!=0:
                #  record_view.delete(* record_view.get_children())
                for record in result:
                    record_view.insert("",END,values=record)
        
                conn.commit()
                conn.close()

def view_data_emp(record_view):
                conn=sq.connect("Face_details.db")

                curobj = conn.cursor()
                curobj.execute("select * from emp_1")
        
                result = curobj.fetchall()
            # if len(result)!=0:
                #  record_view.delete(* record_view.get_children())
                for record in result:
                    record_view.insert("",END,values=record)
        
                conn.commit()
                conn.close()

def clear(id_var,fname_var,lname_var,address,wh_phone,gmailid):
                id_var.set("")
                fname_var.set("")
                lname_var.set("")
                address.set("")
                wh_phone.set("")
                gmailid.set("")
        
#database data find using id and name
def search_on_id(eid):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        cur.execute(f"select * from Emp_details where id={eid}")
        data=cur.fetchall()
        return data

def search_on_name(ename):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        cur.execute(f"select * from Emp_details where fname='{ename}'")
        data=cur.fetchall()
        return data

def seacrh_data_from_feild(search_feild,search_component):
    
    if search_feild=="ID":
            eid=int(search_component)
            return search_on_id(eid)
    else:
            return search_on_name(str(search_component))
                    
#employee_activity frame
def seacrh_data_from_feild_employee(search_feild,search_component):
    
    if search_feild=="ID":
            eid=int(search_component)
            return search_on_id_employee(eid)
    else:
            return search_on_name_employee(str(search_component))
                    
def search_on_id_employee(eid):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        data=[]
        try:
            cur.execute(f"select * from emp_{eid}")
            data=cur.fetchall()
            return data
        except:
               return data
def search_on_name_employee(ename):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        cur.execute(f"select id from Emp_details where fname='{ename}'")
        eid=cur.fetchall()
        cur.execute(f"select * from emp_{eid[0][0]}")
        data=cur.fetchall()
        return data

#avaible employee detials
def seacrh_data_from_feild_employee_avaible(search_feild,search_component):
    
    if search_feild=="ID":
            eid=int(search_component)
            return search_on_id_employee_avaible(eid)
    else:
            return search_on_name_employee_avaible(str(search_component))


def search_on_name_employee_avaible(ename):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        cur.execute(f"select id from Emp_details where fname='{ename}'")
        eid=cur.fetchall()
        cur.execute(f"select * from Emp_avaible where id={eid}")
        data=cur.fetchall()
        return data

                    
def search_on_id_employee_avaible(eid):
        conn=sq.connect("Face_details.db")
        cur=conn.cursor()
        data=[]
        try:
            cur.execute(f"select * from Emp_avaible where id={eid}")
            data=cur.fetchall()
            return data
        except:
            return data



def add_face_frame_fn():
            # add_face_frame.pack(expand=1)
                     #add_face frame window

            add_face_frame = Frame(root,bd=2,relief=SOLID)
            add_face_frame.place(x=300,y=0,width=1066,height=768)
            

    
            title = Label(add_face_frame,text="Add Faces Details",font=("Broadway",20,"bold"),bg="black",fg="white")
            title.place(x=0,y=0,width=1066,height=68)


            #take data from user
            emp_manage_frame = Frame(add_face_frame)
            emp_manage_frame.place(x=0,y=68,width=1066,height=700)
            
            
            emp_manage_frame_title = Label(add_face_frame,text="Employee Detail",font=("Broadway",24,"bold"),fg="white")
            emp_manage_frame_title.place(x=0,y=95,width=1066,height=35)
           
            emp_id = Label(emp_manage_frame,text="Employee ID",font=("Arial",16,"bold"),fg="white")
            emp_id.place(x=250,y=100,width=300,height=50)
            inp_id = Entry(emp_manage_frame,text="Employee ID",font=("Arial",16,"bold"),width=25,textvariable= id_var)
            inp_id.place(x=510,y=105,width=250,height=40)

        
            emp_name = Label(emp_manage_frame,text="Employee first name",font=("Arial",16,"bold"),fg="white")
            emp_name.place(x=250,y=160,width=300,height=50)

            inp_name = Entry(emp_manage_frame,text="Employee first Name",font=("Arial",16,"bold"),width=25,textvariable= fname_var)
            inp_name.place(x=510,y=165,width=250,height=40)

        # # last name
            emp_lname = Label(emp_manage_frame,text="Employee Last Name",font=("Arial",16,"bold"),fg="white")
            emp_lname.place(x=250,y=220,width=300,height=50)
        
            l_name = Entry(emp_manage_frame,text="Employee Name",font=("Arial",16,"bold"),width=25,textvariable= lname_var)
            l_name.place(x=510,y=225,width=250,height=40)

        # #address
        
            emp_address = Label(emp_manage_frame,text="Employee Address",font=("Arial",16,"bold"),fg="white")
            emp_address.place(x=250,y=280,width=300,height=50)
        
            e_address = Entry(emp_manage_frame,text="Employee Address",font=("Arial",16,"bold"),width=25,textvariable= address)
            e_address.place(x=510,y=285,width=250,height=40)


        # #wh_number
        
            emp_whnum = Label(emp_manage_frame,text="Employee Number",font=("Arial",16,"bold"),fg="white")
            emp_whnum.place(x=250,y=340,width=300,height=50)
        
            e_whnum = Entry(emp_manage_frame,text="Employee Number",font=("Arial",16,"bold"),width=25,textvariable= wh_phone)
            e_whnum.place(x=510,y=345,width=250,height=40)

        # #gmail 
        
            emp_gmail = Label(emp_manage_frame,text="Employee Gmail",font=("Arial",16,"bold"),fg="white")
            emp_gmail.place(x=250,y=400,width=300,height=50)
        
            e_gmail = Entry(emp_manage_frame,text="Employee Gmail",font=("Arial",16,"bold"),width=25,textvariable= gmailid)
            e_gmail.place(x=510,y=405,width=250,height=40)


            # emp_id = Label(emp_manage_frame,text="Department Id:",font=("Arial",16,"bold"),fg="white")
            # emp_id.place(x=250,y=460,width=300,height=50)
            # inp_id = Entry(emp_manage_frame,text="Department Id:",font=("Arial",16,"bold"),width=25,textvariable= deptid_var)
            # inp_id.place(x=510,y=465,width=250,height=40)

        
            # emp_name = Label(emp_manage_frame,text="Department name",font=("Arial",16,"bold"),fg="white")
            # emp_name.place(x=250,y=520,width=300,height=50)

            # inp_name = Entry(emp_manage_frame,text="deaprtment Name",font=("Arial",16,"bold"),width=25,textvariable= deptname_var)
            # inp_name.place(x=510,y=525,width=250,height=40)

        # call datacollector face 
            def calldatacollector():
                data_id= id_var.get()
                data_name= fname_var.get()
                data_lname= lname_var.get()
                data_address= address.get()
                data_wh= wh_phone.get()
                data_gmail= gmailid.get()
                # data_dept_id=deptid_var.get()
                # data_dept_name=deptname_var.get()
                iamgetaker(data_id,data_name,data_lname,data_address,data_wh,data_gmail)
                clear( id_var, fname_var, lname_var, address, wh_phone, gmailid)
                # view_data(r)
      
      
            add_button = Button(emp_manage_frame,text="Add",bg="#92637b",width=100,height=50,command=calldatacollector,font=("Arial",16,"bold"),fg="black")
            add_button.place(x=410,y=600,width=200,height=50)


# deptid_var = StringVar()
# deptname_var = StringVar()
# managername_var = StringVar()
# manager_id =StringVar()
#department details frame

# def clear_dept(deptid_var,dept_name,man_name,man_id):
#                 deptid_var.set("")
#                 dept_name.set("")
#                 man_name.set("")
#                 man_id.set("")
                # wh_phone.set("")
                # gmailid.set("")
      

# def department_frame_fn():
#             # add_face_frame.pack(expand=1)
#                      #add_face frame window

#             department_frame = Frame(root,bd=2,relief=SOLID)
#             department_frame.place(x=300,y=0,width=1066,height=768)
            
            
    
#             title = Label(department_frame,text="Department Details Details",font=("Broadway",20,"bold"),bg="black",fg="white")
#             title.place(x=0,y=0,width=1066,height=68)


#             #take data from user
#             dept_manage_frame = Frame(department_frame)
#             dept_manage_frame.place(x=0,y=68,width=1066,height=700)
            
            
#             dept_manage_frame_title = Label(department_frame,text="department Detail",font=("Broadway",24,"bold"),fg="white")
#             dept_manage_frame_title.place(x=0,y=95,width=1066,height=35)
           
#             emp_id = Label(dept_manage_frame,text="Department Id:",font=("Arial",16,"bold"),fg="white")
#             emp_id.place(x=250,y=100,width=300,height=50)
#             inp_id = Entry(dept_manage_frame,text="Department Id:",font=("Arial",16,"bold"),width=25,textvariable= deptid_var)
#             inp_id.place(x=510,y=105,width=250,height=40)

        
#             emp_name = Label(dept_manage_frame,text="Department name",font=("Arial",16,"bold"),fg="white")
#             emp_name.place(x=250,y=160,width=300,height=50)

#             inp_name = Entry(dept_manage_frame,text="deaprtment Name",font=("Arial",16,"bold"),width=25,textvariable= deptname_var)
#             inp_name.place(x=510,y=165,width=250,height=40)

#         # # last name
#             emp_lname = Label(dept_manage_frame,text="manager Name",font=("Arial",16,"bold"),fg="white")
#             emp_lname.place(x=250,y=220,width=300,height=50)
        
#             l_name = Entry(dept_manage_frame,text="manager Name",font=("Arial",16,"bold"),width=25,textvariable= managername_var)
#             l_name.place(x=510,y=225,width=250,height=40)

#             man_id = Label(dept_manage_frame,text="manager id:",font=("Arial",16,"bold"),fg="white")
#             man_id.place(x=250,y=280,width=300,height=50)
        
#             man_id_en = Entry(dept_manage_frame,text="manager id",font=("Arial",16,"bold"),width=25,textvariable=manager_id)
#             man_id_en.place(x=510,y=285,width=250,height=40)


#             def calldatacollector():
#                 data_id= deptid_var.get()
#                 data_name= deptname_var.get()
#                 data_mname= manager_id.get()
#                 data_mid= managername_var.get()
                
#                 add_to_dept(data_id,data_name,data_mname,data_mid)
#                 clear_dept(deptid_var,deptname_var,manager_id,managername_var)
#                 # view_data(r)
      
      
#             add_button = Button(dept_manage_frame,text="Add",bg="#92637b",width=100,height=50,command=calldatacollector,font=("Arial",16,"bold"),fg="black")
#             add_button.place(x=410,y=500,width=200,height=50)



#employee activity frame
def employee_activity_frame_fn():
        employee_activity_frame = Frame(root,bd=2,relief=SOLID)
        employee_activity_frame.place(x=300,y=0,width=1066,height=768)

           
            #display data
            #functiuon to display data
            
       
        title = Label(employee_activity_frame,text="Employee Daily Activity",relief=SOLID,font=("Broadway",20,"bold"),bg="black",fg="white")
        title.place(x=0,y=0,width=1066,height=68)
        
        emp_detail_frame = Frame(employee_activity_frame,bd=2,relief=SOLID)
        emp_detail_frame.place(x=0,y=68,width=1066,height=700)

        search = Label(emp_detail_frame,text="Search By",font=("Arial",16,"bold"))
        search.grid(row=0,column=0,pady=0,padx=50,sticky="w")

        #search feild variable
        search_feild=StringVar()
        search_component=StringVar()

        search_drop_down_menu = ttk.Combobox(emp_detail_frame,textvariable=search_feild,font=("Arial",16,"bold"),width=10)
        search_drop_down_menu["values"]=("ID","NAME")
        search_drop_down_menu.grid(row=0,column=1,pady=10,padx=30,sticky="w")
        

        text_search = Entry(emp_detail_frame,bd=5,textvariable=search_component,relief=RIDGE,font=("Arial",16,"bold"))
        text_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")

        def check_feild_are_fill():
            if(search_feild !="" and search_component !=""):
                    result=seacrh_data_from_feild_employee(search_feild.get(),search_component.get())
                    
                    for item in record_view.get_children():
                        record_view.delete(item)
                    if result==[]:
                            record_view.insert("",END,values="No Record ")    
                    else:
                        for record in result:
                            clear(id_var,fname_var,lname_var,address,wh_phone,gmailid)
                            record_view.insert("",END,values=record)
        
        
        searchbtn = Button(emp_detail_frame,text="Search",width=10,command=check_feild_are_fill).grid(row=0,column=3,padx=30,pady=10)
        showall = Button(emp_detail_frame,text="Database",width=10,command=databse_frame_fn).grid(row=0,column=4,padx=35,pady=10)

        record_frame = Frame(emp_detail_frame,bd=4,relief=RIDGE)
        record_frame.place(x=10,y=60,width=1050,height=610)

        scroll_xaxis = Scrollbar(record_frame,orient=HORIZONTAL)
        scroll_yaxis = Scrollbar(record_frame,orient=VERTICAL)

        record_view = ttk.Treeview(record_frame,columns=('Entry','DATE','ARRIVALTIME','LEAVINGTIME'),
                                    style="mystyle.Treeview",
                                   yscrollcommand=scroll_yaxis.set,
                                   xscrollcommand=scroll_xaxis.set,height=50)
        scroll_xaxis.pack(side=BOTTOM,fill=X)
        scroll_yaxis.pack(side=RIGHT,fill=Y)
        scroll_xaxis.config(command=record_view.xview)
        scroll_yaxis.config(command=record_view.yview)

        
        #set tree view font
        style=ttk.Style()
        style.configure("treeview.Heading",font=(None,200))

        record_view.tag_configure("Entry",font=("Arial",10,"bold"))

        record_view.heading("Entry",text="Entry No")
        record_view.heading("DATE",text="Date")
        record_view.heading("ARRIVALTIME",text="Arrival Time")
        record_view.heading("LEAVINGTIME",text="Leaving Time")
            
        record_view['show']="headings"
              
        record_view.column("Entry",width=250)
        record_view.column("DATE",width=250)
        record_view.column("ARRIVALTIME",width=250)
        record_view.column("LEAVINGTIME",width=250)

        record_view.pack(fill=BOTH,expand=1)
        # view_data_emp(record_view)            

def databse_frame_fn():
                 #database_fram window
        database_frame = Frame( root,bd=2,relief=SOLID)
        database_frame.place(x=300,y=0,width=1066,height=768)

        title = Label(database_frame,text="Employee DataBase",relief=SOLID,font=("Broadway",20,"bold"),bg="black",fg="white")
        title.place(x=0,y=0,width=1066,height=68)

            #display data
            #functiuon to display data
            
        emp_detail_frame = Frame(database_frame,bd=2,relief=SOLID)
        emp_detail_frame.place(x=0,y=68,width=1066,height=700)

        search = Label(emp_detail_frame,text="Search By",font=("Arial",16,"bold"))
        search.grid(row=0,column=0,pady=0,padx=50,sticky="w")

        #search feild variable
        search_feild=StringVar()
        search_component=StringVar()

        search_drop_down_menu = ttk.Combobox(emp_detail_frame,textvariable=search_feild,font=("Arial",16,"bold"),width=10)
        search_drop_down_menu["values"]=("ID","NAME")
        search_drop_down_menu.grid(row=0,column=1,pady=10,padx=30,sticky="w")
        

        text_search = Entry(emp_detail_frame,bd=5,textvariable=search_component,relief=RIDGE,font=("Arial",16,"bold"))
        text_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")

        def check_feild_are_fill():
            if(search_feild !="" and search_component !=""):
                    result=seacrh_data_from_feild(search_feild.get(),search_component.get())
                    
                    for item in record_view.get_children():
                        record_view.delete(item)
                    if result==[]:
                            record_view.insert("",END,values="No Record ")    
                    else:
                        for record in result:
                            clear(id_var,fname_var,lname_var,address,wh_phone,gmailid)
                            record_view.insert("",END,values=record)
        
        
        searchbtn = Button(emp_detail_frame,text="Search",width=10,command=check_feild_are_fill).grid(row=0,column=3,padx=30,pady=10)
        showall = Button(emp_detail_frame,text="Avaible",width=10,command=employee_activity_frame_fn).grid(row=0,column=4,padx=35,pady=10)

        record_frame = Frame(emp_detail_frame,bd=4,relief=RIDGE)
        record_frame.place(x=10,y=60,width=1050,height=610)

        scroll_xaxis = Scrollbar(record_frame,orient=HORIZONTAL)
        scroll_yaxis = Scrollbar(record_frame,orient=VERTICAL)

        record_view = ttk.Treeview(record_frame,columns=("ID","NAME",'LastName','Address','WhatsappNumber','G-mail'),
                                   style="mystyle.Treeview",
                                   yscrollcommand=scroll_yaxis.set,
                                   xscrollcommand=scroll_xaxis.set)
        scroll_xaxis.pack(side=BOTTOM,fill=X)
        scroll_yaxis.pack(side=RIGHT,fill=Y)
        scroll_xaxis.config(command=record_view.xview)
        scroll_yaxis.config(command=record_view.yview)

        record_view.tag_configure("tag1",font=("Arial",16,"bold"))

        record_view.heading("ID",text="ID")
        # record_view.heading("Dept_Id",text="Dept_Id")
        # record_view.heading("Dept_name",text="Dept_Name")
        record_view.heading("NAME",text="Name")
        record_view.heading("LastName",text="Last Name")
        record_view.heading("Address",text="Address")
        record_view.heading("WhatsappNumber",text="whatsapp Number")
        record_view.heading("G-mail",text="G-mail")
            
        record_view['show']="headings"
              
        record_view.column("ID",width=50)
        
        # record_view.column("Dept_Id",width=70)
        # record_view.column("Dept_name",width=70)
        record_view.column("NAME",width=70)
        record_view.column("LastName",width=70)
        record_view.column("Address",width=100)
        record_view.column("WhatsappNumber",width=100)
        record_view.column("G-mail",width=100)

        record_view.pack(fill=BOTH,expand=1)
        view_data(record_view)
        

#avaible employee details

def avilable_employee_frame_fn():
        employee_activity_frame = Frame(root,bd=2,relief=SOLID)
        employee_activity_frame.place(x=300,y=0,width=1066,height=768)

           
            #display data
            #functiuon to display data
            
       
        title = Label(employee_activity_frame,text="Available Employees Deatils",relief=SOLID,font=("Broadway",20,"bold"),bg="black",fg="white")
        title.place(x=0,y=0,width=1066,height=68)
        
        emp_detail_frame = Frame(employee_activity_frame,bd=2,relief=SOLID)
        emp_detail_frame.place(x=0,y=68,width=1066,height=700)


        record_frame = Frame(emp_detail_frame,bd=4,relief=RIDGE)
        record_frame.place(x=10,y=0,width=1056,height=700)

        scroll_xaxis = Scrollbar(record_frame,orient=HORIZONTAL)
        scroll_yaxis = Scrollbar(record_frame,orient=VERTICAL)

        record_view = ttk.Treeview(record_frame,columns=("SERIES","ID","DATE","NAME",'LastName','Address','WhatsappNumber','G-mail'),
                                      style="mystyle.Treeview",
                                   yscrollcommand=scroll_yaxis.set,
                                   xscrollcommand=scroll_xaxis.set)
        scroll_xaxis.pack(side=BOTTOM,fill=X)
        scroll_yaxis.pack(side=RIGHT,fill=Y)
        scroll_xaxis.config(command=record_view.xview)
        scroll_yaxis.config(command=record_view.yview)

        record_view.tag_configure("tag1",font=("Arial",16,"bold"))

        record_view.heading("SERIES",text="SERIES")
        record_view.heading("ID",text="ID")
        record_view.heading("DATE",text="DATE")
        record_view.heading("NAME",text="Name")
        record_view.heading("LastName",text="Last Name")
        record_view.heading("Address",text="Address")
        record_view.heading("WhatsappNumber",text="whatsapp Number")
        record_view.heading("G-mail",text="G-mail")
            
        record_view['show']="headings"
              
        record_view.column("SERIES",width=50)
        record_view.column("ID",width=50)
        record_view.column("DATE",width=50)
        record_view.column("NAME",width=100)
        record_view.column("LastName",width=100)
        record_view.column("Address",width=100)
        record_view.column("WhatsappNumber",width=100)
        record_view.column("G-mail",width=100)

        record_view.pack(fill=BOTH,expand=1)
        view_data_avaible(record_view)
        #call main home frame

#message send function
def message_senf_fn():
       
       #make frame for message
       
       message_send_frame = Frame(root,bd=2,relief=SOLID)
       message_send_frame.place(x=300,y=68,width=1066,height=700)

def verification_msg_fn():
        verification_msg_frame = Frame(root,bd=2,relief=SOLID)
        verification_msg_frame.place(x=300,y=68,width=1066,height=700)

        
def log_in_after():
        
    
    navigation_frame = Frame( root,bg="black")
    navigation_frame.place(x=0,y=68,width=300,height=700)
    
    
    title = Label(root,text="FRS",font=("Broadway",32,"bold"),bg="black",fg="white")
    title.place(x=0,y=0,width=300,height=68)

    add_face_frame_fn()

    add_data_button=Button( navigation_frame,text="Add Data",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=add_face_frame_fn)
    add_data_button.place(x=30,y=30,width=240,height=40)

    database_button=Button( navigation_frame,text="Database",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=databse_frame_fn,border=1,relief=SOLID)
    database_button.place(x=30,y=110,width=240,height=40)

    employee_activity_button=Button( navigation_frame,text="Employee Activity",bg="#245b8c",fg="white",font=("Arial",16,"bold"),command=employee_activity_frame_fn,border=1,relief=SOLID)
    employee_activity_button.place(x=30,y=190,width=240,height=40)
   

    aval_employee_button=Button( navigation_frame,text="Available",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=avilable_employee_frame_fn,border=1,relief=SOLID)
    aval_employee_button.place(x=30,y=190,width=240,height=40)
      
    message_button=Button( navigation_frame,text="Message",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=message_senf_fn,border=1,relief=SOLID)
    message_button.place(x=30,y=270,width=240,height=40)

    access_button=Button( navigation_frame,text="Access",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=verification_msg_fn,border=1,relief=SOLID)
    access_button.place(x=30,y=350,width=240,height=40)
    # department_button=Button( navigation_frame,text="Department",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=department_frame_fn,border=1,relief=SOLID)
    # department_button.place(x=30,y=350,width=240,height=40)

    front_camera_button=Button( navigation_frame,text="Front",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=front_camera,border=1,relief=SOLID)
    front_camera_button.place(x=10,y=620,width=130,height=40)

    back_camera_button=Button( navigation_frame,text="Back",bg="#245b8c",fg="white",font=("Arial",12,"bold"),command=back_camera,border=1,relief=SOLID)
    back_camera_button.place(x=150,y=620,width=130,height=40)

    

#login screen with image
login_frame= Frame( root,bg="white")
login_frame.place(x=0,y=0,width=1368,height=768)
bgimg=ImageTk.PhotoImage(Image.open("45-1.jpg").resize((1368,768)))
label1=Label(login_frame,image=bgimg)
label1.pack()

#login_menu
log_in_use_pass_frame=Frame(login_frame,bg="white",width=350,height=300)
log_in_use_pass_frame.place(x=100,y=200)
#username feild
#heading login

login_title = Label(log_in_use_pass_frame,text="LogIn",bg="white",font=("Broadway",22,"bold"),fg="black")
login_title.place(x=100,y=10,width=150)

#heading of the department
dept_heading_title = Label(login_frame,text="Labour,Skill Developement and Employement Department of Gujarat",bg="white",font=("Broadway",15,"bold"),fg="black")
dept_heading_title.place(x=200,y=30,width=900,height=50)

# #declare variavble to stotre username and password
user_name=StringVar()
password=StringVar()
#function for login

# search_feild=StringVar()


# search = Label(log_in_use_pass_frame,text="Search By",font=("Arial",16,"bold"),bg="white",fg="black")
# search.place(x=20,y=60,width=150)

# search_drop_down_menu = ttk.Combobox(log_in_use_pass_frame,textvariable=search_feild,font=("Arial",16,"bold"),width=10,background="white")
# search_drop_down_menu["values"]=("IT","CIVIL","MECHENICAL")
# search_drop_down_menu.place(x=170,y=60,width=150,height=30)
        


username_title = Label(log_in_use_pass_frame,text="Username :",bg="white",font=("Broadway",15,"bold"),fg="black")
username_title.place(x=20,y=100,width=150)

user_name = Entry(log_in_use_pass_frame,text="Username",fg="black",bg="white",font=("Arial",16,"bold"),width=25,textvariable=user_name)
user_name.place(x=170,y=100,width=150)


pass_word_title = Label(log_in_use_pass_frame,text="Password :",bg="white",font=("Broadway",15,"bold"),fg="black")
pass_word_title.place(x=20,y=150,width=150)

pass_word = Entry(log_in_use_pass_frame,text="Password",fg="black",bg="white",font=("Arial",16,"bold"),width=25,textvariable=password)
pass_word.place(x=170,y=150,width=150)



# function for login
def login_process():

        # dept_name=str(search_feild.get())
        # data_name=get_dept_data(dept_name)

        # print(data_name)
        usernames="charvin"
        passwords="1125"
        # for i in data_name:
        # usernames.append(i[1])
        # passwords.append(i[0])
        print(usernames)    
    #    print(str(user_name.get()))    
        if(str(user_name.get()) in usernames) and (str(password.get()) in passwords):
            log_in_after()

Login_button=CTk.CTkButton(log_in_use_pass_frame,text="Login",corner_radius=15,font=("Arial",25),command=login_process,width=200,height=35)
Login_button.pack(padx=75,pady=200)

# log_in_after()

root.mainloop()