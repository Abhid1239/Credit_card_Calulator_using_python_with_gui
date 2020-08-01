from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root = Tk()
root.title("CREDIT CARD CALCULATOR") screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1300
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2) root.geometry('%dx%d+%d+%d' % (width, height, x, y)) root.resizable(0, 0)
#==========================METHODS=============================== def Database():
global conn, cursor
conn = sqlite3.connect('CREDITCC.db') cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS credit(NAME TEXT,CREDIT_NO TEXT,CVV TEXT, EXPIRY_DATE TEXT,LOAN_AMOUNT TEXT, INETEREST_RATE TEXT,REPAYEMENT_TENURE TEXT,PRINCIPAL_AMOUNT TEXT,INTEREST_AMOUNT TEXT,EMI TEXT)")
def Create():
   
 if NAME.get() == "" or CREDIT_NO.get() == "" or CVV.get() == "" or EXPIRY_DATE.get() == "" or LOAN_AMOUNT.get() == "" or INETEREST_RATE.get() == "" or REPAYEMENT_TENURE =="" or PRINCIPAL_AMOUNT=="" or INTEREST_AMOUNT =="" or EMI=="":
txt_result.config(text="Please complete the required field!", fg="red") else:
Database()
cursor.execute("INSERT INTO `credit` (NAME, CREDIT_NO, CVV, EXPIRY_DATE, LOAN_AMOUNT, INETEREST_RATE, REPAYEMENT_TENURE, PRINCIPAL_AMOUNT, INTEREST_AMOUNT, EMI)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(NAME.get()), str(CREDIT_NO.get()), str(CVV.get()),
str(EXPIRY_DATE.get()),str(LOAN_AMOUNT.get()), str(REPAYEMENT_TENURE.get()), str(INTEREST_AMOUNT.get()), str(EMI.get())))
conn.commit()
NAME,set("") CREDIT_NO,set("")
CVV,set("") EXPIRY_DATE,set("") LOAN_AMOUNT,set("") INETEREST_RATE,set("") REPAYEMENT_TENURE,set("") PRINCIPAL_AMOUNT,set("") INTEREST_AMOUNT,set("") EMI,set("")
cursor.close()
conn.close()
txt_result.config(text="Create a data!", fg="green")
str(INETEREST_RATE.get()), str(PRINCIPAL_AMOUNT.get()),
def Read():
tree.delete(*tree.get_children())
Database()
cursor.execute("SELECT * FROM `credit` ORDER BY 'NAME' ASC ") fetch = cursor.fetchall()
for data in fetch:
tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
cursor.close() conn.close()

 txt_result.config(text="Successfully read the data from database", fg="black")
