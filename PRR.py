import pypyodbc
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
m=Tk()
m.configure(bg='white')
m.geometry("1600x1000")
con = pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=E:\MAHEEN\FIRST SEM\Database41.accdb;')
l1=Label(m,text="AIRLINE RESERVATION SYSTEM",font=("Times New Roman",48,"bold"),bd=10,width=42,bg="purple",fg="white")
l1.grid(row=0,column=0,sticky=N)

img1=PhotoImage(file="maf_logo.png")
img2=img1.subsample(2,2)
lim=Label(m,image=img2).grid(row=1,column=0)

def cb():
    n=Tk()
    n.title("Welcome to our cancellation system")
    n.configure(bg="black")
    l2=Label(n,text="CANCELLATION SYSTEM",width=20,font=("Times New Roman",12,"bold"),bd=10,bg="pink",fg="black").grid(row=0,column=0)
    l3=Label(n,text="ENTER PASSPORT NUMBER",width=30,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=2,column=0,padx=15,pady=15)
    e1=Entry(n)
    e1.grid(row=2,column=1,padx=10,pady=10)
    l4 = Label(n,text="ENTER CLASS:",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=3, column=0,padx=15,pady=15)
    z1=ttk.Combobox(n,height=7,width=20,values=["economy","bussiness"])
    z1.grid(row=3,column=1,padx=10,pady=10)
    l5= Label(n, text="SELECT BOARDING",width=35,height=2,pady=10,padx=10,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=4, column=0,padx=15,pady=15)
    z2 = ttk.Combobox(n, height=7, width=35, values=["karachi", "islamabad","skurdu","gilgit"])
    z2.grid(row=4, column=1,padx=10,pady=10)
    def cr():
        a=e1.get()
        b=z1.get()
        c=z2.get()
        cur1=con.cursor()
        con.commit()
        if a=='' or b=='' or c=='':
            messagebox.showerror("ERROR","you can't leave any field empty")
        else:
            if b=="economy":
                cur1.execute(f"DELETE from economy where adno=(?) and boarding=(?)",(a,c))
                cur1.commit()
                cur1.execute("select * from economy")
                messagebox.showinfo("your reservation has cancelled",cur1.fetchall())
            else:
                cur1.execute(f"DELETE from bussiness where adno=(?) and boarding=(?)", (a, c))
                cur1.commit()
                cur1.execute("select * from bussiness")
                messagebox.showinfo("your reservation has cancelled", cur1.fetchall())
    bc=Button(n,text="cancel reservation",bg="green",width=25,command=cr).grid(row=4,column=2,padx=15,pady=15)
    n.mainloop()

def sf():
    l=Tk()
    l.configure(bg="black")
    l.title("Welcome,Search Flights")
    l2 = Label(l, text="SEARCH FLIGHT", width=20, font=("Times New Roman", 12, "bold"), bd=10, bg="pink",fg="black").grid(row=0, column=0)
    l1=Label(l,text="ENTER BOARDING",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=1,column=0,padx=10,pady=10)
    w1=ttk.Combobox(l,height=5,width=15,values=["karachi","islamabad","skurdu","gilgit"])
    w1.grid(row=1,column=1)
    l2=Label(l,text="SELECT DESTINATION",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=2,column=0,padx=10,pady=10)
    w2=ttk.Combobox(l,height=5,width=15,values=["karachi","islamabad","skurdu","gilgit"])
    w2.grid(row=2,column=1)
    l3=Label(l,text="CHOOSE DAY OF TRAVEL",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=3,column=0,padx=10,pady=10)
    w3= ttk.Combobox(l,height=5,width=15,values=["sun", "mon", "tues", "wed","thurs","fri","sat"])
    w3.grid(row=3, column=1)
    def isf():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur3=con.cursor()
        if a=='' or b=='' or c=='':
            messagebox.showerror("ERROR","you can't leave any field empty")
        else:
            if a!=b:
                cur3.execute("select * from flights where boarding=? and destination=?",(a,b))
                z=cur3.fetchall()
                messagebox.showinfo("flights availaible",z)
            else:
                messagebox.showerror("boarding and desstination cant be same")

    b4=Button(l,text='SEARCH',command=isf,width=15,bg='green',fg='white').grid(row=4,column=0)
    l.mainloop()

