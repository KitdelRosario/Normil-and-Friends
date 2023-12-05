from tkinter import *
import os

user=[]
passwrd = []
email = []
age = []
test1 = []
test2 = []
def reg_user():

    print("Loading...")

    StdNum_info = StdNum.get()
    password_info = password.get()
    Email_info = Email.get()
    Age_info = Age.get()
    Test1_info = Test1.get()
    Test2_info = Test2.get()

    user.append(StdNum_info)
    passwrd.append(password_info)
    email.append(Email_info)
    age.append(Age_info)
    test1.append(Test1_info)
    test2.append(Test2_info)

    print(user)
    print(passwrd)

    lbl = Label(cre, text="Registration Complete", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=370, y=600)

def login_verify():

    user_pass = list(zip(user, passwrd))
    StdNum1 = StdNum_verify.get()
    password1 = password_verify.get()
    try:
        passwd_index = user_pass.index((StdNum1, password1))
        if password1 == passwrd[passwd_index]:
            logsuc()
        else:
            pnr()
    except ValueError:
        unf()

def logsuc():
    global logsuc
    logsuc = Toplevel(main)
    logsuc.title("Success")
    logsuc.geometry("300x100+810+500")
    Label(logsuc, text="Login Sucess").pack()
    Button(logsuc, text="OK", command=deletelogsuc).pack()


def pnr():
    global pnr
    pnr = Toplevel(main)
    pnr.title("Wrong")
    pnr.geometry("300x100+810+500")
    Label(pnr, text="Wrong Student Number or Password").pack()
    Button(pnr, text="OK", command=deletepnr).pack()


def unf():
    global unf
    unf = Toplevel(main)
    unf.title("Wrong")
    unf.geometry("300x100+810+500")
    Label(unf, text="Wrong Student Number or Password").pack()
    Button(unf, text="OK", command=deleteunf).pack()

def log_back():

    log.destroy()
    main.deiconify()

def cre_back():

    cre.destroy()
    main.deiconify()

def upd_back():

    upd.destroy()
    main.deiconify()

def delt_back():

    delt.destroy()
    main.deiconify()

def deletelogsuc():
    logsuc.destroy()


def deletepnr():
    pnr.destroy()


def deleteunf():
    unf.destroy()

def main_scrn(): # Main Screen

    global main
    main = Tk()
    main.geometry("600x500+650+275")
    main.title("Student Portal")
    main.configure(bg="#DED0B6")


    lbl = Label(text="Welcome to Student Portal", fg="#454545", bg="#DED0B6", height=1, width=25, font=("Times", 30, "bold"))
    lbl.place(x = 1, y = 20)

    btn = Button(text="Login Account", fg="#F4BF96", bg="#454545", height=2, width=20, bd=5, font=("Times", 15, "bold"), command = log_scrn) # calling the def_log and will be directed at login screen
    btn.place(x=180, y=100)

    btn = Button(text="Create Account", fg="#F4BF96", bg="#454545", height=2, width=20, bd=5, font=("Times", 15, "bold"), command = cre_scrn) # calling the def_cre and will be directed at create screen
    btn.place(x=180, y=200)

    btn = Button(text="Update Account", fg="#F4BF96", bg="#454545", height=2, width=20, bd=5, font=("Times", 15, "bold"), command = upd_scrn) # calling the def_cre and will be directed at updates screen
    btn.place(x=180, y=300)

    btn = Button(text="Delete Account", fg="#F4BF96", bg="#454545", height=2, width=20, bd=5, font=("Times", 15, "bold"), command = delt_scrn) # calling the def_del and will be directed at delete screen
    btn.place(x=180, y=400)


    main.resizable(False, False)
    main.mainloop()

def log_scrn(): # Login Screen

    global log, StdNum_verify, password_verify, StdNum_entry1, password_entry1
    log = Toplevel(main)
    log.geometry("600x500+650+275")
    log.title("Login Account")
    log.configure(bg="#DED0B6")

    StdNum_verify = StringVar()
    password_verify = StringVar()

    lbl = Label(log, text="Login Account", fg="#454545", bg="#DED0B6", height=1, width=12, font=("Times", 40, "bold"))
    lbl.place(x=116, y=20)

    lbl = Label(log, text="Enter Student Number:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=220, y=140)

    StdNum_entry1 = Entry(log, textvariable=StdNum_verify, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 15))
    StdNum_entry1.place(x=195, y=190)

    lbl = Label(log, text="Enter password:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=240, y=270)

    password_entry1 = Entry(log, textvariable=password_verify, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Times", 16), show="*")
    password_entry1.place(x=197, y=320)

    btn = Button(log, text="       Log In       ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"),command = login_verify) # calling the def_Check
    btn.place(x=130, y=400)

    btn = Button(log, text="         Back          ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"), comman = log_back) # calling  log_back and returning on main screen
    btn.place(x=330, y=400)


    log.resizable(False, False)
    main.withdraw()

