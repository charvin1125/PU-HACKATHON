from make_csv import make_csv_fn
from sqlite3 import *
import datetime
from datetime import date
conn=connect("Face_details.db")

cur=conn.cursor()
#EMPLOYEE DEPSRTMENT TABLEW
# cur.execute("""create table if not exists dept_details
#                 (
#                     dept_id primary key,
#                     name text,
#                     man_id number,
#                     manager_name text                  
#                 )
#             """)
# conn.commit()

# cur.execute("drop table emp_1")
# conn.commit()

# def add_to_dept(dept_id,dept_name,manager_id,man_name):
    
#     cur.execute(f"insert into dept_details values({dept_id},'{dept_name}','{manager_id}','{man_name}')")
#     conn.commit()

#employee table
cur.execute("""create table if not exists Emp_details
                (
                    id primary key,
                    fname text,
                    lname text,
                    address text,
                    wh_no number,
                    email text
                );
                """)

#employee avaible table
cur.execute("""create table if not exists Emp_avaible
                (
                    series integer primary key, 
                    id number,
                    date text,
                    fname text,
                    lname text,
                    address text,
                    wh_no number,
                    email text
                );
                """)
conn.commit()

# for i in range(1,9):
# cur.execute(f"drop table Emp_details")
# conn.commit()

#employee not aavable tyable


def add_record(id,fname,lname,address,wh_no,email):
   
    cur.execute(f"""insert into Emp_details values
                ({id},'{fname}','{lname}','{address}',{wh_no},'{email}');""")
    conn.commit()

#fetch employee data using face detection
def get_data_by_face(emp_id):
    # print("hi")
    cur.execute(f"""select * from Emp_details where id={emp_id}""")
    emp_data=cur.fetchall()
    # print("hi")
    # print(f"Employee Data:\nId:{emp_data[0]}\nFirst Name:{emp_data[1]}\nLast Name:{emp_data[2]}\nAddress:{emp_data[3]}\nWhatsapp Number:{emp_data[4]}\nEmail:{emp_data[5]}")
    conn.commit()
    return emp_data
#make table for individual emp time and date record

# def get_dept_data(dept_name):
#     cur.execute(f"select man_id,manager_name from dept_details where name='{dept_name}'")
#     data=cur.fetchall()
#     return data

def emp_timing(emp_id):
    currentdatetime=str(datetime.datetime.now()).split(" ")
    datee=currentdatetime[0]
    timee=currentdatetime[1]
    cur.execute(f"""create table if not exists emp_{emp_id}
                (
                    unique_id primary key,
                    date text,
                    arraival_time text,
                    leaving_time text
                )""")
    cur.execute(f"""insert into emp_{emp_id} values
                ( 1,'{datee}','{timee}',"NULL");""")

    conn.commit()
    # conn.close()

#avaible table entry
def add_in_avaible_table(emp_id,datee):
    data=get_data_by_face(emp_id)
    cur.execute(f"select series from Emp_avaible where id={emp_id} and date<>'{datee}'")
    data2=cur.fetchall()
    u_id=0
    print(data2)
    if(len(data2)!=0):
        u_id=data2[-1][0]+1
    if(len(data2)!=0):
        cur.execute(f"""insert into Emp_avaible values({u_id},{data[0][0]},'{data[0][1]}','{datee}','{data[0][2]}','{data[0][3]}',{data[0][4]},'{data[0][5]}')""")
        conn.commit()
    else:
        cur.execute(f"""insert into Emp_avaible values(1,{data[0][0]},'{data[0][1]}','{datee}','{data[0][2]}','{data[0][3]}',{data[0][4]},'{data[0][5]}')""")
        conn.commit()


def remove_from_avaible_table(emp_id,datee):
    data=get_data_by_face(emp_id)
    cur.execute(f"select series from Emp_avaible where id={emp_id} and date<>'{datee}'")
    data2=cur.fetchall()
    u_id=0
    print(data2)
    if(len(data2)!=0):
        u_id=data2[-1][0]
    if(len(data2)!=0):
        cur.execute(f"delete from Emp_avaible where series={u_id}")
        conn.commit()
    else:
        cur.execute(f"delete from Emp_avaible where series=1")
        conn.commit()

csv_data=[]   
def arrival_timeentry(emp_id):
    
    if emp_id not in csv_data:
        csv_data.append(emp_id) 
    
    currentdatetime=str(datetime.datetime.now()).split(" ")
    datee=currentdatetime[0]
    timee=currentdatetime[1]
    data=[]
    cur.execute(f"select * from emp_{emp_id} where date='{datee}'")
    data=cur.fetchall()

    # print(data)
    if(len(data)!=0):
        unique_id=data[-1][0]+1
        # print("hi1")
        if(data[-1][1]!=datee or data[-1][-1]!="NULL"):
            # print("hi2")
            cur.execute(f"""insert into emp_{emp_id} values
                    ( {unique_id},'{datee}','{timee}',"NULL");""")
            add_in_avaible_table(emp_id,datee)
        # print("added")
    else:
        cur.execute(f"select unique_id from emp_{emp_id}")
        data=cur.fetchall()

        unique_id=data[-1][0]+1
        cur.execute(f"""insert into emp_{emp_id} values
                    ( {unique_id},'{datee}','{timee}',"NULL");""")
        add_in_avaible_table(emp_id,datee)
    conn.commit()
    # conn.close()

#leaving time entry
def leaving_timeentry(emp_id):
    currentdatetime=str(datetime.datetime.now()).split(" ")
    datee=currentdatetime[0]
    timee=currentdatetime[1]
   
    data=[]
    
    cur.execute(f"select * from emp_{emp_id} where date='{datee}'")
    data=cur.fetchall()
    
    if(len(data)!=0):
        
        unique_id=data[-1][0] 
        
        if(data[-1][1]==str(datee) or data[-1][-2]!="NULL"):
            
            cur.execute(f"""update emp_{emp_id}
                        set leaving_time='{timee}'
                        where unique_id={unique_id};""")
            remove_from_avaible_table(emp_id,datee)
    else:
        print("hi3")
        cur.execute(f"select unique_id from emp_{emp_id}")
        data=cur.fetchall()

        unique_id=data[-1][0]
        cur.execute(f"""update emp_{emp_id}
                        set leaving_time='{timee}'
                        where unique_id={unique_id};""")
        remove_from_avaible_table(emp_id,datee)
    conn.commit()
    

#make dATA FOR CSV FILE MAKING
file_data=[]
for i in csv_data:
    row=get_data_by_face(i)    
   
    file_data.append(row)
    
make_csv_fn(file_data)
