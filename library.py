import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        self.Member_var = StringVar()
        self.prn_no_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.phone_var = StringVar()
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.laterfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        frame = Frame(self.root, bd=12, relief=RIDGE,
                      padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=410)

        lbtitle = Label(self.root, text="Library Management System", bg="powder blue", fg="green",
                        bd=20, relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue",
                                   fg="green", bd=20, relief=RIDGE, font=("Times New Roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=390)

        lbMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=(
            "Times New Roman", 15, "bold"), padx=2, pady=6)
        lbMember.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(DataFrameLeft, font=(
            "Times New Roman", 15, "bold"), textvariable=self.Member_var, width=23, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lbPRN_No = Label(DataFrameLeft, font=("Arial", 13, "bold"),
                         text="PRN NO", padx=2, pady=6, bg="powder blue")
        lbPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.prn_no_var, width=23)
        txtPRN_NO.grid(row=1, column=1)

        lbId_no = Label(DataFrameLeft, bg="powder blue", font=(
            "Arial", 13, "bold"), text="Id No", padx=2, pady=6)
        lbId_no.grid(row=2, column=0, sticky=W)
        txtId_no = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.id_var, width=23)
        txtId_no.grid(row=2, column=1)

        LbFirstName = Label(DataFrameLeft, font=(
            "Arial", 13, "bold"), bg="powder blue", text="First Name", padx=2, pady=6)
        LbFirstName.grid(row=3, column=0, stick=W)
        txtFirstName = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.firstname_var, width=23)
        txtFirstName.grid(row=3, column=1)

        LbSurname = Label(DataFrameLeft, bg="powder blue", font=(
            "Arial", 13, "bold"), text="Surname", padx=2, pady=6)
        LbSurname.grid(row=4, column=0, sticky=W)
        txtSurname = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.lastname_var, width=23)
        txtSurname.grid(row=4, column=1)

        LbA1 = Label(DataFrameLeft, text="Address 1", font=(
            "Arial", 13, "bold"), bg="powder blue", padx=2, pady=6)
        LbA1.grid(row=5, column=0, sticky=W)
        txtA1 = Entry(DataFrameLeft, font=("Arial", 14, "bold"),
                      textvariable=self.address1_var, width=23)
        txtA1.grid(row=5, column=1)

        LbA2 = Label(DataFrameLeft, text="Address 2", font=(
            "Arial", 13, "bold"), bg="powder blue", padx=2, pady=6)
        LbA2.grid(row=6, column=0, sticky=W)
        txtA2 = Entry(DataFrameLeft, font=("Arial", 14, "bold"),
                      textvariable=self.address2_var, width=23)
        txtA2.grid(row=6, column=1)

        Lbp_code = Label(DataFrameLeft, text="Postal code", font=(
            "Arial", 13, "bold"), bg="powder blue", padx=2, pady=6)
        Lbp_code.grid(row=7, column=0, sticky=W)
        txtp_code = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.postcode_var, width=23)
        txtp_code.grid(row=7, column=1)

        Lbph_no = Label(DataFrameLeft, text="Phone Number", font=(
            "Arial", 13, "bold"), bg="powder blue", padx=2, pady=6)
        Lbph_no.grid(row=8, column=0, sticky=W)
        txtph_no = Entry(DataFrameLeft, font=("Arial", 14, "bold"),
                         textvariable=self.phone_var, width=23)
        txtph_no.grid(row=8, column=1)

        LbBook_id = Label(DataFrameLeft, text="Book Id", font=(
            "Arial", 13, "bold"), bg="powder blue", padx=2, pady=6)
        LbBook_id.grid(row=0, column=2, sticky=W)
        txtBook_id = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.book_id_var, width=23)
        txtBook_id.grid(row=0, column=3)

        LbBook_title = Label(DataFrameLeft, text="Book Title", font=(
            "Arial", 13, "bold"), bg="Powder blue", padx=2, pady=6)
        LbBook_title.grid(row=1, column=2, sticky=W)
        txtBook_title = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.book_title_var, width=23)
        txtBook_title.grid(row=1, column=3)

        LbAuthor = Label(DataFrameLeft, text="Author Name", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.author_var, width=23)
        txtAuthor.grid(row=2, column=3)

        LbDateborrowed = Label(DataFrameLeft, text="Date Borrowed", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbDateborrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.dateborrowed_var, width=23)
        txtDateBorrowed.grid(row=3, column=3)

        LbDate_due = Label(DataFrameLeft, text="Date Due", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbDate_due.grid(row=4, column=2, sticky=W)
        txtDate_due = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.datedue_var, width=23)
        txtDate_due.grid(row=4, column=3)

        LbDateOnBook = Label(DataFrameLeft, text="Days On Book", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbDateOnBook.grid(row=5, column=2, sticky=W)
        txtDateOnBook = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.daysonbook_var, width=23)
        txtDateOnBook.grid(row=5, column=3)

        LbLateReturnFine = Label(DataFrameLeft, text="Late Return Fine", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLRFine = Entry(DataFrameLeft, font=("Arial", 14, "bold"),
                          textvariable=self.laterfine_var, width=23)
        txtLRFine.grid(row=6, column=3)

        LbDateOverDue = Label(DataFrameLeft, text="Date Over Due", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbDateOverDue.grid(row=7, column=2, sticky=W)
        txtDODue = Entry(DataFrameLeft, font=("Arial", 14, "bold"),
                         textvariable=self.dateoverdue_var, width=23)
        txtDODue.grid(row=7, column=3)

        LbActualPrice = Label(DataFrameLeft, text="Actual Price", font=(
            "Arial", 14, "bold"), bg="powder blue", padx=2, pady=6)
        LbActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=(
            "Arial", 14, "bold"), textvariable=self.finalprice_var, width=23)
        txtActualPrice.grid(row=8, column=3)

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                                    fg="green", bd=20, relief=RIDGE, font=("Times New Roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=390)

        self.txtBox = Text(DataFrameRight, font=(
            "Arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        ListScrollBar=Scrollbar(DataFrameRight)
        ListScrollBar.grid(row=0,column=1,sticky=NS)

        ListBooks = [
    "To Kill a Mockingbird","1984","Pride and Prejudice","The Great Gatsby","Moby-Dick","Brave New World","The Catcher in the Rye","Jane Eyre","Crime and Punishment","The Hobbit","The Lord of the Rings","The Odyssey","Frankenstein","One Hundred Years of Solitude","Wuthering Heights","The Picture of Dorian Gray","War and Peace","Anna Karenina","Don Quixote","Little Women","Hamlet","The Adventures of Sherlock Holmes","Les Misérables",
    "The Brothers Karamazov","The Grapes of Wrath","The Scarlet Letter","Alice's Adventures in Wonderland","The Count of Monte Cristo","Gulliver's Travels","Middlemarch","Heart of Darkness","Great Expectations","The Canterbury Tales","The Iliad","The Divine Comedy","Slaughterhouse-Five","The Sun Also Rises","Catch-22",
    "The Sound and the Fury","Beloved","Invisible Man","The Stranger","Lord of the Flies","A Clockwork Orange","The Handmaid's Tale","The Bell Jar","Mrs. Dalloway","Catch-22","Walden","The Old Man and the Sea","On the Road","Fahrenheit 451","The Grapes of Wrath","A Tale of Two Cities","Ulysses","Moby-Dick","The Wind in the Willows"
]
        def SelectBook(event=''):
            value=str(ListBox.get(ListBox.curselection()))
            x=value
            if(x=="To Kill a Mockingbird"):
                self.book_id_var.set("BKID6666")
                self.book_title_var.set('philosophy')
                self.author_var.set("Jack")
                 
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterfine_var.set('560')
                self.dateoverdue_var.set('NO')
                self.finalprice_var.set('560')


        ListBox=Listbox(DataFrameRight,font=("Arial",12,'bold'),width=32,height=16)
        ListBox.bind("<<ListboxSelect>>",SelectBook)
        ListBox.grid(row=0,column=0,padx=4)
        ListScrollBar.config(command=ListBox.yview)
        
        for item in ListBooks:
            ListBox.insert(END,item)

# Buttons Frame
        FrameButton = Frame(self.root, bd=12, relief=RIDGE,
                            padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(FrameButton, command=self.adda_data, text="Add Data", font=(
            "Times New Roman", 12, "bold"), width=25, bg="green", fg="white")
        btnAddData.grid(row=0, column=5)

        btnShowData = Button(FrameButton,command= self.showData, text="Show Data", width=25, bg="blue", font=(
            "Times New Roman", 12, "bold"), fg="white")
        btnShowData.grid(row=0, column=6)

        btnUpdate = Button(FrameButton,command= self.update, text="Update", bg="blue", fg="white", font=(
            "Times New Roman", 12, "bold"), width=25)
        btnUpdate.grid(row=0, column=7)

        btndelete = Button(FrameButton, text="Delete",command=self.delete, bg="red", fg="white", font=(
            "Times New Roman", 12, "bold"), width=25)
        btndelete.grid(row=0, column=8)

        btnreset = Button(FrameButton,command=self.reset, text="Reset", bg="blue", fg="white", font=(
            "Times New Roman", 12, "bold"), width=25)
        btnreset.grid(row=0, column=9)

        btnexit = Button(FrameButton,command=self.iExit, text="Exit", bg="red", fg="white", font=(
            "Times New Roman", 12, "bold"), width=25)
        btnexit.grid(row=0, column=10, padx=10, pady=10)

# information frame
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg='powder blue')
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","idno","firstname","lastname","address1","address2","postid","phonenumber","bookid","booktitle","author","dateborrowed","datedue","daysonbook", "latereturnfine","dateoverdue","finalprice"))
        # Pack Scrollbars
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        # Column Headings"me
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No")
        self.library_table.heading("idno", text="Id No")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Postalcode")
        self.library_table.heading("phonenumber", text="Phone Number")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("daysonbook", text="Days On Book")
        self.library_table.heading(
            "latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("phonenumber", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("daysonbook", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data()
        self.library_table.bind("<<>ButtonRelease-1>",self)

    def new_method(self, FrameDetails):
        Table_frame = Frame(FrameDetails, bd=6,
                            relief='ridge', bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        # Scrollbars
        xscroll = Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = Scrollbar(Table_frame, orient=VERTICAL)

        # Treeview widget
        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "idno", "firstname", "lastname", "address1", "address2", "postid", "phonenumber", "bookid", "booktitle", "author", "dateborrowed", "datedue", "daysonbook", "latereturnfine", "dateoverdue", "finalprice"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        self.fetch_data()
        self.library_table.bind("<<>>ButtonRelease-1>",self.get_cursor)

    def adda_data(self):  
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="****",
                database="LibraryMng"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO library VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Member_var.get(),
                self.prn_no_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.phone_var.get(),
                self.book_id_var.get(),
                self.book_title_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.laterfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get()
            ))
            conn.commit()
            self.fetch_data()

            messagebox.showinfo("Success","Member has been added successfully") 


        except mysql.connector.Error as err:   
                     messagebox.showerror("Error", f"Error: {err}")

        finally:
        # Close connection and cursor in finally block to ensure they are always closed
            if 'conn' in locals() and conn.is_connected():
             my_cursor.close()
             conn.close()

    def update(self):

        try:
          conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="*****",
                database="LibraryMng"
            )
          my_cursor = conn.cursor()
          my_cursor.execute("UPDATE library SET Member=%s,id=%s,first_name=%s,last_name=%s,address1=%s,address2=%s,postal_code=%s,phone_no=%s,book_id=%s,book_title=%s,author_name=%s,date_borrowed=%s,date_due=%s,days_on_book=%s,late_return_fine=%s,date_over_due=%s,actual_price=%s where PRN_NO=%s", (
                self.Member_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.phone_var.get(),
                self.book_id_var.get(),
                self.book_title_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.laterfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get(),
                self.prn_no_var.get(),
            ))
          conn.commit()
          self.fetch_data()
          self.reset()
          

          messagebox.showinfo("Success","Member has been updated")
         
        except mysql.connector.Error as err:   
                     messagebox.showerror("Error", f"Error: {err}")

        finally:
        # Close connection and cursor in finally block to ensure they are always closed
            if 'conn' in locals() and conn.is_connected():
             my_cursor.close()
             conn.close()


    def fetch_data(self):
         conn=mysql.connector.connect( host="localhost",
                username="root",
                password="*****",
                database="LibraryMng")  
         my_cursor=conn.cursor()
         my_cursor.execute("select * from library")
         rows=my_cursor.fetchall()

         if len(rows)!=0:
              self.library_table.delete(*self.library_table.get_children())
              for i in rows:
                   self.library_table.insert("",END,values=i)
                   conn.commit()
                   conn.close()       

    def get_cursor(self,events=""):
         cursor_row=self.library_table.focus()
         content=self.library_table.item(cursor_row)
         row=content['values']

         self.Member_var.set(row[0])
         self.prn_no_var.set(row[1])
         self.id_var.set(row[2])
         self.firstname_var.set(row[3])
         self.lastname_var.set(row[4])
         self.address1_var.set(row[5])
         self.address2_var.set(row[6])
         self.postcode_var.set(row[7])
         self.phone_var.set(row[8])
         self.book_id_var.set(row[9])
         self.book_title_var.set(row[10])
         self.author_var.set(row[11])
         self.dateborrowed_var.set(row[12])
         self.datedue_var.set(row[13])
         self.daysonbook_var.set(row[14])
         self.laterfine_var.set(row[15])
         self.dateoverdue_var.set(row[16])
         self.finalprice_var.set(row[17])   
    
    def showData(self):
         self.txtBox.insert(END,"Member Type:\t\t"+self.Member_var.get()+"\n")
         self.txtBox.insert(END,"PRN NO:\t\t"+self.prn_no_var.get()+"\n")
         self.txtBox.insert(END,"Id No:\t\t"+self.id_var.get()+"\n")
         self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
         self.txtBox.insert(END,"Surname:\t\t"+self.lastname_var.get()+"\n")
         self.txtBox.insert(END,"Address 1:\t\t"+self.address1_var.get()+"\n")
         self.txtBox.insert(END,"Address 2:\t\t"+self.address2_var.get()+"\n")
         self.txtBox.insert(END,"Postal Code:\t\t"+self.postcode_var.get()+"\n")
         self.txtBox.insert(END,"Phone Number:\t\t"+self.phone_var.get()+"\n")
         self.txtBox.insert(END,"Book Id:\t\t"+self.book_id_var.get()+"\n")
         self.txtBox.insert(END,"Book Title:\t\t"+self.book_title_var.get()+"\n")
         self.txtBox.insert(END,"Author Name:\t\t"+self.author_var.get()+"\n")
         self.txtBox.insert(END,"Date Borrowed:\t\t"+self.dateborrowed_var.get()+"\n")
         self.txtBox.insert(END,"Date Due:\t\t"+self.datedue_var.get()+"\n")
         self.txtBox.insert(END,"Days with Book:\t\t"+self.daysonbook_var.get()+"\n")
         self.txtBox.insert(END,"Late Return Fine:\t\t"+self.lastname_var.get()+"\n")
         self.txtBox.insert(END,"Date Over Due:\t\t"+self.dateoverdue_var.get()+"\n")
         self.txtBox.insert(END,"Actual Price:\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
                self.Member_var.set('')
                self.prn_no_var.set('')
                self.id_var.set('')
                self.firstname_var.set('')
                self.lastname_var.set('')
                self.address1_var.set('')
                self.address2_var.set('')
                self.postcode_var.set('')
                self.phone_var.set('')
                self.book_id_var.set('')
                self.book_title_var.set('')
                self.author_var.set('')
                self.dateborrowed_var.set('')
                self.datedue_var.set('')
                self.daysonbook_var.set('')
                self.laterfine_var.set('')
                self.dateoverdue_var.set('')
                self.finalprice_var.set('')
                self.txtBox.delete('1.0',END)

    def iExit(self):
         iExit=messagebox.askyesno("Library management system","Do you want to exit")
         if iExit>0:
              self.root.destroy()
              return

    def delete(self):
     if self.prn_no_var.get() == "" or self.id_var.get() == "":
        messagebox.showerror("Error", "First select the Member")
     else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="*****",
                database="LibraryMng"
            )
            my_cursor = conn.cursor()
            query = "DELETE FROM library WHERE PRN_NO = %s"
            value = (self.prn_no_var.get(),)  # Define 'value' as a tuple
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()

            messagebox.showinfo("Success", "Member has been deleted")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            if 'conn' in locals() and conn.is_connected():
                my_cursor.close()
                conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
