import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os


class CustomerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("1290x540+230+245")
        
        # Initialize variables for form fields
        self.initialize_variables()
        
        # Create UI components
        self.create_title_bar()
        self.create_customer_form()
        self.create_search_view()
        
        # Load initial data
        self.fetch_data()
        
    def initialize_variables(self):
        """Initialize tkinter variables for form fields"""
        # Generate random reference number
        self.var_ref = tk.StringVar()
        self.var_ref.set(str(random.randint(1, 99999)))
        
        # Customer details variables
        self.var_name = tk.StringVar()
        self.var_nationality = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_mobile = tk.StringVar()
        self.var_state = tk.StringVar()
        self.var_pincode = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_id_proof = tk.StringVar()
        self.var_id_number = tk.StringVar()
        
        # Search variables
        self.var_search_by = tk.StringVar()
        self.var_search_text = tk.StringVar()
        
    def create_title_bar(self):
        """Create the title bar at the top of the window"""
        title = tk.Label(
            self.root, 
            text="ADD CUSTOMER DETAILS", 
            font=("times new roman", 20, "bold"), 
            bg="black", 
            fg="gold", 
            bd=4, 
            relief=tk.RIDGE
        )
        title.place(x=0, y=0, width=1290, height=50)
        
    def create_customer_form(self):
        """Create the form for customer details entry"""
        # Frame for customer details
        form_frame = ttk.LabelFrame(
            self.root, 
            text="Customer Details", 
            padding=10
        )
        form_frame.place(x=5, y=50, width=425, height=490)
        
        # Create form fields
        self.create_form_fields(form_frame)
        
        # Button frame for actions
        btn_frame = tk.Frame(form_frame, bd=2, relief=tk.RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)
        
        # Create action buttons
        self.create_action_buttons(btn_frame)
        
    def create_form_fields(self, parent):
        """Create all form fields for customer data entry"""
        # Common style for entry fields
        entry_width = 33
        label_font = ("arial", 12, "bold")
        entry_font = ("arial", 10)
        
        # Reference number (read-only)
        tk.Label(parent, text="Customer Reference:", font=label_font, pady=6).grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_ref, width=entry_width, font=entry_font, state="readonly").grid(row=0, column=1)
        
        # Name
        tk.Label(parent, text="Customer Name:", font=label_font, pady=6).grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_name, width=entry_width, font=entry_font).grid(row=1, column=1)
        
        # Address
        tk.Label(parent, text="Address:", font=label_font, pady=6).grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_address, width=entry_width, font=entry_font).grid(row=2, column=1)
        
        # ID Proof Type
        tk.Label(parent, text="ID Proof Type:", font=label_font, pady=6).grid(row=3, column=0, sticky=tk.W)
        id_combo = ttk.Combobox(parent, textvariable=self.var_id_proof, width=31, font=entry_font, state="readonly")
        id_combo["values"] = ("Adhar Card", "Passport", "Driving Licence")
        id_combo.current(0)
        id_combo.grid(row=3, column=1)
        
        # ID Number
        tk.Label(parent, text="ID Card No:", font=label_font, pady=6).grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_id_number, width=entry_width, font=entry_font).grid(row=4, column=1)
        
        # Gender
        tk.Label(parent, text="Gender:", font=label_font, pady=6).grid(row=5, column=0, sticky=tk.W)
        gender_combo = ttk.Combobox(parent, textvariable=self.var_gender, width=31, font=entry_font, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=5, column=1)
        
        # State
        tk.Label(parent, text="State:", font=label_font, pady=6).grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_state, width=entry_width, font=entry_font).grid(row=6, column=1)
        
        # Mobile
        tk.Label(parent, text="Mobile No:", font=label_font, pady=6).grid(row=7, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_mobile, width=entry_width, font=entry_font).grid(row=7, column=1)
        
        # Email
        tk.Label(parent, text="Email Id:", font=label_font, pady=6).grid(row=8, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_email, width=entry_width, font=entry_font).grid(row=8, column=1)
        
        # Nationality
        tk.Label(parent, text="Nationality:", font=label_font, pady=6).grid(row=9, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_nationality, width=entry_width, font=entry_font).grid(row=9, column=1)
        
        # Pincode
        tk.Label(parent, text="Pincode:", font=label_font, pady=6).grid(row=10, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.var_pincode, width=entry_width, font=entry_font).grid(row=10, column=1)
    
    def create_action_buttons(self, parent):
        """Create action buttons for form operations"""
        # Common button style
        btn_style = {
            "font": ("arial", 12, "bold"),
            "bg": "black",
            "fg": "white",
            "width": 9
        }
        
        # Add button
        add_btn = tk.Button(parent, text="Add", command=self.add_data, **btn_style)
        add_btn.grid(row=0, column=0, padx=1, pady=1)
        
        # Update button
        update_btn = tk.Button(parent, text="Update", command=self.update, **btn_style)
        update_btn.grid(row=0, column=1, padx=1, pady=1)
        
        # Delete button
        delete_btn = tk.Button(parent, text="Delete", command=self.delete, **btn_style)
        delete_btn.grid(row=0, column=2, padx=1, pady=1)
        
        # Reset button
        reset_btn = tk.Button(parent, text="Reset", command=self.reset, **btn_style)
        reset_btn.grid(row=0, column=3, padx=1, pady=1)
    
    def create_search_view(self):
        """Create search panel and data table view"""
        # Frame for search and view
        view_frame = ttk.LabelFrame(
            self.root,
            text="View and Search Customer Details",
            padding=10
        )
        view_frame.place(x=435, y=50, width=860, height=490)
        
        # Create search controls
        search_label = tk.Label(
            view_frame,
            text="Search By:",
            font=("arial", 12, "bold"),
            bg="black",
            fg="white"
        )
        search_label.grid(row=0, column=0, sticky=tk.W, padx=2)
        
        # Search type dropdown
        search_combo = ttk.Combobox(
            view_frame,
            textvariable=self.var_search_by,
            font=("arial", 13),
            width=20,
            state="readonly"
        )
        search_combo["values"] = ("Id Card No", "Mobile", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2)
        
        # Search text entry
        search_entry = ttk.Entry(
            view_frame,
            textvariable=self.var_search_text,
            width=25,
            font=("arial", 13)
        )
        search_entry.grid(row=0, column=2, padx=2)
        
        # Search button
        search_btn = tk.Button(
            view_frame,
            text="Search",
            command=self.search_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="white",
            width=9
        )
        search_btn.grid(row=0, column=3, padx=1, pady=1)
        
        # Show all button
        show_btn = tk.Button(
            view_frame,
            text="Show All",
            command=self.fetch_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="white",
            width=9
        )
        show_btn.grid(row=0, column=4, padx=1, pady=1)
        
        # Create data table
        self.create_data_table(view_frame)
    
    def create_data_table(self, parent):
        """Create the data table for displaying customer records"""
        # Table frame
        table_frame = tk.Frame(parent, bd=2, relief=tk.RIDGE)
        table_frame.place(x=0, y=50, width=845, height=410)
        
        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        
        # Define columns
        columns = (
            "ref", "name", "address", "id_proof_type", "id_no", 
            "gender", "state", "pincode", "mobile", "email", "nationality"
        )
        
        # Create treeview
        self.customer_table = ttk.Treeview(
            table_frame,
            columns=columns,
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )
        
        # Configure scrollbars
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)
        
        # Configure column headings
        column_headers = {
            "ref": "Reference No",
            "name": "Name",
            "address": "Address",
            "id_proof_type": "ID Type",
            "id_no": "ID No",
            "gender": "Gender",
            "state": "State",
            "pincode": "Pincode",
            "mobile": "Mobile",
            "email": "Email ID",
            "nationality": "Nationality"
        }
        
        column_widths = {
            "ref": 100,
            "name": 150,
            "address": 200,
            "id_proof_type": 100,
            "id_no": 100,
            "gender": 100,
            "state": 100,
            "pincode": 100,
            "mobile": 100,
            "email": 150,
            "nationality": 100
        }
        
        # Set column headers and widths
        for col in columns:
            self.customer_table.heading(col, text=column_headers[col])
            self.customer_table.column(col, width=column_widths[col])
        
        # Show headings and pack table
        self.customer_table["show"] = "headings"
        self.customer_table.pack(fill=tk.BOTH, expand=1)
        
        # Bind selection event
        self.customer_table.bind("<ButtonRelease-1>", self.get_selected_record)
    
    def db_connection(self):
        """Create and return database connection"""
        try:
            load_dotenv()
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"), 
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE")
            )
            return conn
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}", parent=self.root)
            return None
    
    def fetch_data(self):
        """Fetch all customer data from database"""
        conn = self.db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            
            # Clear existing data
            self.customer_table.delete(*self.customer_table.get_children())
            
            # Insert new data
            for row in rows:
                self.customer_table.insert("", tk.END, values=row)
                
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)
            conn.close()
    
    def add_data(self):
        """Add new customer record to database"""
        # Validate required fields
        if not self.var_mobile.get() or not self.var_id_number.get():
            messagebox.showerror("Error", "Mobile and ID Number are required fields", parent=self.root)
            return
            
        conn = self.db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            
            # Prepare data tuple
            data = (
                self.var_ref.get(),
                self.var_name.get(),
                self.var_address.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_gender.get(),
                self.var_state.get(),
                self.var_pincode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get()
            )
            
            # Execute insert query
            insert_query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, data)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success", "Customer added successfully", parent=self.root)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error adding customer: {str(e)}", parent=self.root)
        finally:
            conn.close()
    
    def get_selected_record(self, event=None):
        """Get selected record from table and populate form fields"""
        selected_row = self.customer_table.focus()
        if not selected_row:
            return
            
        data = self.customer_table.item(selected_row)
        row = data.get("values", [])
        
        if not row:
            return
            
        # Populate form fields with selected data
        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_address.set(row[2])
        self.var_id_proof.set(row[3])
        self.var_id_number.set(row[4])
        self.var_gender.set(row[5])
        self.var_state.set(row[6])
        self.var_pincode.set(row[7])
        self.var_mobile.set(row[8])
        self.var_email.set(row[9])
        self.var_nationality.set(row[10])
    
    def update(self):
        """Update selected customer record"""
        # Validate required fields
        if not self.var_mobile.get():
            messagebox.showerror("Error", "Mobile number is required", parent=self.root)
            return
            
        conn = self.db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            
            # Prepare update query and data
            update_query = """UPDATE customer SET 
                name = %s, 
                address = %s, 
                `id proof type` = %s, 
                `id no` = %s, 
                gender = %s, 
                state = %s, 
                pincode = %s, 
                mobile = %s, 
                email = %s, 
                nationality = %s 
                WHERE ref = %s"""
                
            data = (
                self.var_name.get(),
                self.var_address.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_gender.get(),
                self.var_state.get(),
                self.var_pincode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_ref.get()
            )
            
            # Execute update query
            cursor.execute(update_query, data)
            
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Customer details updated successfully", parent=self.root)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error updating customer: {str(e)}", parent=self.root)
        finally:
            conn.close()
    
    def delete(self):
        """Delete selected customer record"""
        selected = self.customer_table.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a customer to delete", parent=self.root)
            return
            
        # Confirm deletion
        confirm = messagebox.askyesno("Delete Customer", "Are you sure you want to delete this customer?", parent=self.root)
        if not confirm:
            return
            
        conn = self.db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            
            # Execute delete query
            delete_query = "DELETE FROM customer WHERE ref = %s"
            cursor.execute(delete_query, (self.var_ref.get(),))
            
            conn.commit()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting customer: {str(e)}", parent=self.root)
        finally:
            conn.close()
    
    def reset(self):
        """Reset all form fields"""
        # Generate new reference number
        self.var_ref.set(str(random.randint(1, 99999)))
        
        # Clear other fields
        self.var_name.set("")
        self.var_address.set("")
        self.var_id_proof.set("Adhar Card")
        self.var_id_number.set("")
        self.var_gender.set("Male")
        self.var_state.set("")
        self.var_pincode.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
    
    def search_data(self):
        """Search customer records based on criteria"""
        if not self.var_search_text.get():
            messagebox.showerror("Error", "Please enter search text", parent=self.root)
            return
            
        conn = self.db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            
            # Map search by options to database column names
            search_column = {
                "Id Card No": "id no",
                "Mobile": "mobile",
                "Name": "name"
            }.get(self.var_search_by.get(), "id no")
            
            # Prepare search query with wildcard
            search_query = f"SELECT * FROM customer WHERE `{search_column}` LIKE %s"
            cursor.execute(search_query, (f"%{self.var_search_text.get()}%",))
            
            rows = cursor.fetchall()
            
            if not rows:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)
                return
                
            # Update table with results
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error searching data: {str(e)}", parent=self.root)
        finally:
            conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerManager(root)
    root.mainloop()