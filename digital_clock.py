from tkinter import *
import time  

root = Tk()
root.title('My Digital Clock')
#root.iconbitmap('python_ico.ico') use to replace logo of tkinter with one of your choice
root.geometry('360x320')


#Define the time
def clock():
    hours = time.strftime('%H')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    local = time.strftime('%p')
    day = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%Y')
    day_name = time.strftime('%A')

    clock_label.config(text=hours + ':' + minutes + ':' + seconds + local)
    clock_label.after(1000, clock)
    day_label.config(text= day + '/' + month + '/' + year )
    day_label.after(hours == 00)
    name_day_label.config(text= day_name)
    name_day_label.after(hours == 00)

#Labels
clock_label = Label(root, text="", font=('helvetica', 48), bg='blue', fg='white' )
clock_label.pack(pady=20)

day_label = Label(root, text="", font=('helvetica', 48))
day_label.pack(pady=10)

name_day_label = Label(root, text="", font=('helvetica', 48), fg='purple')
name_day_label.pack(pady=10)
clock()

root.mainloop()