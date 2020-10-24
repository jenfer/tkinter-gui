from tkinter import *

window=Tk()

def km_to_miles():
    #print(km_val.get())
    miles = float(km_val.get()) * 1.6
    t1.insert(END, miles)
    
# Button
b1 = Button(window, text="Execute", command=km_to_miles)
# b1.pack()
b1.grid(row=0,column=0,rowspan=2)

# Input Field
km_val = StringVar()
e1 = Entry(window, textvariable=km_val)
e1.grid(row=0,column=1)

# Text Area
t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=2)

window.mainloop()