def Exit():
result = tkMessageBox.askquestion('CREDIT CARD CALCULATOR', 'Are you sure you
want to exit?', icon="warning") if result == 'yes':
root.destroy() exit()
#===========================VARIABLES============================ NAME = StringVar()
CREDIT_NO = StringVar()
CVV = StringVar()
EXPIRY_DATE = StringVar() LOAN_AMOUNT= StringVar() INETEREST_RATE = StringVar() REPAYEMENT_TENURE = StringVar() PRINCIPAL_AMOUNT = StringVar() INTEREST_AMOUNT = StringVar() EMI = StringVar()
#============================FRAME=============================== Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise") Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450) Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise") Buttons.pack(side=BOTTOM)
#===========================LABEL_WIDGET========================= txt_title = Label(Top, width=900, font=('arial', 24), text = "CREDIT CARD CALCULATOR")
txt_title.pack()
txt_NAME = Label(Forms, text="NAME:", font=('arial', 16), bd=15) txt_NAME.grid(row=0, stick="w")
txt_CREDIT_NO = Label(Forms, text="CREDIT_NO:", font=('arial', 16), bd=15) txt_CREDIT_NO.grid(row=1, stick="w")
txt_CVV = Label(Forms, text="CVV:", font=('arial', 16), bd=15)

 txt_CVV.grid(row=2, stick="w")
txt_EXPIRY_DATE = Label(Forms, text="EXPIRY_DATE:", font=('arial', 16), bd=15) txt_EXPIRY_DATE.grid(row=3, stick="w")
txt_LOAN_AMOUNT= Label(Forms, text="LOAN_AMOUNT:", font=('arial', 16), bd=15) txt_LOAN_AMOUNT.grid(row=4, stick="w")
txt_INETEREST_RATE = Label(Forms, text="INETEREST_RATE:", font=('arial', 16), bd=15)
txt_INETEREST_RATE.grid(row=5, stick="w")
txt_REPAYEMENT_TENURE = Label(Forms, text="REPAYEMENT_TENURE:", font=('arial', 16), bd=15)
txt_REPAYEMENT_TENURE.grid(row=6,stick="w")
txt_PRINCIPAL_AMOUNT = Label(Forms, text="PRINCIPAL_AMOUNT:", font=('arial', 16), bd=15)
txt_PRINCIPAL_AMOUNT.grid(row=7, stick="w")
txt_INTEREST_AMOUNT= Label(Forms, text="INTEREST_AMOUNT:", font=('arial', 16), bd=15)
txt_INTEREST_AMOUNT.grid(row=8, stick="w")
txt_EMI = Label(Forms, text="EMI:", font=('arial', 16), bd=15)
txt_EMI.grid(row=9, stick="w")
txt_result = Label(Buttons) txt_result.pack(side=TOP)
#========================ENTRY_WIDGET============================ NAME = Entry(Forms, textvariable=NAME, width=30)
NAME.grid(row=0, column=1)
CREDIT_NO = Entry(Forms, textvariable=CREDIT_NO, width=30) CREDIT_NO.grid(row=1, column=1)
CVV = Entry(Forms, textvariable=CVV, width=30, show="*") CVV.grid(row=2, column=1)
EXPIRY_DATE = Entry(Forms, textvariable=EXPIRY_DATE, width=30) EXPIRY_DATE.grid(row=3,column=1)
LOAN_AMOUNT = Entry(Forms, textvariable=LOAN_AMOUNT, width=30) LOAN_AMOUNT.grid(row=4, column=1)
INETEREST_RATE= Entry(Forms, textvariable=INETEREST_RATE, width=30) INETEREST_RATE.grid(row=5, column=1)
REPAYEMENT_TENURE= Entry(Forms, width=30)
REPAYEMENT_TENURE.grid(row=6, column=1) PRINCIPAL_AMOUNT=Entry(Forms, width=30,state=DISABLED) PRINCIPAL_AMOUNT.grid(row=7, column=1)
textvariable=REPAYEMENT_TENURE, textvariable=PRINCIPAL_AMOUNT,

 INTEREST_AMOUNT=Entry(Forms, textvariable=INTEREST_AMOUNT, width=30,state=DISABLED)
INTEREST_AMOUNT.grid(row=8, column=1)
EMI=Entry(Forms, textvariable=EMI, width=30,state=DISABLED)
EMI.grid(row=9, column=1)
#===========================BUTTONS_WIDGET===================== btn_pay=Button(Buttons, width=10,text="Calculated", command=lambda: calc(PRINCIPAL_AMOUNT,INTEREST_AMOUNT,EMI ))
btn_pay.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Create", command=Create) btn_update.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read ) btn_read.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit) btn_exit.pack(side=LEFT)
#============================LIST_WIDGET========================== scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("NAME", "CREDIT_NO","CVV", "EXPIRY_DATE", "LOAN_AMOUNT", "INETEREST_RATE", "REPAYEMENT_TENURE", "PRINCIPAL_AMOUNT", "INTEREST_AMOUNT", "EMI"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set) scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('NAME', text="NAME", anchor=W)
tree.heading('CREDIT_NO', text="CREDIT_NO", anchor=W)
tree.heading('CVV', text="CVV", anchor=W)
tree.heading('EXPIRY_DATE', text="EXPIRY_DATE", anchor=W) tree.heading('LOAN_AMOUNT', text="LOAN_AMOUNT", anchor=W) tree.heading('INETEREST_RATE', text="INETEREST_RATE", anchor=W) tree.heading('REPAYEMENT_TENURE', text="REPAYEMENT_TENURE", anchor=W) tree.heading('PRINCIPAL_AMOUNT', text="PRINCIPAL_AMOUNT", anchor=W) tree.heading('INTEREST_AMOUNT', text="INTEREST_AMOUNT", anchor=W) tree.heading('EMI', text="EMI", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0) tree.column('#1', stretch=NO, minwidth=0, width=120) tree.column('#2', stretch=NO, minwidth=0, width=120)

tree.column('#3', stretch=NO, minwidth=0, width=50) tree.column('#4', stretch=NO, minwidth=0, width=80) tree.column('#5', stretch=NO, minwidth=0, width=100) tree.column('#6', stretch=NO, minwidth=0, width=100) tree.column('#7', stretch=NO, minwidth=0, width=135) tree.column('#8', stretch=NO, minwidth=0, width=125) tree.column('#9', stretch=NO, minwidth=0, width=120) tree.pack()
def calc(PRINCIPAL_AMOUNT,INTEREST_AMOUNT,EMI ): C0=float(LOAN_AMOUNT.get()) p=float(REPAYEMENT_TENURE.get()) f=float(INETEREST_RATE.get())
PRINCIPAL_AMOUNT.configure(state=NORMAL) PRINCIPAL_AMOUNT.delete(0,'end') PRINCIPAL_AMOUNT.insert(0, str(C0/p)) PRINCIPAL_AMOUNT.configure(state=DISABLED)
INTEREST_AMOUNT.configure(state=NORMAL) INTEREST_AMOUNT.delete(0,'end') INTEREST_AMOUNT.insert(0,str(((C0*f)/100))) INTEREST_AMOUNT.configure(state=DISABLED)
EMI.configure(state=NORMAL) EMI.delete(0,'end') EMI.insert(0,str((C0/p)+((C0*f)/100))) EMI.configure(state=DISABLED)

                                  
