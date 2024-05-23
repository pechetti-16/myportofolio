from tkinter import *
from tkinter import messagebox
from datetime import datetime
#import pyttsx3
from mysql.connector import connect
from string import *


username='0'
root = Tk()
root.title('SAHA')
root.resizable(False,False)
root.geometry("1536x864+0+0")
w=1536
h=864
attributes=('Segoe UI Emoji',30,'bold')
conn = connect(
    host = 'localhost',
    user = 'root', 
    password = 'Sanjana@2005',
    database = 'hack1'
)
cursor = conn.cursor()


def home():
    ff=Frame(root,width=w,height=h,bg="#f47c3c")
    ff.place(x=0,y=0)
    f=Frame(root,width=750,height=h,bg="#f47c3c")
    f.place(x=800,y=0)
    f1=Frame(root,width=750,height=810,bg="white")
    f1.place(x=10,y=10)
    '''f2=Frame(root,width=400,height=250,bg="steel blue")
    f2.place(x=170,y=500)'''
    h1=Label(f1,text="SAHA",fg='#f47c3c',bg='white',font=('Arial Black',45,'italic'))
    h1.place(x=250,y=100)
    h1=Label(f1,text="Give what you can!!",fg='#f47c3c',bg='white',font=('Cooper Black',25))
    h1.place(x=200,y=200)

    '''img1=PhotoImage(file='login.jpg')
    im=Label(ff,image=img1)
    im.pack()'''

    b1=Button(f,text='Sign up',bg="black",fg="white",font=("Arial",30,'bold'),width=20,command=signup)
    b1.place(x=150,y=200)

    b2=Button(f,text='Login',bg="black",fg="white",font=("Arial",30,'bold'),width=20,command=login)
    b2.place(x=150,y=400)
    def exit():
       f.destroy()
       ff.destroy()
       f1.destroy()
       root.destroy()
    logout_button=Button(f,text='Exit',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=exit)
    logout_button.place(x=350,y=600)
    


def login():
    f=Frame(root,width=w,height=h,bg="white")
    f.place(x=0,y=0)
    fr=Frame(root,width=850,height=650,bg="#f47c3c")
    fr.place(x=350,y=100)
    heading=Label(fr,text='Login',fg='black',bg='#f47c3c',font=('Times new roman',44,'bold'))
    heading.place(x=350,y=5)

    name1=Label(fr,text="Name",font=("Arial",30),bg="#f47c3c")
    name1.place(x=100,y=150)
    user1 = Entry(fr,width=15,fg='black',border=1,bg="white",font=("Arail",30))
    user1.place(x=300,y=150)

    password1=Label(fr,text="password",font=("Arial",30),bg="#f47c3c")
    password1.place(x=100,y=250)
    password22 = Entry(fr,show="*",width=15,fg='black',border=2,bg="white",font=("Arail",30))
    password22.place(x=300,y=250)
    def validate_login():
        username = user1.get()
        password0 = password22.get()
        # Replace these with your actual username and password
        cursor.execute('select * from users;')
        data = cursor.fetchall()
        names = [item[0] for item in data]
        passw = [pas[1] for pas in data]
        if username in names and password0 in passw and names.index(username)==passw.index(password0):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            users_page()
        else:
            messagebox.showerror("ERROR","Invalid username and password")
        return username

    login_b=Button(fr,text='Login',bg="brown",fg="white",font=("Arial",30,'bold'),width=12,command=validate_login)
    login_b.place(x=300,y=400)
    def back():
       fr.destroy()
       home()
    back_button=Button(fr,text='Back',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=back)
    back_button.place(x=380,y=500)



