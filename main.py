from logging import root
from tkinter import*
from turtle import title
from PIL import Image,ImageTk
from customer import cust

class Hotel :
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management")
        self.root.geometry("1500x800+0+0")

#Top Image
        img1=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel_Hospital Management\Images\wide.jpg")
        img1=img1.resize((1500,140),Image.ANTIALIAS)
        self.bagimg=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.bagimg,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1550,height=140)

#title
        title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title.place(x=0,y=140,width=1550,height=70)

#Logo
      
        img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel_Hospital Management\Images\logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.bagimg1=ImageTk.PhotoImage(img2)

        lab=Label(self.root,image=self.bagimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=230,height=140)

#main frame
        mainf=Frame(self.root,bd=4,relief=RIDGE)
        mainf.place(x=0,y=210,width=1550,height=620)

#menu
        menu=Label(mainf,text="MENU",font=("times new roman",40,"bold"),bg="dark blue",fg="silver",bd=4,relief=RIDGE)
        menu.place(x=0,y=0,width=250,)


#button frame
        btn=Frame(mainf,bd=4,relief=RIDGE)
        btn.place(x=0,y=65,width=250,height=190)

        cust_btn=Button(btn,text="CUSTOMER",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn,text="ROOM",width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        detail_btn=Button(btn,text="DETAILS",width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        detail_btn.grid(row=2,column=0,pady=1)

        repo_btn=Button(btn,text="REPORT",width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        repo_btn.grid(row=3,column=0,pady=1)

        logout=Button(btn,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        logout.grid(row=4,column=0,pady=1)

#main frame img
        img3=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel_Hospital Management\Images\Back.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.bagimg3=ImageTk.PhotoImage(img3)

        lab=Label(mainf,image=self.bagimg3,bd=4,relief=RIDGE)
        lab.place(x=225,y=0,width=1310,height=590)

#down frame img
        img4=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel_Hospital Management\Images\down.jpg")
        img4=img4.resize((170,250),Image.ANTIALIAS)
        self.bagimg4=ImageTk.PhotoImage(img4)

        lab=Label(mainf,image=self.bagimg4,bd=0,relief=RIDGE)
        lab.place(x=0,y=260,width=210,height=330)

        

    def cust_details(self):
            self.new_window=Toplevel(self.root)
            self.za=cust(self.new_window)






if __name__=="__main__":
    root=Tk()
    obj=Hotel(root)
    root.mainloop()