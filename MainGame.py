from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

ActivePlayer=1
p1=[]
p2=[]

root=Tk()

root.title("Tic Tac Toe : O")
style=ttk.Style()
style.theme_use('classic')

#Menambahkan button
b1=ttk.Button(root,text=" ")
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
b1.config(command=lambda: buClick(1))

b2=ttk.Button(root,text=" ")
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda: buClick(2))

b3=ttk.Button(root,text=" ")
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda: buClick(3))

b4=ttk.Button(root,text=" ")
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda: buClick(4))

b5=ttk.Button(root,text=" ")
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda: buClick(5))

b6=ttk.Button(root,text=" ")
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda: buClick(6))

b7=ttk.Button(root,text=" ")
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda: buClick(7))

b8=ttk.Button(root,text=" ")
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda: buClick(8))

b9=ttk.Button(root,text=" ")
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda: buClick(9))

def buClick(ID) :
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(ID,"X")
        p1.append(ID)
        root.title("Tic Tac Toe: Player 2 Turn")
        ActivePlayer=2
        print("P1 : {}".format(p1))
        AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(ID,"O")
        p2.append(ID)
        root.title("Tic Tac Toe: Player 1 Turn")
        ActivePlayer=1
        print("P2 : {}".format(p2))
    CheckWinner()

def SetLayout(id,PlayerSymbol):
    if id==1:
        b1.config(text=PlayerSymbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text=PlayerSymbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text=PlayerSymbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text=PlayerSymbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text=PlayerSymbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text=PlayerSymbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text=PlayerSymbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text=PlayerSymbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text=PlayerSymbol)
        b9.state(['disabled'])

def CheckWinner():
    Winner=-1
    if((1 in p1) and (2 in p1) and (3 in p1)):
        Winner=1
    if((1 in p2) and (2 in p2) and (3 in p2)):
        Winner=2
    
    if((4 in p1) and (5 in p1) and (6 in p1)):
        Winner=1
    if((4 in p2) and (5 in p2) and (6 in p2)):
        Winner=2        

    if((7 in p1) and (8 in p1) and (9 in p1)):
        Winner=1
    if((7 in p2) and (8 in p2) and (9 in p2)):
        Winner=2
        
    if((1 in p1) and (4 in p1) and (7 in p1)):
        Winner=1
    if((1 in p2) and (4 in p2) and (7 in p2)):
        Winner=2
        
    if((2 in p1) and (5 in p1) and (8 in p1)):
        Winner=1
    if((2 in p2) and (5 in p2) and (8 in p2)):
        Winner=2    
    
    if((3 in p1) and (6 in p1) and (9 in p1)):
        Winner=1
    if((3 in p2) and (6 in p2) and (9 in p2)):
        Winner=2    
        
    if Winner==1:
        messagebox.showinfo(title="Selamat!", message="Player 1 Menang")
    elif Winner==2:
        messagebox.showinfo(title="Selamat!", message="Player 2 Menang")

def AutoPlay():
    global p1
    global p2
    EmptyCells=[]
    for cell in range(9):
        if (not ((cell+1 in p1) or (cell+1 in p2))):
            EmptyCells.append(cell+1)
            
    if (p1==[1,2]):
        buClick(EmptyCells[3])
    else:
        RandIndex=randint(0,len(EmptyCells)-1)
        buClick(EmptyCells[RandIndex])

root.mainloop()