from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



win=Tk()
win.geometry("900x700")
win.title("Expense Analysis Tool ")



def register():
    def click_register():
        id=entry_id.get()
        name=entry_name.get()
        email=entry_email.get()
        psw=entry_password.get()
        contact=entry_contact.get()

        if (id=="" or psw=="" or name=="" or email=="" or contact==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        else:
            con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("insert into new_table values('"+id+"','"+name+"','"+email+"','"+contact+"','"+psw+"')")
            cursor.execute("commit")

            MessageBox.showinfo("Alert","Registration completed Successfully")
            con.close()
            login()

    f1=Frame(bg="#0096DC")
    f1.place(x=0,y=0,height=500,width=500)

    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l2=Label(f1,text="Name:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l3=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#0096DC")
    l4=Label(f1,text="Contact",font=("Verdena 15"),fg="white",bg="#0096DC")
    l5=Label(f1,text="Password:",font=("Verdena 15"),fg="white",bg="#0096DC")

    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    l4.place(x=100,y=250)
    l5.place(x=100,y=300)

    entry_id=Entry(f1,font=("Verdena 15"))
    entry_name=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_contact=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,show="*",font=("Verdena 15"))
    
    entry_id.place(x=200,y=100)
    entry_name.place(x=200,y=150)
    entry_email.place(x=200,y=200)
    entry_password.place(x=200,y=300)
    entry_contact.place(x=200,y=250)

    b1=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=click_register)
    b2=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=login)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
    
    
    
