from tkinter import *
from random import randint

def calculateRoll():
    sum = 0
    for _ in range(int(entry1.get())):
        sum += randint(1, int(entry2.get()))
    sum += int(entry3.get())
    entry4.delete(0, END)
    entry4.insert(END, str(sum))
    

def reset():
    entry1.delete(0, END)
    entry1.insert(END, "1")
    entry2.delete(0, END)
    entry2.insert(END, "20")
    entry3.delete(0, END)
    entry3.insert(END, "0")
    entry4.delete(0, END)
    entry4.insert(END, "0")
    

root = Tk()

root.geometry("500x500")

root.title('Die Roller')

# Title
label0 = Label(root,text='Die Roller', width=20,font=("bold",20))
label0.place(x=90,y=60)

# Label and Entry for Number of dice
label1 = Label(root,text="Number of Dice:", width=20,font=("bold",10))
label1.place(x=80,y=130)
entry1 = Entry(root)
entry1.place(x=240,y=130)
entry1.insert(END, "1")

# Label and Entry for Number of Sides on each die
label2 = Label(root,text="Number of Sides:", width=20,font=("bold",10))
label2.place(x=78,y=180)
entry2 = Entry(root)
entry2.place(x=240,y=180)
entry2.insert(END, "20")

# Label and Entry for Modifier
label3 = Label(root,text="Modifier:", width=20,font=("bold",10))
label3.place(x=88,y=230)
entry3 = Entry(root)
entry3.place(x=240,y=230)
entry3.insert(END, "0")

# Submit and Reset Button
Button(root, text='Submit' , width=10,bg="black",fg='white', command=calculateRoll).place(x=150,y=280)
Button(root, text='Reset' , width=10,bg="black",fg='white', command=reset).place(x=260,y=280)

# Label and Entry for Resulting roll
label4 = Label(root,text="Roll:", width=20,font=("bold",10))
label4.place(x=88,y=330)
entry4 = Entry(root)
entry4.place(x=240,y=330)
entry4.insert(END, "0")

#this will run the mainloop.
root.mainloop()