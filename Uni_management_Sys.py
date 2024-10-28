



def add_stud():
    def submit_add():
        id=id_val.get()
        name =name_val.get()
        mobile = mob_val.get()
        email = mail_val.get()
        dob = dob_val.get()
        gender =gen_val.get()
        address = add_val.get()
        added_time = time.strftime("%H:%M:%S")
        added_date =time.strftime("%d/%m/%y")
        try:
            strr = 'insert into student_data1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,added_date,added_time))
            con.commit()
            res =messagebox.askyesnocancel('notifications','Id {} Name {} Added successfully.Do you want to clear the form?'.format(id,name),parent=add_root)
            if(res==True):       
                     id_val.set('')
                     name_val.set('')
                     mob_val.set('')
                     mail_val.set('')
                     dob_val.set('')
                     gen_val.set('')
                     add_val.set('')
            else:
                  pass  

        except:
            messagebox.showerror('notifications','Id already Exist Try again!',parent=add_root)
        strr ='select * from student_data1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        std_table.delete(*std_table.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            std_table.insert('',END,values=vv)

    add_root = Toplevel(master= data_entry_frame)
    add_root.grab_set()
    add_root.geometry('470x470+220+200')
    add_root.title('University Mangement System')
    add_root.config(bg='blue')
    add_root.resizable(False,False)
    # Student Labels 
    id_label = Label(add_root,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    id_label.place(x=10,y=10)

    name_label = Label(add_root,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    name_label.place(x=10,y=70)
    
    mob_label = Label(add_root,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mob_label.place(x=10,y=130)
    
    mail_label = Label(add_root,text='Enter E-Mail : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mail_label.place(x=10,y=190)
    
    add_label = Label(add_root,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    add_label.place(x=10,y=250)
    
    gen_label = Label(add_root,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gen_label.place(x=10,y=310)
    
    dob_label = Label(add_root,text='Enter DOB : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dob_label.place(x=10,y=370)

# Add Student Entries
    id_val =StringVar()
    name_val =StringVar()
    mob_val =StringVar()
    mail_val =StringVar()
    dob_val =StringVar()
    gen_val =StringVar()
    add_val =StringVar()


    id_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable= id_val)
    id_entry.place(x=250,y=10)
    
    name_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=name_val)
    name_entry.place(x=250,y=70)

    mob_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=mob_val)
    mob_entry.place(x=250,y=130)

    mail_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=mail_val)
    mail_entry.place(x=250,y=190)

    add_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=add_val)
    add_entry.place(x=250,y=250)

    gen_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=gen_val)
    gen_entry.place(x=250,y=310)

    dob_entry = Entry(add_root,font=('roman',15,'bold'),bd=5,textvariable=dob_val)
    dob_entry.place(x=250,y=370)

    submit_btn = Button(add_root,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submit_add)
    submit_btn.place(x=150,y=420)


    add_root.mainloop()

def search_stud():
    def submit_search():
        id=id_val.get()
        name =name_val.get()
        mobile = mob_val.get()
        email = mail_val.get()
        dob = dob_val.get()
        gender =gen_val.get()
        address = add_val.get()
        added_date =time.strftime("%d/%m/%y")
        if(id!= ''):
            strr = 'select *from student_data1 where id = %s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        
        if(name!= ''):
            strr = 'select *from student_data1 where name = %s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        
        elif(mobile!= ''):
            strr = 'select *from student_data1 where mobile = %s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)

        elif(email!= ''):
            strr = 'select *from student_data1 where email= %s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        elif(dob!= ''):
            strr = 'select *from student_data1 where dob = %s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        elif(gender!= ''):
            strr = 'select *from student_data1 where gender = %s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        elif(address!= ''):
            strr = 'select *from student_data1 where address = %s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)
        elif(added_date!= ''):
            strr = 'select *from student_data1 where added_date = %s'
            mycursor.execute(strr,(added_date))
            datas = mycursor.fetchall()   
            std_table.delete(*std_table.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                std_table.insert('',END,values=vv)

    search_root = Toplevel(master= data_entry_frame)
    search_root.grab_set()
    search_root.geometry('470x540+220+200')
    search_root.title('University Mangement System')
    search_root.config(bg='red3')
    search_root.resizable(False,False)
    # Student Labels 
    id_label = Label(search_root,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    id_label.place(x=10,y=10)

    name_label = Label(search_root,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    name_label.place(x=10,y=70)
    
    mob_label = Label(search_root,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mob_label.place(x=10,y=130)
    
    mail_label = Label(search_root,text='Enter E-Mail : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mail_label.place(x=10,y=190)
    
    add_label = Label(search_root,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    add_label.place(x=10,y=250)
    
    gen_label = Label(search_root,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gen_label.place(x=10,y=310)
    
    dob_label = Label(search_root,text='Enter DOB : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dob_label.place(x=10,y=370)

    date_label = Label(search_root,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    date_label.place(x=10,y=430)

# Add Student Entries
    id_val =StringVar()
    name_val =StringVar()
    mob_val =StringVar()
    mail_val =StringVar()
    dob_val =StringVar()
    gen_val =StringVar()
    add_val =StringVar()
    date_val =StringVar()


    id_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=id_val)
    id_entry.place(x=250,y=10)
    
    name_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=name_val)
    name_entry.place(x=250,y=70)

    mob_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=mob_val)
    mob_entry.place(x=250,y=130)

    mail_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=mail_val)
    mail_entry.place(x=250,y=190)

    add_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=add_val)
    add_entry.place(x=250,y=250)

    gen_entry = Entry(search_root,font=('roman',15,'bold'),bd=5,textvariable=gen_val)
    gen_entry.place(x=250,y=310)

    dob_entry = Entry(search_root,font=('centaur',15,'bold'),bd=5,textvariable=dob_val)
    dob_entry.place(x=250,y=370)

    date_entry = Entry(search_root,font=('centaur',15,'bold'),bd=5,textvariable=date_val)
    date_entry.place(x=250,y=430)
    
    submit_btn = Button(search_root,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submit_search)
    submit_btn.place(x=150,y=490)


    search_root.mainloop()


def dlt_stud():
    cc = std_table.focus()
    content = std_table.item(cc)
    pp = content ['values'][0]
    strr ='delete from student_data1 where id =%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully.'.format(pp))
    strr = 'select *from student_data1 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()   
    std_table.delete(*std_table.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        std_table.insert('',END,values=vv)

def upd_stud():
    

    def submit_update():
        id=id_val.get()
        name =name_val.get()
        mobile = mob_val.get()
        email = mail_val.get()
        dob = dob_val.get()
        gender =gen_val.get()
        address = add_val.get()
        date =date_val.get()
        time = time_val.get()

        strr = ' update student_data1 set name=%s,mobile=%s,email=%s,dob=%s,gender=%s,address=%s,date =%s,time=%s where id =%s'
        mycursor.execute(strr,(name,mobile,email,dob,gender,address,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Updated Successfully .'.format(id),parent=upd_root)
        strr = 'select *from student_data1 '
        mycursor.execute(strr)
        datas = mycursor.fetchall()   
        std_table.delete(*std_table.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            std_table.insert('',END,values=vv)

    upd_root = Toplevel(master= data_entry_frame)
    upd_root.grab_set()
    upd_root.geometry('470x590+220+160')
    upd_root.title('University Mangement System')
    upd_root.config(bg='red3')
    upd_root.resizable(False,False)
    # Student Labels 
    id_label = Label(upd_root,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    id_label.place(x=10,y=10)

    name_label = Label(upd_root,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    name_label.place(x=10,y=70)
    
    mob_label = Label(upd_root,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mob_label.place(x=10,y=130)
    
    mail_label = Label(upd_root,text='Enter E-Mail : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mail_label.place(x=10,y=190)
    
    add_label = Label(upd_root,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    add_label.place(x=10,y=250)
    
    gen_label = Label(upd_root,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gen_label.place(x=10,y=310)
    
    dob_label = Label(upd_root,text='Enter DOB : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dob_label.place(x=10,y=370)

    date_label = Label(upd_root,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    date_label.place(x=10,y=430)

    time_label = Label(upd_root,text='Enter Time : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    time_label.place(x=10,y=490)

# Add Student Entries
    id_val =StringVar()
    name_val =StringVar()
    mob_val =StringVar()
    mail_val =StringVar()
    dob_val =StringVar()
    gen_val =StringVar()
    add_val =StringVar()
    date_val =StringVar()
    time_val =StringVar()

    id_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=id_val)
    id_entry.place(x=250,y=10)
    
    name_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=name_val)
    name_entry.place(x=250,y=70)

    mob_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=mob_val)
    mob_entry.place(x=250,y=130)

    mail_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=mail_val)
    mail_entry.place(x=250,y=190)

    add_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=add_val)
    add_entry.place(x=250,y=250)

    gen_entry = Entry(upd_root,font=('roman',15,'bold'),bd=5,textvariable=gen_val)
    gen_entry.place(x=250,y=310)

    dob_entry = Entry(upd_root,font=('centaur',15,'bold'),bd=5,textvariable=dob_val)
    dob_entry.place(x=250,y=370)

    date_entry = Entry(upd_root,font=('centaur',15,'bold'),bd=5,textvariable=date_val)
    date_entry.place(x=250,y=430)

    time_entry = Entry(upd_root,font=('centaur',15,'bold'),bd=5,textvariable=time_val)
    time_entry.place(x=250,y=490)

    submit_btn = Button(upd_root,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submit_update)
    submit_btn.place(x=150,y=540)

    cc =std_table.focus()
    content = std_table.item(cc)
    pp = content['values']
    if (len(pp)!=0):
        id_val.set(pp[0])
        name_val.set(pp[1])
        mob_val.set(pp[2])
        mail_val.set(pp[3])
        dob_val.set(pp[4])
        gen_val.set(pp[5])
        add_val.set(pp[6])
        date_val.set(pp[7])
        time_val.set(pp[8])

    upd_root.mainloop()


def all_stud():
        strr = 'select *from student_data1 '
        mycursor.execute(strr)
        datas = mycursor.fetchall()   
        std_table.delete(*std_table.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            std_table.insert('',END,values=vv)
       

def export_stud():
    ff = filedialog.asksaveasfilename()
    gg = std_table.get_children()
    id,name,mobile,email,address,gender,dob,added_date,added_time =[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = std_table.item(i)
        pp = content['values']
        id.append(pp[0],name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),added_date.append(pp[7]),added_time.append(pp[8]))
    dd=['Id','Name','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip( id,name,mobile,email,address,gender,dob,added_date,added_time)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student Data Saved Successfully {}'.format(paths))
def exit():
    res = messagebox.askyesnocancel('Notification','Do you Want to Exit?')
    if (res== True):
        root.destroy()


def Connectdb():
    def submit_db():
        global con,mycursor
        host = host_val.get()
        user =user_val.get()
        password = password_val.get()
        # host ='localhost'
        # user = 'root'
        # password = 'hassan123'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor =con.cursor()
        except:
            messagebox.showerror('Notification','Incorrect Data, Please Try Again ')
            return
        try:
            strr = 'create Database University_management_system1'
            mycursor.execute(strr)
            strr = 'use University_management_system1'
            mycursor.execute(strr)
            strr = 'create table student_data1(id int, name varchar(20), mobile varchar(20), email varchar(30), address varchar (100), gender varchar(50), dob varchar(50),date varchar(50), time varchar(50) )'
            mycursor.execute(strr)
            strr = 'alter table student_data1 modify column id  int not null'
            mycursor.execute(strr)
            strr = 'alter table student_data1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Successfully Created Database,Now you are Connected to the Database' )

        except:
            strr = 'Use University_management_system1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Successfully Connected to the Database' )
        dbroot.destroy()
           
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.geometry('470x250+800+230')
    dbroot.config(bg='blue')
    
    hostlabel =Label(dbroot,text="Enter Host: ", bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)
    
    userlabel =Label(dbroot,text="Enter User: ", bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10,y=70)
    
    passwordlabel =Label(dbroot,text="Enter Password: ", bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10,y=130)

    host_val = StringVar()
    user_val = StringVar()
    password_val = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=host_val)
    hostentry.place(x=250,y=10)
    
    
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=user_val)
    userentry.place(x=250,y=70)

    
    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=password_val)
    passwordentry.place(x=250,y=130)

    submit_button = Button(dbroot, text ='Log In', font=('calibri',15,'bold'), bg='green2', bd=5, width=20,activebackground='red2', activeforeground='white',command=submit_db)
    submit_button.place(x=150,y=190)


    dbroot.mainloop()


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m: %Y")
    clock.config(text='Date: ' + date_string + "\nTime: "+ time_string)
    clock.after(200,tick)
    
# intro slider 
colors = ['red','green','blue', 'pink', 'orange','red2','gold']
def intro_lab_color():
    fg =random.choice(colors)
    slider_label.config(fg=fg)
    slider_label.after(175,intro_lab_color)




def intro_label():
    global count, text
    if(count >= len(ss)):
        count = -1
        text=''
        slider_label.config(text=text)
    else:
        text =text+ ss[count]
        slider_label.config(text = text)
    count += 1
    slider_label.after(175,intro_label)

from tkinter import*
import pymysql
import pandas
from tkinter import Toplevel, messagebox,filedialog
from tkinter.ttk import Treeview 
from tkinter import ttk
import time 
import random
root = Tk()
root.title("University Management System")
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.resizable(False,False)

# Frames

# Data entry frame
data_entry_frame = Frame(root, bg = 'gold2',relief=GROOVE, borderwidth=5)
data_entry_frame.place(x=10,y=80,width=500,height=600)


frontlabel = Label(data_entry_frame, text='-------------------WELCOME----------------------',width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
add_Btn = Button(data_entry_frame,text='1.  Add Student',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white', command=add_stud)
add_Btn.pack(side=TOP,expand=True)

search_Btn = Button(data_entry_frame,text='2.  Search Student',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=search_stud)
search_Btn.pack(side=TOP,expand=True)

dlt_Btn = Button(data_entry_frame,text='3.  Delete Student',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=dlt_stud)
dlt_Btn.pack(side=TOP,expand=True)

update_Btn = Button(data_entry_frame,text='4.  Update Student',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white', command=upd_stud)
update_Btn.pack(side=TOP,expand=True)

showAll_Btn = Button(data_entry_frame,text='5.  Show All',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=all_stud)
showAll_Btn.pack(side=TOP,expand=True)

export_Btn = Button(data_entry_frame,text='6.  Export Data',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=export_stud)
export_Btn.pack(side=TOP,expand=True)

exit_Btn = Button(data_entry_frame,text='7.  Exit',width=25,font=('centaur',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exit)
exit_Btn.pack(side=TOP,expand=True)

# Show data frames
show_dat = Frame(root, bg = 'gold2',relief=GROOVE, borderwidth=5)
show_dat.place(x=550,y=80,width=620,height=600)

style = ttk.Style()
style.configure('Treeview.Heading',font=('centaur',18,'bold'),foreground='black')
style.configure('Treeview',font=('times',13,'bold'),foreground='black')
scroll_x = Scrollbar(show_dat,orient=HORIZONTAL)
scroll_y = Scrollbar(show_dat,orient=VERTICAL)
std_table = Treeview(show_dat,columns=('Id','Name','Mob No','Email','Address','Gender','D.O.B','Added Date','Added Time'), yscrollcommand= scroll_y.set , xscrollcommand= scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=std_table.xview)
scroll_y.config(command=std_table.yview)
std_table.heading('Id',text='Id')
std_table.heading('Name',text='Name')
std_table.heading('Mob No',text='Mob NO')
std_table.heading('Email',text='Email')
std_table.heading('Address',text='Address')
std_table.heading('Gender',text='Gender')
std_table.heading('D.O.B',text='D.O.B')
std_table.heading('Added Date',text='Added Date')
std_table.heading('Added Time',text='Added Time')
std_table['show'] = 'headings'
std_table.column('Id',width=100)
std_table.column('Name',width=200)
std_table.column('Mob No',width=200)
std_table.column('Email',width=200)
std_table.column('Address',width=300)
std_table.column('Gender',width=100)
std_table.column('D.O.B',width=150)
std_table.column('Added Date',width=150)
std_table.column('Added Time',width=150)
std_table.pack(fill=BOTH, expand=1)

# Slider
ss= "Welcome To University Management System"
count = 0
text =''
slider_label = Label(root,text=ss,font=('centaur',30,'italic bold'), relief=RIDGE, borderwidth=4, width=35 , bg='cyan')
slider_label.place(x=180,y=0)
intro_label()
intro_lab_color()


# clock

clock = Label(root, font=('times',14,'bold'), relief=RIDGE, borderwidth=4 , bg='lawn green')
clock.place(x=0,y=0)
tick()

# BUtton
connect_button = Button(root, text='Connect to Database', width=18, font=('centaur',15,' bold'), relief=RIDGE,borderwidth=4, bg='green2', activebackground='blue', activeforeground='white', command=Connectdb)
connect_button.place(x=962,y=0)

root.mainloop()
