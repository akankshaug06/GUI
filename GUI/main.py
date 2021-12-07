import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
import re
from sqlite3 import *
import smtplib
import database

root = Tk()


# Create a photoimage object of the image in the path
image1 = Image.open("b2.jpeg")
test = ImageTk.PhotoImage(image1)

label0 = tkinter.Label(image=test)
label0.image = test

# Position image
label0.place(x=00, y=00)

root.title("Event Registration Form")
gender = IntVar()
c = StringVar()
agree = IntVar()


def on_press():
    email_id = email.get()
    first_name = fname.get()
    last_name = lname.get()
    gender_value = gender.get()
    age_value = age.get()
    database.insert(email_id, first_name, last_name, gender_value, age_value)
    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("priyaug1998@gmail.com", "priya@0109")
    # message to be sent
    message = f"Hello {fname} {lname}\nThanks for participating in our event.\nPRIYA GUPTA"
    # sending the mail
    s.sendmail("priyaug1998@gmail.com", email_id, message)
    # terminating the session
    s.quit()

def data_display():
    connection = connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('SELECT * FROM userInfo')
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        entry_board.insert(END, row)
        entry_board.insert(END, '\n')


def reset():
    fname.delete(0, 'end')
    lname.delete(0, 'end')
    Mobilenumber.delete(0, 'end')
    email.delete(0, 'end')
    age.delete(0, 'end')
    agree.set(0)
    gender.set(1)
    email.config(text='')


def clear():
    entry_board.delete(1.0, 'end')


label1 = Label(root, text='EVENT REGISTRATION FORM', font=("bold,40"))
label1.place(x=575, y=10)

label2 = Label(root, text="Email id:", fg='black', font=("bold,10"))
label2.pack(pady=5)
label2.place(x=750, y=100)

email = Entry(root, width=30)
email.pack(pady=5)
email.place(x=900, y=102)

label3 = Label(root, text="First name:", fg='black', font=("bold,10"))
label3.pack(pady=5)
label3.place(x=250, y=53)

fname = Entry(root, width=30)
fname.pack(pady=5)
fname.place(x=400, y=55)

label4 = Label(root, text="Last name:", fg='black', font=("bold,10"))
label4.pack(pady=5)
label4.place(x=750, y=53)

lname = Entry(root, width=30, )
lname.pack(pady=5)
lname.place(x=900, y=55)

label5 = Label(root, text="Age:", fg='black', font=("bold,10"))
label5.pack(pady=5)
label5.place(x=250, y=100)

age = Entry(root, width=30)
age.pack(pady=5)
age.place(x=400, y=102)

label6 = Label(root, text="Mobile Number:", fg='black', font=("bold,10"))
label6.pack(pady=5)
label6.place(x=250, y=153)

Mobilenumber = Entry(root, width=30)
Mobilenumber.pack(pady=5)
Mobilenumber.place(x=400, y=155)

label7 = Label(root, text='Gender:', font=("bold,10"))
label7.place(x=250, y=203)

male_gender = Radiobutton(root, text='Male', variable=gender, value=1)
male_gender.place(x=380, y=203)

female_gender = Radiobutton(root, text='Female', variable=gender, value=2)
female_gender.place(x=480, y=203)

other_gender = Radiobutton(root, text='Other', variable=gender, value=3)
other_gender.place(x=580, y=203)

label8 = Label(root, text='Event Category:', font=("bold", 12))
label8.place(x=750, y=153)

list1 = ['Cultural','Sports','Arts','Technical'];

droplist = OptionMenu(root, c, *list1)
droplist.config(width=20)
c.set('select your category')
droplist.place(x=900, y=153)

label9 = Label(root, text=f"{datetime.datetime.now():%a, %b %d %Y  %H:%M:%S %p}", fg="white", bg="black", font=("helvetica", 12))
label9.place(x=90, y=350)

register_button = Button(root, text='Register', width=20, fg='white', bg='blue', command=on_press)
register_button.pack(pady=5)
register_button.place(x=500, y=300)


reset_button = Button(root, text='Reset', width=20, fg='white', bg='red', command= reset)
reset_button.pack(pady=5)
reset_button.place(x=700, y=300)


view_button = Button(root, text='View All', width=20, fg='white', bg='blue', command = data_display)
view_button.pack(pady=5)
view_button.place(x=90, y=450)
entry_board=Text(root, width=1, height=1)
entry_board.place(x=500, y=350, width=700, height=320)


clear_button = Button(root, text='Clear', width=20, fg='white', bg='red', command= clear)
clear_button.pack(pady=5)
clear_button.place(x=90, y=500)


agree_button = Checkbutton(root, text='I agree with terms and conditions', variable=agree, onvalue=1, offvalue=0)
agree_button.pack()
agree_button.place(x=600, y=250)



root.mainloop()