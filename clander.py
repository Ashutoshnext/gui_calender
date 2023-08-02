from tkinter import *
from  tkcalendar import *
 
root=Tk()

root.title("Calender")
root.geometry('700x500')
root.config(bg='navyblue')

cal=Calendar(root,selectmode="day", year=2010, month=12, day=2, background="red")
cal.pack(pady=20)

def grab_date():
    my_label.config(text=cal.get_date())
button=Button(root, background='black',foreground='red', font=('arial',15,'bold'), text="Slect Date",  command=grab_date)
button.pack(pady=20)
my_label=Label(root,background="navyblue",foreground='white' ,font=('arial',15,'bold'))
my_label.pack(pady=20)

root.mainloop()