def cre_scrn(): # Create Screen

    global cre, StdNum, password, Email, Age, Test1, Test2, StdNum_entry, password_entry, Email_entry, Age_entry, Test1_entry, Test2_entry
    cre = Toplevel(main)
    cre.geometry("900x700+490+200")
    cre.title("Create Account")
    cre.configure(bg="#DED0B6")

    StdNum = StringVar()
    password = StringVar()
    Email = StringVar()
    Age = StringVar()
    Test1 = StringVar()
    Test2 = StringVar()

    lbl = Label(cre, text="Create an Account", fg="#454545", bg="#DED0B6", height=1, width=15, font=("Times", 50, "bold"))
    lbl.place(x=160, y=20)

    lbl = Label(cre, text="Student Number:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=80, y=160)

    StdNum_entry = Entry(cre, textvariable=StdNum, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20))
    StdNum_entry.place(x=80, y=200)

    lbl = Label(cre, text="Create Password:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=80, y=280)

    password_entry = Entry(cre, textvariable=password, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20), show="*")
    password_entry.place(x=80, y=320)

    lbl = Label(cre, text="Test:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=80, y=400)

    Test1_entry = Entry(cre, textvariable=Test1, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20))
    Test1_entry.place(x=80, y=440)

    lbl = Label(cre, text="E-Mail:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=500, y=160)

    Email_entry = Entry(cre, textvariable=Email, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20))
    Email_entry.place(x=500, y=200)

    lbl = Label(cre, text="Age:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=500, y=280)

    Age_entry = Entry(cre, textvariable=Age, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20))
    Age_entry.place(x=500, y=320)

    lbl = Label(cre, text="Test:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=500, y=400)

    Test2_entry = Entry(cre, textvariable=Test2, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 20))
    Test2_entry.place(x=500, y=440)

    btn = Button(cre, text="            Create            ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"), command = reg_user)
    btn.place(x=260, y=540)

    btn = Button(cre, text="            Back            ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"), command = cre_back) # calling  cre_back and returning on main screen
    btn.place(x=470, y=540)

    cre.resizable(False, False)
    main.withdraw()

def upd_scrn():  # Update Screen

    global upd
    upd = Toplevel(main)
    upd.geometry("600x500+650+275")
    upd.title("Login Account")
    upd.configure(bg="#DED0B6")

    lbl = Label(upd, text="Update Account", fg="#454545", bg="#DED0B6", height=1, width=12, font=("Times", 40, "bold"))
    lbl.place(x=116, y=20)

    lbl = Label(upd, text="Enter Student Number:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=220, y=140)

    txtfld = Entry(upd, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 15))
    txtfld.place(x=195, y=190)

    lbl = Label(upd, text="Enter password:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=240, y=270)

    txtfld_password = Entry(upd, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Times", 16), show="*")
    txtfld_password.place(x=197, y=320)

    btn = Button(upd, text="         Edit         ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"))  # calling the def_Check
    btn.place(x=130, y=400)

    btn = Button(upd, text="         Back          ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"), command = upd_back)  # calling  upd_back and returning on main screen
    btn.place(x=330, y=400)

    upd.resizable(False, False)
    main.withdraw()

def delt_scrn(): # Delete Screen

    global delt
    delt = Toplevel(main)
    delt.geometry("600x500+650+275")
    delt.title("Login Account")
    delt.configure(bg="#DED0B6")

    lbl = Label(delt, text="Update Account", fg="#454545", bg="#DED0B6", height=1, width=12, font=("Times", 40, "bold"))
    lbl.place(x=116, y=20)

    lbl = Label(delt, text="Enter Student Number:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=220, y=140)

    txtfld = Entry(delt, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Helvetica", 15))
    txtfld.place(x=195, y=190)

    lbl = Label(delt, text="Enter password:", fg="#454545", bg="#DED0B6", font=("Times", 13, "bold"))
    lbl.place(x=240, y=270)

    txtfld_password = Entry(delt, fg="#454545", bg="#F0E9D2", bd=3.5, font=("Times", 16), show="*")
    txtfld_password.place(x=197, y=320)

    btn = Button(delt, text="         Delete         ", fg="#F4BF96", bg="#454545", bd=3.5,
                 font=("Times", 13, "bold"))  # calling the def_Check
    btn.place(x=130, y=400)

    btn = Button(delt, text="         Back          ", fg="#F4BF96", bg="#454545", bd=3.5, font=("Times", 13, "bold"), command = delt_back)  # calling  delt_back and returning on main screen
    btn.place(x=330, y=400)

    delt.resizable(False, False)
    main.withdraw()

main_scrn()