def fb():
    p=Tk()
    p.title("Flight booking")
    p.configure(bg="black")
    l1 = Label(p, text="BOOK YOUR FLIGHT", width=20, font=("Times New Roman", 12, "bold"), bd=10, bg="pink", fg="black").grid(row=0, column=0,padx=10,pady=10)
    l2=Label(p,text="ENTER BOARDING",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=1,column=0)
    w1=ttk.Combobox(p,height=5,width=15,values=["karachi","islamabad","skurdu","gilgit"])
    w1.grid(row=1,column=1)
    l3=Label(p,text="ENTER DESTINATION",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=2,column=0,padx=10,pady=10)
    w2= ttk.Combobox(p, height=5, width=15, values=["karachi", "islamabad", "skurdu", "gilgit"])
    w2.grid(row=2, column=1)
    l4=Label(p,text="ENTER PASSPORT NUMBER:",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=3,column=0,padx=10,pady=10)
    e1=Entry(p,width=20)
    e1.grid(row=3,column=1)
    l5=Label(p,text="CHOOSE CLASS",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=4,column=0,padx=10,pady=10)
    w3=ttk.Combobox(p,height=5,width=15,values=["bussinessclass","economy"])
    w3.grid(row=4,column=1)
    l6=Label(p,text="CHOOSE DAY OF TRAVEL",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=5,column=0,padx=10,pady=10)
    w4=ttk.Combobox(p,height=5,width=15,values=["sun","mon","tues","wed","thurs","fri","sat"])
    w4.grid(row=5,column=1)
    l7=Label(p,text="CHOOSE TIME OF FLIGHT",width=35,height=3,bg="purple",fg="white",font=("Times New Roman",10,"bold")).grid(row=6,column=0,padx=10,pady=10)
    w5=ttk.Combobox(p,height=5,width=15,values=["1:00 AM","7:00 AM","1:00 PM","4:00 PM","9:00 PM"])
    w5.grid(row=6,column=1)
    def fbb():
        a=w1.get()
        b=w2.get()
        c=e1.get()
        d=w3.get()
        f=w4.get()
        g=w5.get()
        cur2=con.cursor()

        if a=='' or b=='' or c=='' or d==''or f=='' or g=='':
            messagebox.showerror("ERROR","you can't leave any field empty")
            cur2.close()
        else:
            if d=="economy":
                if a!=b:
                    cur2.execute(f"INSERT INTO economy(boarding,destination,adno,day,time2) values('{w1.get()}','{w2.get()}','{e1.get()}','{w4.get()}','{w5.get()}')")
                    messagebox.showinfo("congrats","one seat has been reserved")
                    con.commit()
                    cur2.execute(f"select * from economy where adno={e1.get()}")
                    messagebox.showinfo("records",cur2.fetchall())
                else:
                    messagebox.showerror("error","you can't choose same city")
            else:
                if a!=b:
                    cur2.execute(f"INSERT INTO bussiness(boarding,destination,adno,day,time2) values('{w1.get()}','{w2.get()}','{e1.get()}','{w4.get()}','{w5.get()}')")
                    messagebox.showinfo("congrats","one seat has been reserved")
                    cur2.commit()
                    cur2.execute(f"select * from bussiness where adno={(e1.get())}")
                    messagebox.showinfo("records",cur2.fetchall())
                else:
                    messagebox.showerror("error","you can't choose same city")


    b2=Button(p,text="BOOK FLIGHT",command=fbb,bg="green",fg="white").grid(row=8,column=0)
    p.mainloop()

b1=Button(m,text="CANCEL BOOKING",height=4,width=35,font=("Times New Roman",15,"bold"),bg="black",fg="white",command=cb).grid(row=7,column=0,padx=10,pady=10)
b2=Button(m,text="SEARCH FLIGHT",height=4,width=35,font=("Times New Roman",15,"bold"),bg="black",fg="white",command=sf).grid(row=5,column=0,padx=10,pady=10)
b3=Button(m,text="BOOK FLIGHT",height=4,width=35,font=("Times New Roman",15,"bold"),bg="black",fg="white",command=fb).grid(row=6,column=0,padx=10,pady=10)

m.mainloop()