def signup():
    frame11=Frame(root,width=w,height=h,bg="white")
    frame11.place(x=0,y=0)
    frame=Frame(root,width=850,height=650,bg="#f47c3c")
    frame.place(x=350,y=100)
    heading=Label(frame,text='Sign up',fg='red',bg='white',font=('Times new roman',44,'bold'))
    heading.place(x=350,y=5)

    name=Label(frame,text="Name",font=("Arial",30),bg="white")
    name.place(x=100,y=100)
    user = Entry(frame,width=15,fg='black',border=1,bg="white",font=("Arail",30))
    user.place(x=300,y=100)

    email=Label(frame,text="Email",font=("Arial",30),bg="white")
    email.place(x=100,y=200)
    email1 = Entry(frame,width=15,fg='black',border=1,bg="white",font=("Arail",30))
    email1.place(x=300,y=200)

    password1=Label(frame,text="password",font=("Arial",30),bg="white")
    password1.place(x=100,y=300)
    password = Entry(frame,show="*",width=15,fg='black',border=2,bg="white",font=("Arail",30))
    password.place(x=300,y=300)
    def validate_signup():
        username = user.get()
        password0 = password.get()
        email2=email1.get()
        cursor.execute('select * from users;')
        data = cursor.fetchall()
        names = [item[0] for item in data]
        passw = [pas[1] for pas in data]
        # Replace these with your actual username and password
        insert_query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        user_data = (username, password0, email2)
        cursor.execute(insert_query, user_data)
        conn.commit()
        if username in names and password0 in passw:
            messagebox.showerror("ERROR","You have already signed up, please login!!")
        else:
          messagebox.showinfo("Signup Successful", "Welcome, " + username + "!")
          users_page()
    def back():
       frame.destroy()
       frame11.destroy()
       home()
    back_button=Button(frame,text='Back',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=back)
    back_button.place(x=350,y=550)
    signup=Button(frame,text='Sign up',bg="brown",fg="white",font=("Arial",30,'bold'),command=validate_signup)
    signup.place(x=320,y=400)



def users_page():
    fram=Frame(root,width=w,height=h,bg='white')
    fram.place(x=0,y=0)
    frame2=Frame(fram,width=w,height=105,bg='#f47c3c')
    frame2.place(x=0,y=0)

    h1=Label(fram,text="SAHA",fg='white',font=('Arial Black',45),background='#f47c3c')
    h1.place(x=625,y=10)

    donate_button=Button(fram,text='DONATE',bg='#f47c3c',fg='white',font=('Cooper Black',40,'bold'),command=for_whom)
    donate_button.place(x=560,y=200)
    recieve_button=Button(fram,text='RECIEVE',bg='#f47c3c',fg='white',font=('Cooper Black',40,'bold'))
    recieve_button.place(x=560,y=440)
    def logout():
       fram.destroy()
       home()
    logout_button=Button(fram,text='Logout',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=logout)
    logout_button.place(x=1300,y=40)



def for_whom():
    fra=Frame(root,width=w,height=h,bg='white')
    fra.place(x=0,y=0)
    frame2=Frame(fra,width=w,height=105,bg='#f47c3c')
    frame2.place(x=0,y=0)

    h1=Label(fra,text="SAHA",fg='white',font=('Arial Black',45),background='#f47c3c')
    h1.place(x=625,y=10)

    homeless=Button(fra,text='Food for Homeless',bg='#f47c3c',fg='white',font=('Cooper Black',35,'bold'),command=details_page_donor)
    homeless.place(x=560,y=200)
    animals=Button(fra,text='Food for Animals',bg='#f47c3c',fg='white',font=('Cooper Black',35,'bold'),command=for_animals)
    animals.place(x=560,y=440)
    def back():
       fra.destroy()
       users_page()
    logout_button=Button(fra,text='Back',bg='#f47c3c',fg='white',font=('Cooper Black',20,'bold'),command=back)
    logout_button.place(x=740,y=680)



