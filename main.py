import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *

class Login_Page(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Setting up the window
        self.master = master
        self.master.title("Dreamhouse Rental Business Login")
        self.master.geometry("400x400")
        self.master.minsize(400,400)

        self.titleframe = tk.Frame(self.master, bg="#614051")
        self.titleframe.pack(side="top", fill="x")
        
        self.titlelabel = tk.Label(self.titleframe, text="WELCOME TO DREAMHOUSE RENTALS", font=("Helvetica", 15), bg="#614051", fg="white")
        self.titlelabel.pack(pady=20)

        self.contentframe = tk.Frame(self.master, bg="#A08C96")
        self.contentframe.pack(side="top", fill="both", expand=True)

        # Creating a label for the dropdown
        self.select_role_label = tk.Label(self.contentframe, text="Select Role:", font=("Helvetica", 12), bg="#A08C96")
        self.select_role_label.grid(row=1, column=1, pady=10, padx=2)

        # Creating a dropdown for the roles
        self.role_options = ["Staff", "Owner", "Client"]
        self.role_var = tk.StringVar()
        self.role_dropdown = ttk.Combobox(self.contentframe, textvariable=self.role_var, values=self.role_options, state="readonly")
        self.role_dropdown.grid(row=1, column=2, pady=5, padx=2)

        # Creating a label for the ID entry
        self.id_label = tk.Label(self.contentframe, text="ID:", font=("Helvetica", 12), bg="#A08C96")
        self.id_label.grid(row=2, column=1)

        # Creating an entry for the ID
        self.id_entry = tk.Entry(self.contentframe, width=30)
        self.id_entry.grid(row=2, column=2)

        # Creating a button to log in
        self.login_button = tk.Button(self.contentframe, text="Log In", font=("Helvetica", 12), command=self.login)
        self.login_button.grid(row=3, column=2, pady=4)

        self.regtitle = tk.Label(self.contentframe, text="Don't have an account?", font=("Helvetica", 12), bg="#A08C96")
        self.regtitle.grid(row=4, column=1, pady=4)

        # Creating a button to register
        self.register_button = tk.Button(self.contentframe, text="Register", font=("Helvetica", 12), command=self.register)
        self.register_button.grid(row=4, column=2, pady=4)

    def login(self):
        role = self.role_var.get()
        id = self.id_entry.get()

        # TODO: Check if the ID is valid for the selected role and log in if it is

    def register(self):
        role = self.role_var.get()
        id = self.id_entry.get()

        # TODO: Register the ID for the selected role
        if role == "Staff":
            # Creating a new window for staff registration
            staff_reg_window = tk.Toplevel(self.master)
            staff_reg_window.title("Staff Registration Form")
            staff_reg_window.geometry("600x500")
            staff_reg_window.resizable(False, False)

            #frame 1 for staff personal details
            staff_f1= tk.Frame(staff_reg_window)
            staff_f1.pack(side="left", anchor="nw")

            # staff name
            staff_name_label = tk.Label(staff_f1, text="Staff Name:", font=("Helvetica", 10))
            staff_name_label.grid(column=0, row=0)

            staff_name_entry = tk.Entry(staff_f1, width=30)
            staff_name_entry.grid(column=1, row=0)

            # staff sex
            staff_sex_label = tk.Label(staff_f1, text="Staff Sex:", font=("Helvetica", 10))
            staff_sex_label.grid(column=0, row=1)

            staff_sex_radio_frame= tk.Frame(staff_f1)
            staff_sex_radio_frame.grid(row=1, column=1)

            staff_sex_var = tk.StringVar()
            staff_sex_male_radio = tk.Radiobutton(staff_sex_radio_frame, text="M", variable=staff_sex_var, value="M")
            staff_sex_female_radio = tk.Radiobutton(staff_sex_radio_frame, text="F", variable=staff_sex_var, value="F")
            staff_sex_male_radio.pack(side="left")
            staff_sex_female_radio.pack(side="left")

            # staff dob
            dob_label = tk.Label(staff_f1, text="Date of Birth:", font=("Helvetica", 10))
            dob_label.grid(row=2, column=0)

            self.dob_entry = DateEntry(staff_f1, width=12, background='darkblue',foreground='white', date_pattern='yyyy-mm-dd')
            self.dob_entry.grid(row=2, column=1)

            # staff salary
            dob_label = tk.Label(staff_f1, text="Salary:", font=("Helvetica", 10))
            dob_label.grid(row=3, column=0)

            salaryval = tk.IntVar()

            staff_name_entry = tk.Entry(staff_f1, width=30, textvariable=salaryval)
            staff_name_entry.grid(column=1, row=3)

            # frame 2 for branch details of staff
            staff_f2= tk.Frame(staff_reg_window)
            staff_f2.pack(side="right", anchor="ne")
            
            # branch number
            branch_name_label = tk.Label(staff_f2, text="Branch Number:", font=("Helvetica", 10))
            branch_name_label.grid(column=0, row=0)

            branch_name_entry = tk.Entry(staff_f2, width=30)
            branch_name_entry.grid(column=1, row=0)

            # branch address
            branch_addr_label = tk.Label(staff_f2, text="Branch Address:", font=("Helvetica", 10))
            branch_addr_label.grid(column=0, row=1)

            branch_addr_entry = tk.Entry(staff_f2, width=30)
            branch_addr_entry.grid(column=1, row=1)

            # branch numbers
            branch_num_val = tk.IntVar()
            branch_num_label = tk.Label(staff_f2, text="Telephone Number:", font=("Helvetica", 10))
            branch_num_label.grid(column=0, row=2)

            branch_num_entry = tk.Entry(staff_f2, width=30, textvariable=branch_num_val)
            branch_num_entry.grid(column=1, row=2)

            # Creating a button to submit staff registration
            # submit_button = tk.Button(staff_reg_window, text="Submit", font=("Helvetica", 12))
            # submit_button.pack(pady=10)

        elif role == "Owner":
            owner_reg_window = tk.Toplevel(self.master)
            owner_reg_window.title("Owner Registration Form")
            owner_reg_window.geometry("400x300")
            owner_reg_window.resizable(False, False)

            #labels and entries for Property registration form
            
            top_frame = tk.Frame(owner_reg_window)
            top_frame.pack(side = "top")
            
            form_name1 = tk.Label(top_frame, text="DreamHome", font=("Helvetica", 12))
            form_name1.pack()

            form_name2 = tk.Label(top_frame, text="Property Registration Form", font=("Helvetica", 12))
            form_name2.pack()

            top_left_frame = tk.Frame(owner_reg_window)
            top_left_frame.pack(side = "left")

            owner_prop_num_label = tk.Label(top_left_frame, text="Property Number: ", font=("Helvetica", 12))
            # owner_prop_num_label.pack()

            owner_prop_num_entry = tk.Entry(top_left_frame, width=30)
            # owner_prop_num_entry.pack()

            owner_prop_num_label.grid(row=1, column=1)
            owner_prop_num_entry.grid(row=1, column=2)





            








if __name__ == "__main__":
    root = tk.Tk()
    login_page = Login_Page(root)
    login_page.pack()
    root.mainloop()