def login():
    def click_login():
        id=entry_id.get()
        email=entry_email.get()
        psw=entry_password.get()
        
        con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        cursor.execute("SELECT Userid FROM new_table")
        database_id=cursor.fetchall()
        cursor.execute("SELECT Email FROM new_table")
        database_email=cursor.fetchall()
        cursor.execute("SELECT Password FROM new_table")
        database_psw=cursor.fetchall()
        
        var1=0
        var2=0
        var3=0

        
        for userid in database_id:
               uid=userid[0]
               if(uid==id):
                   var1=1    
        for useremail in database_email:
               uml=useremail[0]
               if(uml==email):
                   var2=1    
        for userpsw in database_psw:
               upw=userpsw[0]
               if(upw==psw):
                   var3=1    
          
        if (id=="" or psw=="" or email==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 or var2==1 or var3==1):
            MessageBox.showinfo("Alert","Login completed Successfully")
            
            #for task
            def insert(itemname,date,cost):
                con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                cur=con.cursor()
                cur.execute("INSERT INTO expenses (Name,Date,Cost)VALUES(%s,%s,%s)",(itemname,date,cost))
                con.commit()
                con.close()

            def view():
                con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                cur=con.cursor()
                cur.execute("SELECT * FROM expenses")
                rows=cur.fetchall()
                con.commit()
                con.close()
                return rows
    
            def search(itemname="",date="",cost=""):
                 con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                 cursor=con.cursor()
                 cursor.execute("SELECT * FROM expenses WHERE itemname=? OR date=? OR cost=?",(itemname,date,cost))
                 rows=cursor.fetchall()
                 con.commit()
                 con.close()
                 return rows

            def delete(id):
                con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                cur=con.cursor()
                
                cur.execute("DELETE FROM expenses WHERE id=?",(id))
                con.commit()
                con.close()
            
            def insertitems(itemname,date,cost):
                a=exp_itemname.get()
                b=exp_date.get()
                c=exp_cost.get()
                d=c.replace('.', '', 1)
                e=b.count('-')      

                if a=="" or b=="" or c=="":
                    messagebox.showinfo("oops something wrong","Field should not be empty")
                elif len(b)!=10 or e!=2:
                    messagebox.showinfo("oops something wrong","DATE should be in format dd-mm-yyyy")
                elif (d.isdigit()==False):
                    messagebox.showinfo("oops something wrong","Cost should be a number")
                else:
                    insert(a,b,c)
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                
            def viewallitems():
                tree.delete(0,END)
                tree.insert(END,"ID   NAME     DATE      COST")
                for row in view():
                    a=str(row[0])
                    b=str(row[1])
                    c=str(row[2])
                    d=str(row[3])
                    f= a + "     " + b + "    " + c + "    " + d
                    tree.insert(END,f)
            def deletewithid():
                 for item in tree.get_children():
                    tree.delete(item)

            
            def deletealldata():
                con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                cur=con.cursor()
                cur.execute("DELETE FROM expenses")
                con.commit()
                con.close()
                tree.delete(0,END)
                messagebox.showinfo('Successful', 'All data deleted')
            def search_item():
                tree.delete(0,END)
                tree.insert(END,"ID   NAME     DATE      COST")
                for row in search(exp_itemname.get(),exp_date.get(),exp_cost.get()):
                    a=str(row[0])
                    b=str(row[1])
                    c=str(row[2])
                    d=str(row[3])
                    f= a + "     " + b + "    " + c + "    " + d
                    tree.insert(END,f)
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                            
            def sumofitems():
                con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
                # cur=con.cursor()
                # cur.execute("SELECT SUM(cost) FROM expenses ")
                # sum=cur.fetchone()
                # tree.delete(0,END)
                # b=str(sum[0])
                # a="YOU SPENT " + b
                # messagebox.showinfo('TOTAL SPENT',a)
                # con.commit()
                # con.close()
                # return 

               
                cur = con.cursor()
                cur.execute("SELECT SUM(cost) FROM expenses")
                sum = cur.fetchone()
                
                # Clear the treeview
                for item in tree.get_children():
                    tree.delete(item)
                
                b = str(sum[0])
                a = "YOU SPENT " + b
                messagebox.showinfo('TOTAL SPENT', a)
                con.commit()
                con.close()
                return

            

            def endpage():
                p1=Label(gui,width=100,height=100,font=("century",35),bg="#bfbfbf",text="")
                p1.place(x=-455,y=0)
                p2=Label(gui,font=("lucida fax",40),bg="#bfbfbf",text="EXPENSE Anlysis Tool")
                p2.place(x=190,y=10)
                

            def recall():
                tree =ttk.Treeview(gui, columns=('ID', 'Name', 'Date','Cost'), show='headings')
                tree.heading('ID', text='ID')
                tree.heading('Name', text='Name')
                tree.heading('Date', text='Date')
                tree.heading('Cost',text='Cost')

                tree.column('ID', width=100)
                tree.column('Name', width=100)
                tree.column('Date', width=100)
                tree.column('Cost',width=100)
                #tree_height = min(len(tree) * 15, 350)
                
                for row in rows:
                        tree.insert('', tk.END, values=row)

                tree.place(x=168, y=450, width=500, height=400)
                con.close()
                
            
            
            gui=Frame(bg="#B1DDC6")
            gui.place(x=0,y=0,height=700,width=900)
            l1=Label(gui,width=60,height=7,font=("century",35),bg="#1ad1ff",text="")
            
            l3=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Product name",fg="white")
            
            #
        
            #
            
            
    
            l1.place(x=450,y=60)
        
            l3.place(x=10,y=150)
            exp_itemname=StringVar()
            e1=Entry(gui,font=("adobe clean",15),textvariable=exp_itemname)
            e1.place(x=220,y=155,height=27,width=165)
            l4=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Date(dd-mm-yyyy)")
            l4.place(x=10,y=200)
            exp_date=StringVar()
            e2=Entry(gui,font=("adobe clean",15),textvariable=exp_date)
            e2.place(x=220,y=205,height=27,width=165)
            l5=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Cost of product")
            l5.place(x=10,y=250)
            exp_cost=StringVar()
            e3=Entry(gui,font=("adobe clean",15),textvariable=exp_cost)
            e3.place(x=220,y=255,height=27,width=165)
            # l6=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Select ID to delete")
            # l6.place(x=520,y=170)
            #exp_id=StringVar()
            # sb=Spinbox(gui, font=("adobe clean",17),from_= 0, to_ = 200,textvariable=exp_id,justify=CENTER)
            # sb.place(x=745,y=174,height=30,width=50)
            
            
            con=mysql.connect(host="localhost",user="root",password="#Ani@8318",database="expense_proj",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("SELECT * FROM expenses")
            rows=cursor.fetchall()
            
            tree =ttk.Treeview(gui, columns=('ID', 'Name', 'Date','Cost'), show='headings')
            tree.heading('ID', text='ID')
            tree.heading('Name', text='Name')
            tree.heading('Date', text='Date')
            tree.heading('Cost',text='Cost')

            tree.column('ID', width=100)
            tree.column('Name', width=100)
            tree.column('Date', width=100)
            tree.column('Cost',width=100)
            #tree_height = min(len(tree) * 15, 350)
            
            for row in rows:
                    tree.insert('', tk.END, values=row)

            tree.place(x=168, y=450, width=500, height=400)
            con.close()
            
            
            
            b1=Button(gui,text="Add Item",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=12,command=lambda:insertitems(e1.get(),e2.get(),e3.get()))
            b2=Button(gui,text="View all items",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=recall)
            b3=Button(gui,text="Delete",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=deletewithid)
            b4=Button(gui,text="Delete all items",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=deletealldata)
            b5=Button(gui,text="Search",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=10,command=search_item)
            b6=Button(gui,text="Total spent",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=sumofitems)
            b7=Button(gui,text="Close app",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=endpage)
            l6=Label(gui,width=60,font=("century",35),bg="#ff9999",fg="#b32d00",text="EXPENSE  ANLYSIS TOOL")
            l6.place(x=-450,y=0)
            
            b1.place(x=30,y=300)
            b2.place(x=110,y=355)
            b3.place(x=572,y=220)
            b4.place(x=550,y=280)
            b5.place(x=220,y=298)
            b6.place(x=550,y=340)
            b7.place(x=700,y=650)
            
            
            
        
        else:
            MessageBox.showinfo("Alert","There is error")
        
    f1=Frame(bg="#B1DDC6")
    f1.place(x=0,y=0,height=500,width=500)
    
    label_head=Label(f1,text="Fill credentials To Login",font=("Verdena 25"),fg="white",bg="#B1DDC6")
    label_head.place(x=80,y=10)
    
    
    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l2=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l3=Label(f1,text="password",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    
    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    
    entry_id=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,font=("Verdena 15"),show="*")

    entry_id.place(x=200,y=100)
    entry_email.place(x=200,y=150)
    entry_password.place(x=200,y=200)
    
    b1=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=click_login)
    b2=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=register)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)


register()
win.mainloop()