def for_animals():
    f1=Frame(root,width=w,height=h,bg='white')
    f1.place(x=0,y=0)
    det=Label(f1,text="DONATE FOOD",fg='black',bg='white',font=attributes)
    det.place(x=670,y=20)
    det1=Label(f1,text="Fill the details:",fg='black',bg='white',font=attributes)
    det1.place(x=0,y=70)
    det2=Label(f1,text="Name:",fg='black',bg='white',font=attributes)
    det2.place(x=0,y=130)
    ent1=Entry(f1,text="Name:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent1.place(x=250,y=140)
    det3=Label(f1,text="Mobile No:",fg='black',bg='white',font=attributes)
    det3.place(x=0,y=190)
    ent2=Entry(f1,text="NAME:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent2.place(x=250,y=200)
    det4=Label(f1,text="Location:",fg='black',bg='white',font=attributes)
    det4.place(x=0,y=240)
    op=StringVar()
    op.set('Bhimavram')
    #options.config(width=20,font=('Arial',18,'bold'))
    drop=OptionMenu(f1,op,'Bhimavaram','Visakoduru','Guntur','Hyderabad','Vizag','Ongole','Kakinada','Kanigiri','Amalapuram')
    drop.config(width=20,font=('Arial',18,'bold'))  # Set the width of the dropdown button
    drop.pack(pady=20)
    drop.place(x=250,y=260)
    det5=Label(f1,text="Food Type",fg='black',bg='white',font=attributes)
    det5.place(x=0,y=350)
    a1=IntVar()
    a2=IntVar()
    a=[a1,a2]
    type=['veg','non-veg']
    i=0
    j=0
    k=0
    for check in type:
       check1=Checkbutton(f1,text=check,bg='white',variable=a[i],font=('Algerian',20),width=20)
       check1.place(x=0+k,y=450)
       j=j+45
       i=i+1
       k=k+300
    det6=Label(f1,text="Quantity(for persons)",fg='black',bg='white',font=attributes)
    det6.place(x=0,y=500)
    ent3=Entry(f1,text="NAME:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent3.place(x=10,y=570)
    options0=StringVar()
    options0.set('01')
    drop0=OptionMenu(f1,options0,'01','02','03','04','05','06','07','08','09','10','11','12')
    drop0.place(x=150,y=670)
    op1=StringVar()
    op1.set('00')
    drop1=OptionMenu(f1,op1,'00','05','10','15','20','25','30','35','40','45','50','55')
    drop1.place(x=200,y=670)
    op2=StringVar()
    op2.set('am')
    drop3=OptionMenu(f1,op2,'am','pm')
    drop3.place(x=250,y=670)
    det7=Label(f1,text="Time",fg='black',bg='white',font=attributes)
    det7.place(x=0,y=650)
    donate=Button(f1,text='Donate',fg='black',bg='white',font=('Arial Black',20))
    donate.place(x=150,y=730)
    def back():
       f1.destroy()
       for_whom()
    back_button=Button(f1,text='Back',bg='white',fg='black',font=('Cooper Black',20,'bold'),command=back)
    back_button.place(x=100,y=20)



def details_page_donor():
    frame1=Frame(root,width=w,height=h,bg='white')
    frame1.place(x=0,y=0)
    det=Label(frame1,text="DONATE FOOD",fg='black',bg='white',font=attributes)
    det.place(x=670,y=20)
    det1=Label(frame1,text="Fill the details:",fg='black',bg='white',font=attributes)
    det1.place(x=0,y=70)
    det2=Label(frame1,text="Name:",fg='black',bg='white',font=attributes)
    det2.place(x=0,y=130)
    ent1=Entry(frame1,text="Name:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent1.place(x=250,y=140)
    det3=Label(frame1,text="Mobile No:",fg='black',bg='white',font=attributes)
    det3.place(x=0,y=190)
    ent2=Entry(frame1,text="NAME:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent2.place(x=250,y=200)
    det4=Label(frame1,text="Location:",fg='black',bg='white',font=attributes)
    det4.place(x=0,y=240)
    options=StringVar()
    options.set('Bhimavram')
    drop=OptionMenu(frame1,options,'Bhimavaram','Visakoduru','Guntur','Hyderabad','Vizag','Ongole','Kakinada','Kanigiri','Amalapuram')
    drop.config(width=20,font=('Arial',18,'bold'))  # Set the width of the dropdown button
    drop.pack(pady=20)
    drop.place(x=250,y=260)
    det5=Label(frame1,text="Food Type",fg='black',bg='white',font=attributes)
    det5.place(x=0,y=350)
    a1=IntVar()
    a2=IntVar()
    a=[a1,a2]
    type=['veg','non-veg']
    i=0
    j=0
    k=0
    for check in type:
       check1=Checkbutton(frame1,text=check,bg='white',variable=a[i],font=('Algerian',20),width=20)
       check1.place(x=0+k,y=450)
       j=j+45
       i=i+1
       k=k+300
    det6=Label(frame1,text="Quantity(for persons)",fg='black',bg='white',font=attributes)
    det6.place(x=0,y=500)
    ent3=Entry(frame1,text="NAME:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent3.place(x=10,y=570)
    options0=StringVar()
    options0.set('01')
    drop0=OptionMenu(frame1,options0,'01','02','03','04','05','06','07','08','09','10','11','12')
    drop0.place(x=150,y=670)
    options1=StringVar()
    options1.set('00')
    drop1=OptionMenu(frame1,options1,'00','05','10','15','20','25','30','35','40','45','50','55')
    drop1.place(x=200,y=670)
    options2=StringVar()
    options2.set('am')
    drop3=OptionMenu(frame1,options2,'am','pm')
    drop3.place(x=250,y=670)
    det7=Label(frame1,text="Time",fg='black',bg='white',font=attributes)
    det7.place(x=0,y=650)
    donate=Button(frame1,text='Donate',fg='black',bg='white',font=('Arial Black',20))
    donate.place(x=150,y=730)
    def back():
       frame1.destroy()
       for_whom()
    logout_button=Button(frame1,text='Back',bg='white',fg='black',font=('Cooper Black',20,'bold'),command=back)
    logout_button.place(x=100,y=20)



home()
root.mainloop()


