from logging import root
from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class cust:
    def __init__(self,root) :
            self.root=root
            self.root.title("Customer Management")
            self.root.geometry("1290x540+230+245")


#variables
            self.var=StringVar()
            x=random.randint(1,99999)
            self.var.set(str(x))

            self.var_cust=StringVar()
            self.var_name=StringVar()
            self.var_natio=StringVar()
            self.var_gender=StringVar()
            self.var_email=StringVar()
            self.var_mob=StringVar()
            self.var_state=StringVar()
            self.var_pin=StringVar()
            self.var_addr=StringVar()
            self.var_id_proof=StringVar()
            self.var_id_no=StringVar()


#title
            title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            title.place(x=0,y=0,width=1290,height=50)

#label frame
            lbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
            lbf.place(x=5,y=50,width=425,height=490)

#labels in frame

            lab_ref=Label(lbf,text="Customer Reference:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_ref.grid(row=0,column=0,sticky=W)
            entry_ref=ttk.Entry(lbf,textvariable=self.var,width=33,font=("arial",10),state="readonly")
            entry_ref.grid(row=0,column=1)

            lab_name=Label(lbf,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_name.grid(row=1,column=0,sticky=W)
            entry_name=ttk.Entry(lbf,textvariable=self.var_name,width=33,font=("arial",10))
            entry_name.grid(row=1,column=1)

            lab_add=Label(lbf,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_add.grid(row=2,column=0,sticky=W)
            entry_add=ttk.Entry(lbf,textvariable=self.var_addr,width=33,font=("arial",10))
            entry_add.grid(row=2,column=1)

            lab_id=Label(lbf,text="ID Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_id.grid(row=3,column=0,sticky=W)
            cke_id=ttk.Combobox(lbf,font=("arial",10),textvariable=self.var_id_proof,width=31,state="readonly")
            cke_id["value"]=("Adhar Card","Passport","Driving Licence")
            cke_id.current(0)
            cke_id.grid(row=3,column=1)
        

            lab_adh=Label(lbf,text="ID Card No:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_adh.grid(row=4,column=0,sticky=W)
            entry_adh=ttk.Entry(lbf,textvariable=self.var_id_no,width=33,font=("arial",10))
            entry_adh.grid(row=4,column=1)

            lab_gen=Label(lbf,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_gen.grid(row=5,column=0,sticky=W)
            cke_gen=ttk.Combobox(lbf,font=("arial",10),width=31,textvariable=self.var_gender,state="readonly")
            cke_gen["value"]=("Male","Female","Other")
            cke_gen.current(0)
            cke_gen.grid(row=5,column=1)
        

            lab_sta=Label(lbf,text="State:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_sta.grid(row=6,column=0,sticky=W)
            entry_sta=ttk.Entry(lbf,width=33,textvariable=self.var_state,font=("arial",10))
            entry_sta.grid(row=6,column=1)

            lab_pin=Label(lbf,text="Pincode:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_pin.grid(row=10,column=0,sticky=W)
            entry_pin=ttk.Entry(lbf,width=33,textvariable=self.var_pin,font=("arial",10))
            entry_pin.grid(row=10,column=1)

            lab_mob=Label(lbf,text="Mobile No:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_mob.grid(row=7,column=0,sticky=W)
            entry_mob=ttk.Entry(lbf,width=33,textvariable=self.var_mob,font=("arial",10))
            entry_mob.grid(row=7,column=1)

            lab_eid=Label(lbf,text="Email Id:",font=("arial",12,"bold"),padx=2,pady=6)
            lab_eid.grid(row=8,column=0,sticky=W)
            entry_eid=ttk.Entry(lbf,width=33,textvariable=self.var_email,font=("arial",10))
            entry_eid.grid(row=8,column=1)

            lab_nat=Label(lbf,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
            lab_nat.grid(row=9,column=0,sticky=W)
            entry_nat=ttk.Entry(lbf,width=33,textvariable=self.var_natio,font=("arial",10))
            entry_nat.grid(row=9,column=1)
#buttons


            btf=Frame(lbf,bd=2,relief=RIDGE)
            btf.place(x=0,y=400,width=412,height=40)

            btn_add=Button(btf,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_add.grid(row=0,column=0,pady=1,padx=1)

            btn_upd=Button(btf,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_upd.grid(row=0,column=1,pady=1,padx=1)

            btn_dle=Button(btf,text="Delete",font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_dle.grid(row=0,column=2,pady=1,padx=1)

    
            btn_reset=Button(btf,text="Reset",font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_reset.grid(row=0,column=3,pady=1,padx=1)

#tableframemiddle

            lbm=LabelFrame(self.root,bd=2,relief=RIDGE,text=" View and Search Customer Details",font=("times new roman",12,"bold"),padx=2)
            lbm.place(x=435,y=50,width=860,height=490)

            lab_search=Label(lbm,text="Search By:-",font=("arial",12,"bold"),bg="black",fg="white")
            lab_search.grid(row=0,column=0,sticky=W,padx=2)

            cke_search=ttk.Combobox(lbm,font=("arial",13),width=20,state="readonly")
            cke_search["value"]=("Id Card No","Mobile","Name")
            cke_search.current(0)
            cke_search.grid(row=0,column=1,padx=2)
            entry_search=ttk.Entry(lbm,width=25,font=("arial",13))
            entry_search.grid(row=0,column=2,padx=2)

            btn_search=Button(lbm,text="Search",font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_search.grid(row=0,column=3,pady=1,padx=1)

            btn_show=Button(lbm,text="Show",font=("arial",12,"bold"),bg="black",fg="white",width=9)
            btn_show.grid(row=0,column=4,pady=1,padx=1)

#data table
            showt=Frame(lbm,bd=2,relief=RIDGE)
            showt.place(x=0,y=50,width=845,height=410)

            scrx=ttk.Scrollbar(showt,orient=HORIZONTAL)
            scry=ttk.Scrollbar(showt,orient=VERTICAL)

            self.custseatable=ttk.Treeview(showt,columns=("ref","name","address","id proof type","id no","gender","state","pincode","mobile","email","nationality"),
            yscrollcommand=scry.set,xscrollcommand=scrx.set)

            scrx.pack(side=BOTTOM,fill=X)
            scry.pack(side=RIGHT,fill=Y)

            scrx.config(command=self.custseatable.xview)
            scry.config(command=self.custseatable.yview)


            self.custseatable.heading("ref",text="Reference No")
            self.custseatable.heading("name",text="Name")
            self.custseatable.heading("address",text="Address")
            self.custseatable.heading("id proof type",text="ID Type")
            self.custseatable.heading("id no",text="ID No")
            self.custseatable.heading("gender",text="Gender")
            self.custseatable.heading("state",text="State")
            self.custseatable.heading("pincode",text="Pincode")
            self.custseatable.heading("mobile",text="Mobile")
            self.custseatable.heading("email",text="Email ID")
            self.custseatable.heading("nationality",text="Nationality")
           

            self.custseatable["show"]="headings"
            self.custseatable.column("ref",width=100)
            self.custseatable.column("name",width=150)
            self.custseatable.column("address",width=200)
            self.custseatable.column("id proof type",width=100)
            self.custseatable.column("id no",width=100)
            self.custseatable.column("gender",width=100)
            self.custseatable.column("state",width=100)
            self.custseatable.column("pincode",width=100)
            self.custseatable.column("mobile",width=100)
            self.custseatable.column("email",width=150)
            self.custseatable.column("nationality",width=100)
            

            self.custseatable.pack(fill=BOTH,expand=1)
            self.custseatable.bind("<ButtonRelease-1>",self.getcur)
            self.fetch_data()

    def add_data(self):
        if self.var_mob.get()=="" or self.var_id_no.get()=="":
            messagebox.showerror("Error","All Fields Not Field",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Messi10#",database="management")
                my_cur=conn.cursor()
                my_cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var.get(),
                                                                        self.var_name.get(),
                                                                        self.var_addr.get(),
                                                                        self.var_id_proof.get(),
                                                                        self.var_id_no.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_state.get(),
                                                                        self.var_pin.get(),
                                                                        self.var_mob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_natio.get(),
                                                                                                                                                
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Great Success","Customer Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Someting is Wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Messi10#",database="management")
        my_cur=conn.cursor()
        my_cur.execute("select * from customer")
        fet=my_cur.fetchall()
        if len(fet)!=0:
            self.custseatable.delete(*self.custseatable.get_children())
            for i in fet:
                self.custseatable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def getcur(self,events=""):
        currow=self.custseatable.focus()
        content=self.custseatable.item(currow)
        row=content["values"]

        self.var.set(row[0]),
        self.var_name.set(row[1]),
        self.var_addr.set(row[2]),
        self.var_id_proof.set(row[3]),
        self.var_id_no.set(row[4]),
        self.var_gender.set(row[5]),
        self.var_state.set(row[6]),
        self.var_pin.set(row[7]),
        self.var_mob.set(row[8]),
        self.var_email.set(row[9]),
        self.var_natio.set(row[10])

    def update(self):
        # print(f"update customer set 'name=%s','address=%s','id proof type=%s','id no=%s','gender=%s','state=%s','pincode=%s','mobile=%s','email=%s','nationality=%s' where 'ref=%s'",( 
        #                                                                                                                     self.var_name.get(),
        #                                                                                                                     self.var_addr.get(),
        #                                                                                                                     self.var_id_proof.get(),
        #                                                                                                                     self.var_id_no.get(),
        #                                                                                                                     self.var_gender.get(),
        #                                                                                                                     self.var_state.get(),
        #                                                                                                                     self.var_pin.get(),
        #                                                                                                                     self.var_mob.get(),
        #                                                                                                                     self.var_email.get(),
        #                                                                                                                     self.var_natio.get(),
        #                                                                                                                     self.var.get()   
        #                                                                                                                     ))
       if self.var_mob.get()=="":
           messagebox.showerror("Error","Please Enter Mobile No",parent=self.root)
       else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Messi10#",database="management")
            my_cur=conn.cursor()
            # my_cur.execute("update customer set name='%s',address='%s',id proof type='%s',id no='%s',gender='%s',state='%s',pincode='%s',mobile='%s',email='%s',nationality='%s' where ref='%s'",( 
            #                                                                                                                 self.var_name.get(),
            #                                                                                                                 self.var_addr.get(),
            #                                                                                                                 self.var_id_proof.get(),
            #                                                                                                                 self.var_id_no.get(),
            #                                                                                                                 self.var_gender.get(),
            #                                                                                                                 self.var_state.get(),
            #                                                                                                                 self.var_pin.get(),
            #                                                                                                                 self.var_mob.get(),
            #                                                                                                                 self.var_email.get(),
            #                                                                                                                 self.var_natio.get(),
            #                                                                                                                 self.var.get()   
            #                                                                                                                 ))

            update_user=("update customer set" "(name,address,id proof type,id no,gender,state,pincode,mobile,email,nationality)" "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" "where ref=" "(%s)")
            data_user=( (self.var_name.get(),
                    self.var_addr.get(),
                    self.var_id_proof.get(),
                    self.var_id_no.get(),
                    self.var_gender.get(),
                    self.var_state.get(),
                    self.var_pin.get(),
                    self.var_mob.get(),
                    self.var_email.get(),
                    self.var_natio.get()),
                    self.var.get())

            my_cur.execute(update_user,data_user)

            # my_cur.execute("update customer set name='?',address='?',id proof type='?',id no='?',gender='?',state='?',pincode='?',mobile='?',email='?',nationality='?' where ref='?'",( 
            #                                                                                                                 self.var_name.get(),
            #                                                                                                                 self.var_addr.get(),
            #                                                                                                                 self.var_id_proof.get(),
            #                                                                                                                 self.var_id_no.get(),
            #                                                                                                                 self.var_gender.get(),
            #                                                                                                                 self.var_state.get(),
            #                                                                                                                 self.var_pin.get(),
            #                                                                                                                 self.var_mob.get(),
            #                                                                                                                 self.var_email.get(),
            #                                                                                                                 self.var_natio.get(),
            #                                                                                                                 self.var.get()   
            #                                                                                                                 ))
                                                                                                                            
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated Succesfully","Customer Details Updated Succesfully",parent=self.root)


        

        

    


if __name__=="__main__":
    root=Tk()
    obj=cust(root)
    root.mainloop()