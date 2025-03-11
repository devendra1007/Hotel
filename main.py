import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from customer import CustomerManager
import os

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")
        self.root.configure(bg='white')
        
        self.load_images()
        self.create_header()
        self.create_main_frame()
    
    def load_images(self):
        """Load all images used in the application"""
        # Define a base path for images - replace with your actual path
        base_path = os.path.join(os.path.dirname(__file__), "images")
        
        # Load and resize the wide header image
        img1 = Image.open(os.path.join(base_path, "wide.jpg"))
        img1 = img1.resize((1500, 140), Image.LANCZOS)
        self.header_img = ImageTk.PhotoImage(img1)
        
        # Load and resize the logo
        img2 = Image.open(os.path.join(base_path, "logo.jpg"))
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(img2)
        
        # Load and resize the main background image
        img3 = Image.open(os.path.join(base_path, "Back.jpg"))
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.background_img = ImageTk.PhotoImage(img3)
        
        # Load and resize the bottom left image
        img4 = Image.open(os.path.join(base_path, "down.jpg"))
        img4 = img4.resize((170, 250), Image.LANCZOS)
        self.bottom_img = ImageTk.PhotoImage(img4)
    
    def create_header(self):
        """Create the header section with logo and title"""
        # Header image
        header_label = tk.Label(self.root, image=self.header_img, bd=4, relief=tk.RIDGE)
        header_label.place(x=0, y=0, width=1550, height=140)
        
        # Logo
        logo_label = tk.Label(self.root, image=self.logo_img, bd=4, relief=tk.RIDGE)
        logo_label.place(x=0, y=0, width=230, height=140)
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Hotel Management System",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=tk.RIDGE
        )
        title_label.place(x=0, y=140, width=1550, height=70)
    
    def create_main_frame(self):
        """Create the main frame with menu and content area"""
        # Main frame
        main_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE)
        main_frame.place(x=0, y=210, width=1550, height=620)
        
        # Menu label
        menu_label = tk.Label(
            main_frame,
            text="MENU",
            font=("times new roman", 40, "bold"),
            bg="dark blue",
            fg="silver",
            bd=4,
            relief=tk.RIDGE
        )
        menu_label.place(x=0, y=0, width=250)
        
        # Create button frame for menu options
        self.create_button_frame(main_frame)
        
        # Main background image
        bg_label = tk.Label(main_frame, image=self.background_img, bd=4, relief=tk.RIDGE)
        bg_label.place(x=225, y=0, width=1310, height=590)
        
        # Bottom image
        bottom_label = tk.Label(main_frame, image=self.bottom_img, bd=0, relief=tk.RIDGE)
        bottom_label.place(x=0, y=260, width=210, height=330)
    
    def create_button_frame(self, parent):
        """Create the navigation buttons"""
        btn_frame = tk.Frame(parent, bd=4, relief=tk.RIDGE)
        btn_frame.place(x=0, y=65, width=250, height=190)
        
        # Button styling
        btn_style = {
            "width": 20,
            "font": ("times new roman", 14, "bold"),
            "bg": "gold",
            "fg": "black",
            "bd": 0,
            "cursor": "hand2"
        }
        
        # Create navigation buttons
        customer_btn = tk.Button(btn_frame, text="CUSTOMER", command=self.open_customer_window, **btn_style)
        customer_btn.grid(row=0, column=0, pady=1)
        
        room_btn = tk.Button(btn_frame, text="ROOM", **btn_style)
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn = tk.Button(btn_frame, text="DETAILS", **btn_style)
        details_btn.grid(row=2, column=0, pady=1)
        
        report_btn = tk.Button(btn_frame, text="REPORT", **btn_style)
        report_btn.grid(row=3, column=0, pady=1)
        
        logout_btn = tk.Button(btn_frame, text="LOGOUT", **btn_style)
        logout_btn.grid(row=4, column=0, pady=1)
    
    def open_customer_window(self):
        """Open the customer management window"""
        self.new_window = tk.Toplevel(self.root)
        self.customer_window = CustomerManager(self.new_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()