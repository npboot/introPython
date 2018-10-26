from tkinter import *
import math
def clicked():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def clicked2():
   grondgetal = int(entry.get())
   wortel = math.sqrt(grondgetal)
   label["text"] = 'Wortel is: ' + str(wortel)
root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

button2 = Button(master=root, text='Wortel',command=clicked2)
button2.pack()

entry = Entry(master=root)
entry.pack(padx=10, pady=10)


root.mainloop()
