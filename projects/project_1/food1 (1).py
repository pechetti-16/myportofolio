from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pyttsx3
from mysql.connector import connect
from string import *
import random


conn = connect(
    host = 'localhost',
    user = 'root', #sql username
    password = 'nyfa@27octP',#password
    database = 'nyf'#name of db
)
cursor = conn.cursor()
l=[]
voice = pyttsx3.init()
global total
username='0'
root = Tk()
root.title('ON TIME FOOD')
root.resizable(False,False)
root.geometry("1000x500+250+150")
attributes=('Segoe UI Emoji',30,'bold')
def loginpage():
 def homepage(use1,passw):
   def menu(u,p):
      #menu page
      cursor.execute("SELECT item_name, price,quantity FROM menu")
      root1 = Tk()
      root1.title('ON TIME FOOD')
      root1.resizable(False, False)
      root1.geometry("1000x780+250+0")
      frame3 = Frame(root1, width=1000, height=780, bg='white')
      frame3.place(x=0,y=0)
      menu_items = cursor.fetchall()
      names = [item[0] for item in menu_items]
      pric = [pas[1] for pas in menu_items]
      #quant=[q[2] for q in menu_items]
    
      def payment(u,p):
            root1.destroy()
            f.destroy()
            frame1.destroy()
  
            fe = Frame(root, bg='white', width=1000, height=500)
            fe.place(x=0, y=0)

            head = Label(fe, text='Get  ready  to  feast!',bg='crimson', fg='white', font=('impact', 25), width=70)
            head.place(x=0, y=0)

            text = "Scan here"
            label = Label(fe, text=text,font=('Arial', 20),fg='crimson',bg='white')
            label.place(x=720,y=110)

            image_file = "scanner.png"  
            img = PhotoImage(file=image_file)
            label = Label(fe, image=img)
            label.place(x=690,y=150)

            order_id = Label(fe, text='Order ID:1024', bg='white', fg='#333333', font=('Arial', 20))
            order_id.place(x=50, y=110)

            '''order_id_value = random.randint(1000, 9999)
            k=order_id_value
            order_id_num = Label(fe, text=f"{k}", bg='white', fg='#333333', font=('Arial', 20))
            order_id_num.place(x=180, y=110)'''

            name = Label(fe, text=f'Recipient:{u}', fg='#333333', bg='white', font=('Arial', 20))
            name.place(x=50, y=150)

            items = Label(fe, text='Items List:Noodles,Manchria,Veg-Meals', bg='white', fg='#333333', font=('Arial', 20))
            items.place(x=50, y=190)

            time1 = Label(fe, text='Time:', fg='#333333', bg='white', font=('Arial', 20))
            time1.place(x=50, y=230)

            amount1 = Label(fe, text='Total Amount:Rs.370', fg='crimson', bg='#F0F0F0', font=('Arial', 20))
            amount1.place(x=50, y=270)

            t = Label(fe, text='Enjoy!!', fg='crimson', bg='white', font=('Arial', 30,'bold'))
            t.place(x=350, y=300)
          

            def get_selected_value():
              selected_value = f"{drop.get()}:{drop1.get()}:{drop2.get()}"
              time1.config(text=f'Time: {selected_value}')

            get_selected_value()

            
            def back():
              fe.destroy()
              img.blank()
              homepage(u,p)

            back_button = Button(fe, text='BACK', bg='#333333', fg='white', font=('Arial', 15, 'bold'), command=back)
            back_button.place(x=430, y=430)


      head2 = Label(frame3, text='List of Food Items', fg='black', font=('Arial Black', 30), width=38, bg='crimson')
      head2.place(x=0, y=0)

      food_items = Label(frame3, text='FOOD ITEMS', fg='black', bg='#DDAA00', font=('Algerian', 30), width=16)
      food_items.place(x=0, y=65)

      prices = Label(frame3, text='PRICES', fg='black', bg='#DDAA00', font=('Algerian', 30), width=15)
      prices.place(x=375, y=65)

      quantity = Label(frame3, text='QUANTITY', fg='black', bg='#DDAA00', font=('Algerian', 30), width=15)
      quantity.place(x=675, y=65)

      names = [item[0] for item in menu_items]
      pric = [pas[1] for pas in menu_items]
      qty=[]
      
      def calculate_total(event=None):
              total=0
              for i, entry in enumerate(qty):
                  ind=qty.index(entry)
                  l.append(qty[ind])
                  try:
                      value = float(entry.get())
                      total += value * pric[i]
                  except ValueError:
                      pass
              k="Total: {:.2f}".format(total)
              amount.config(text=k)
              return k
      
      def create_entry_box(y):
              entry = Entry(frame3,width=10,font=('Algerian', 20))
              entry.place(x=800, y=115 + (i * 45))
              qty.append(entry)
              entry.bind('<KeyRelease>', calculate_total)
      
      
      j=0
      for i in range(len(names)):
            item_label = Label(frame3, text=names[i], bg='white', font=('Algerian', 20), width=20)
            item_label.place(x=0, y=115 + (i * 45))

            price_label = Label(frame3, text=pric[i], bg='white', font=('Algerian', 20), width=20)
            price_label.place(x=375, y=115 + (i * 45))

            create_entry_box(y=i*30 +50)

            
            

      time = Label(frame3, text='select time--->', bg='white', font=('Algerian', 20), width=20)
      time.place(x=200, y=500)

      day = Label(frame3, text='Date', bg='white', font=('Algerian', 20), width=18)
      day.place(x=200, y=550)
      print(qty)

      current_date = datetime.now()
      indian_date_format = current_date.strftime("%d/%m/%Y")
      day1 = Label(frame3, text=indian_date_format, bg='white', font=('Algerian', 20), width=14)
      day1.place(x=480, y=550)

      
      amount = Label(frame3, text=f'0.00', fg='crimson', bg='white', font=('Arial', 20))
      amount.place(x=800, y=505)
      options=['01','02','03','04','05','06','07','08','09','10','11','12']
      drop=StringVar(frame3)
      drop.set(options[0])
      men=OptionMenu(frame3, drop, *options)
      men.place(x=550,y=505)
      options1=['00','05','10','15','20','25','30','35','40','45','50','55']
      drop1=StringVar(frame3)
      drop1.set(options1[0])
      men1=OptionMenu(frame3, drop1, *options1)
      men1.place(x=600,y=505)
      options2=['am','pm']
      drop2=StringVar(frame3)
      drop2.set(options2[0])
      men2=OptionMenu(frame3, drop2, *options2)
      men2.place(x=650,y=505)
      
      
      canvas1 =Canvas(frame3, width=150, height=80, bg='white', highlightthickness=0)
      canvas1.place(x=530,y=600)
   
      submit_button =Button(frame3, text="PLACE ORDER", command=lambda:payment(p,u), bg='#DDAA00', fg='white', bd=5, highlightthickness=10,font=('bold'))
      canvas1.create_window(50, 50, window=submit_button)
        
      def back():
         frame3.destroy()
         
         #img10.blank()
         root1.destroy()
         homepage(u,p)
      canvas =Canvas(frame3, width=100, height=100, bg='white', highlightthickness=0)
      canvas.place(x=530,y=690)

      back_button =Button(frame3, text="back", command=back, bg='crimson', fg='white', bd=5, highlightthickness=0,font=('bold'))
      canvas.create_window(50, 50, window=back_button)
    
      root1.mainloop()
      #end of menu page




   #update password   
   def changepassword(use2,pass2):
      frame1.destroy()
      img1.blank()
      frame4=Frame(root,width=1000,height=500,bg='white')
      frame4.place(x=0,y=0)
      img4=PhotoImage(file="pass.png")
      im=Label(frame4,image=img4)
      im.pack()
      h1=Label(frame4,text="CHANGE PASSWORD",fg='white',bg='navy blue',font=('Arial Black',30))
      h1.place(x=250,y=5)
      p1=Label(frame4,text="Old Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p1.place(x=150,y=100)
      p1_entry = Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p1_entry.place(x=450,y=100)
      p2=Label(frame4,text="New Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p2.place(x=150,y=180)
      p2_entry = Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p2_entry.place(x=450,y=180)
      p3=Label(frame4,text="Confirm Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p3.place(x=150,y=260)
      p3_entry = Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p3_entry.place(x=450,y=260)
      def sub():
        pp=pass2
        u=use2
        if pp==p1_entry.get():
         if p2_entry.get()==p3_entry.get():
             update_query="UPDATE E SET password=%s WHERE username=%s"
             data=(p2_entry.get(),u)
             cursor.execute(update_query,data)
             conn.commit()
             p=p2_entry.get()
             frame4.destroy()
             img4.blank()
             messagebox.showinfo("Password updated","Password successfully changed!!")
             
             homepage(u,p)
         else:
           messagebox.showerror("error","Two passwords should be equal!!")
        else:
          messagebox.showerror("error","your old password is wrong!!")
      def show_hide_password():
        if show_password.get():
         p1_entry.config(show="")
         p2_entry.config(show="")
         p3_entry.config(show="")
        else:
         p1_entry.config(show="*")
         p2_entry.config(show="*")
         p3_entry.config(show="*")
      show_password = BooleanVar()
      show_password_checkbox = Checkbutton(frame4, text="Show Passwords", variable=show_password,bg='LightSkyBlue', command=show_hide_password,font=('Bodoni MT Black',12))
      show_password_checkbox.place(x=430,y=350)
      submit=Button(frame4,text='UPDATE',bg='red',fg='white',font=('Cooper Black',20,'bold'),command=sub)
      submit.place(x=430,y=400)
      def back():
       frame4.destroy()
       img4.blank()
       homepage(use2,pass2)
      back_button=Button(frame4,text='<--BACK',bg='white',fg='black',font=('Cooper Black',15,'bold'),command=back)
      back_button.place(x=25,y=10)



   #home page
   frame.destroy()
   img.blank()
   # Create the home window
   pass1=passw
   use=use1
   
  #reschedulepage
   def create_widgets(parent, order):
        container = ttk.Frame(parent)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)

        ttk.Label(container, text="Re-Schedule", style='Heading.TLabel').grid(row=0, columnspan=2, pady=10)

        ttk.Label(container, text="Order ID:1024", style='My.TLabel').grid(row=1, column=0, sticky="w")
        ttk.Label(container, text=order['order_id'], style='My.TLabel').grid(row=1, column=1, sticky="w")

        ttk.Label(container, text="Contact No:", style='My.TLabel').grid(row=2, column=0, sticky="w")
        ttk.Label(container, text=order['contact_no'], style='My.TLabel').grid(row=2, column=1, sticky="w")

        ttk.Label(container, text="Date of Receiving:", style='My.TLabel').grid(row=3, column=0, sticky="w")
        ttk.Label(container, text=order['date'], style='My.TLabel').grid(row=3, column=1, sticky="w")

        ttk.Label(container, text="Time:", style='My.TLabel').grid(row=4, column=0, sticky="w")
        ttk.Label(container, text=order['time'], style='My.TLabel').grid(row=4, column=1, sticky="w")

        ttk.Separator(container, orient='horizontal').grid(row=5, columnspan=2, sticky="ew", pady=10)

        ttk.Label(container, text="Ordered Items:", style='My.TLabel').grid(row=6, columnspan=2, sticky="w")
        for i, item in enumerate(order['items'], start=7):
            ttk.Label(container, text=item, style='My.TLabel').grid(row=i, columnspan=2, sticky="w")

        ttk.Button(container, text="Reschedule", command=lambda: reschedule_order(parent, order), style='Small.TButton').grid(row=i+1, columnspan=2, pady=10)

   def reschedule_order(parent, order):
        global reschedule_window
        reschedule_window = Toplevel(parent)
        reschedule_window.title("Reschedule")
        reschedule_window.geometry("900x500")  # Set window size

        container = ttk.Frame(reschedule_window)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)

        ttk.Label(container, text="Reschedule", style='Small.Heading.TLabel').grid(row=0, columnspan=2, pady=(10, 20))

        ttk.Label(container, text="Order ID:1024", font=('Helvetica', 12)).grid(row=1, column=0, sticky="w")
        ttk.Label(container, text=order['order_id'], font=('Helvetica', 12)).grid(row=1, column=1, sticky="w")

        ttk.Label(container, text="Penalty for Reschedule: $10", font=('Helvetica', 12)).grid(row=2, columnspan=2, sticky="w")

        ttk.Label(container, text="Select Reschedule Time:", font=('Helvetica', 12)).grid(row=3, columnspan=2, sticky="w")
        new_time_entry = ttk.Entry(container)
        new_time_entry.grid(row=4, columnspan=2, pady=(5, 20))

        ttk.Button(container, text="Update", command=lambda: update_time(order, new_time_entry), style='Small.TButton').grid(row=5, columnspan=2, pady=10)

   def update_time(order, new_time_entry):
        new_time = new_time_entry.get()
        if not (new_time.isdigit() and 1 <= int(new_time) <= 24):
            show_alert("Invalid Time", "Please enter a valid time.")
            return
        order['time'] = new_time
        reschedule_window.destroy()

   def show_alert(title, message):
        alert_window = Toplevel()
        alert_window.title(title)
        alert_window.geometry("400x150")  # Increased window size
        ttk.Label(alert_window, text=message).pack(pady=10)
        ok_button = ttk.Button(alert_window, text="OK", command=alert_window.destroy)
        ok_button.pack(pady=5)

   def initialize_ui(u,p):
        root3 = Tk()
        root3.title("My Orders")
        root3.geometry("900x500+250+150")  # Set window size
        style = ttk.Style(root3)
        style.configure('My.TLabel', font=('Helvetica', 14), padding=10)
        style.configure('Small.TButton', font=('Helvetica', 10), padding=5, background='#FFA500')  # Adjusted button style
        style.configure('Heading.TLabel', font=('Helvetica', 16, 'bold'), padding=10, foreground='white', background='#4CAF50')  # Adjusted heading style

        orders = [
            {"order_id": 1, "contact_no": "1234567890", "date": "2024-03-15", "time": "10:00", "items": ["Item 1", "Item 2"]},
            {"order_id": 2, "contact_no": "9876543210", "date": "2024-03-16", "time": "12:00", "items": ["Item 3", "Item 4"]},
            {"order_id": 3, "contact_no": "4567890123", "date": "2024-03-17", "time": "14:00", "items": ["Item 5", "Item 6"]},
            {"order_id": 4, "contact_no": "8901234567", "date": "2024-03-18", "time": "16:00", "items": ["Item 7", "Item 8"]}
            # Add more orders here as needed
        ]
        def back():
           root3.destroy()
           homepage(u,p)
        back_button=Button(root3,text='BACK',bg='red',fg='white',font=('Arial Black',10,'bold'),command=back)
        back_button.place(x=800,y=430)
        ttk.Label(root3, text="My Orders", style='My.TLabel').grid(row=0, columnspan=2, pady=20)
        for i, order in enumerate(orders, start=1):
            ttk.Button(root3, text=f"Order {order['order_id']}", command=lambda order=order: create_widgets(root3, order), style='My.TButton').grid(row=i, column=0, padx=20, pady=10, sticky="w")

     
   #recieptpage
   def reciept(u,p):
      frame = Frame(root, width=1000, height=500, bg='#F0F0F0')
      frame.pack(fill=BOTH, expand=True)

      heading_frame = Frame(frame, bg='crimson', width=1000, height=60)
      heading_frame.place(x=0, y=20)


      head = Label(frame, text='Get  ready  to  feast!',bg='crimson', fg='white', font=('impact', 25), padx=1, pady=1)
      head.place(x=350, y=20)

      order_id = Label(frame, text='Order ID:1024', bg='#F0F0F0', fg='#333333', font=('Arial', 20))
      order_id.place(x=50, y=110)


      '''order_id_value = random.randint(1000, 9999)
      order_id_num = Label(frame, text=f"{order_id_value}", bg='#F0F0F0', fg='#333333', font=('Arial', 20))
      order_id_num.place(x=180, y=110)'''


      name = Label(frame, text=f'Recipient:{u}', fg='#333333', bg='#F0F0F0', font=('Arial', 20))
      name.place(x=50, y=150)


      items = Label(frame, text='Items List:Noodles,Manchuria,Veg-Meals', bg='#F0F0F0', fg='#333333', font=('Arial', 20))
      items.place(x=50, y=190)


      time = Label(frame, text='Time:06:00 PM', fg='#333333', bg='#F0F0F0', font=('Arial', 20))
      time.place(x=50, y=230)
      
          

      divider = Canvas(frame, width=200, height=2, bg='#333333', highlightthickness=0)
      divider.place(x=40, y=320)
      divider.create_line(0, 0.5, 600, 0.5)

      amount1 = Label(frame, text='Total Amount:Rs.370', fg='crimson', bg='#F0F0F0', font=('Arial', 20))
      amount1.place(x=50, y=270)


      done = Label(frame, text='ORDER PLACED', fg='crimson', bg='#F0F0F0', font=('Arial Black', 20))
      done.place(x=350, y=320)

      def back():
         frame.destroy()
         homepage(u,p)

      back_button = Button(frame, text='BACK', bg='#333333', fg='white', font=('Arial', 15, 'bold'), bd=0, relief=FLAT, padx=10, pady=5, command=back)
      back_button.place(x=430, y=430)

   def changepassword1():
     changepassword(use,pass1)

   f=Frame(root, width=1000, height=500, bg='white')
   f.place(x=0, y=0)

   frame1 = Frame(root, width=1000, height=425, bg='white')
   frame1.place(x=0, y=75)
   frame2 = Frame(root, width=1000, height=75, bg='crimson')
   frame2.place(x=0, y=0)

   img1 = PhotoImage(file='san2.png')
   img_lbl1 = Label(frame1, image=img1)
   img_lbl1.place(x=0,y=0)

   caption=Label(frame1,text="Swift & Savory",fg='crimson',bg='white',font=('Arial Black',25,'bold'))
   caption.place(x=600,y=50)
   caption1=Label(frame1,text="Where Time Meets Taste!",fg='crimson',bg='white',font=('Arial Black',25,'bold'))
   caption1.place(x=500,y=100)

   head1 = Label(frame2, text='ON TIME FOOD',bg='crimson', fg='white', font=('Algerian', 50, 'bold'))
   head1.place(x=15, y=1)
        
   user_lbl = Label(frame2, text=f"USERNAME:", bg='crimson', fg='white', font=('Cooper Black', 13, 'bold'))
   user_lbl.place(x=550, y=10)
   use11 = Label(frame2, text=use.upper(), font=("Cooper Black", 13), fg='yellow', bg='crimson')
   use11.place(x=670, y=10)

   password_update = Button(frame2, text="Change password", font=('arial', 13, 'bold'), bg='white', fg='black',command=changepassword1)
   password_update.place(x=550, y=40) 


   menu_button = Button(frame1, text='MENU', bg='crimson', fg='white', command=lambda:menu(pass1,use), font=('Arial Black', 15, 'bold'))
   menu_button.place(x=670, y=175)

   reschedule_button = Button(frame1, text='MY ORDERS', bg='crimson', fg='white', font=('Arial Black', 15, 'bold'),command=lambda:initialize_ui(use,pass1))
   reschedule_button.place(x=630, y=275)

   reciept_button = Button(frame1, text='RECIEPT', bg='crimson', fg='white', font=('Arial Black', 15, 'bold'),command=lambda:reciept(use,pass1))
   reciept_button.place(x=650, y=375)

   back_button = Button(frame2, text='LOGOUT', bg='crimson', fg='white', font=('Arial Black', 10, 'bold'), command=loginpage)
   back_button.place(x=870, y=20)
   def back():
     frame1.destroy()
     img1.blank()
     loginpage()
   back_button=Button(frame1,text='LOGOUT',bg='red',fg='white',font=('Arial Black',20,'bold'),command=back)
   back_button.place(x=700,y=430)
   
     #end of home page
 



#login page
 frame=Frame(root,width=1000,height=500,bg='white')
 frame.place(x=0,y=0)
 #image setting
 img=PhotoImage(file='login1.png')
 imglbl=Label(frame,image=img)
 imglbl.place(x=50,y=50)
 head=Label(frame,text='LOG IN',fg='black',bg='white',font=attributes)
 head.place(x=600,y=10)
 # Create labels and entry widgets for username and password
 username_lbl = Label(frame, text="Username:",font=attributes, bg = 'white', fg = 'steel blue')
 username_lbl.place(x=500,y=100)
 username_entry = Entry(frame,font=('Microsoft YaHei UI Light',15,'bold'),width=20,border=2)
 username_entry.place(x=700,y=120)
 use1=username_entry.get()
 password_lbl = Label(frame, text="Password:",font=attributes, bg = 'white', fg = 'steel blue')
 password_lbl.place(x=500,y=200)
 password_entry = Entry(frame, show="*",font=('Microsoft YaHei UI Light',15,'bold'),width=20,border=2)  # Passwords should be hidden with '*'
 password_entry.place(x=700,y=220)
 #showhide passwords
 def show_hide_password():
        if show_password.get():
         password_entry.config(show="")
        else:
         password_entry.config(show="*")
 # Function to validate the login credential
 def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    # Replace these with your actual username and password
    cursor.execute('select * from E;')
    data = cursor.fetchall()
    names = [item[0] for item in data]
    passw = [pas[1] for pas in data]
    if username in names and password in passw:
      if names.index(username)==passw.index(password):
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        homepage(username,password)
        nyf="welcome to on time food"
        voice.setProperty('rate', 100)
        voice.say(nyf)
        voice.runAndWait()
        
      else:
         messagebox.showerror("ERROR","Invalid password")

        
    else:
         messagebox.showerror("ERROR","Invalid username and password")
    return use1
 # Create a login button
 login_button = Button(frame, text="Login", command=validate_login,font=('Segoe UI Emoji',20,'bold'),bg='red',width=15,border=3,fg='white')
 login_button.place(x=600,y=350)
 #showhide checkbox
 show_password = BooleanVar()
 show_password_checkbox = Checkbutton(frame, text="Show Password",fg='black',bg='white', variable=show_password, command=show_hide_password,font=('Cooper Black',15))
 show_password_checkbox.place(x=700,y=270)
 def exit():
   root.destroy()
 exit_button=Button(frame,text='EXIT',fg='black',bg='steel blue',font=('Arial Black',15),command=exit)
 exit_button.place(x=700,y=450)
 #end of login page






loginpage()
# Start the main event loop
root.mainloop()


