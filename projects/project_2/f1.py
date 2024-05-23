from tkinter import *
from tkinter import messagebox
total=0
username='0'
root = Tk()
root.title('ON TIME FOOD')
root.resizable(False,False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
attributes=('Segoe UI Emoji',30,'bold')
root.configure(bg='white')

n_frame=Frame(root,width=screen_width,height=screen_height,bg='white')
n_frame.place(x=0,y=0)

n_head=Label(n_frame,text='NGOs LIST',fg='black',bg='white',font=('Georgia',44,'bold'))
n_head.place(x=550,y=50)

n_button1=Button(n_frame,text='NGO-1',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
n_button1.place(x=300,y=160)

n_button2=Button(n_frame,text='NGO-2',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
n_button2.place(x=300,y=290)


n_button3=Button(n_frame,text='NGO-3',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
n_button3.place(x=300,y=420)

n_button4=Button(n_frame,text='NGO-4',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
n_button4.place(x=300,y=550)

#n_frame1=Frame(root,width=550,height=400,bg='white')
#n_frame1.place(x=10,y=150)

Im=PhotoImage(file="ngo.jpg")
Im1=Label(n_frame,image=Im,border=0)
Im1.place(x=150,y=140)


root.mainloop()