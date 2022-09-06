from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("resistor colour code")
root.geometry("800x700")
root.resizable(False,False)
#function
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()

var_1.set(" ")
var_2.set(" ")
var_3.set(" ")
var_4.set(" ")
var_5.set(" ")
#DEFINING FUNCTION FOR RESET
def res():
    var_1.set("")
    var_2.set("")
    var_3.set("")
    var_4.set("")
    var_5.set("")
#DEFINING FUNCTION FOR RESULT
def final():
    a = str(var_1.get())+str(var_2.get())
    print(a)
    a = int(a)
    b = a * int(var_3.get())
    var_5.set(b)

    
#for band 1
def b1_black():
    var_1.set(0)
def b1_brown():
    var_1.set(1)
def b1_red():
    var_1.set(2)
def b1_orange():
    var_1.set(3)
def b1_yellow():
    var_1.set(4)
def b1_green():
    var_1.set(5)
def b1_blue():
    var_1.set(6)
def b1_violet():
    var_1.set(7)
def b1_grey():
    var_1.set(8)
def b1_white():
    var_1.set(9)

#for band 2
def b2_black():
    var_2.set(0)
def b2_brown():
    var_2.set(1)
def b2_red():
    var_2.set(2)
def b2_orange():
    var_2.set(3)
def b2_yellow():
    var_2.set(4)
def b2_green():
    var_2.set(5)
def b2_blue():
    var_2.set(6)
def b2_violet():
    var_2.set(7)
def b2_grey():
    var_2.set(8)
def b2_white():
    var_2.set(9)
    
#for band 3
def b3_black():
    var_3.set(1)
def b3_brown():
    var_3.set(10)
def b3_red():
    var_3.set(100)
def b3_orange():
    var_3.set(1000)
def b3_yellow():
    var_3.set(10000)
def b3_green():
    var_3.set(100000)
def b3_blue():
    var_3.set(1000000)
def b3_violet():
    var_3.set(10000000)
def b3_grey():
    var_3.set(100000000)
def b3_white():
    var_3.set(1000000000)
def b3_gold():
    var_3.set(0.1)
def b3_silver():
    var_3.set(0.01)

#for forth band
def b4_gold():
    var_4.set(5)
def b4_silver():
    var_4.set(10)
 
#framing
f1 = Frame(root, bg =  "white" )
f1.pack(side = "top" , fill = "x")

f2 = Frame(root, bg =  "grey" )
f2.pack(fill = "y",side="left")

f4 = Frame(root,bg = "grey")
f4.pack(fill = "y",side = "left",padx = 10)

f3 = Frame(root, bg =  "grey" )
f3.pack(fill = "y",side="left")

f5 = Frame(root, bg =  "grey" )
f5.pack(fill = "y",side="left",padx = 10)

f6 = Frame(root, bg =  "grey" )
f6.pack(fill = "y",side="right")
#photo
'''photo = PhotoImage(file = "//Users//vinayakbirajdar//Desktop//image//resistor.png")
p1 = Label(image=photo)
p1.pack(side="top",anchor = "e")'''

#text
l1 = Label(f1,text = ("****RESISTANCE DETERMINER****") ,relief = RIDGE ,borderwidth = 3,
            font = ("comicsanms","30"))
l1.pack(pady = 2)

l2 = Label(f2 , text = ("1st band colour"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l2.pack()

l3 = Label(f4 , text = ("2nd band colour"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l3.pack()

l4 = Label(f3 , text = ("3rd band colour"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l4.pack()

l5 = Label(f5 , text = ("4rd band colour"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l5.pack()


#button
b1 = Button(f2,text = ("BLACK"), font = ("comicsanms","20") ,
            bg = "black" , command = b1_black )
b1.pack(side = "top", pady = "6",anchor = "w")

b2 = Button(f2,text = ("BROWN"),fg = "brown", font = ("comicsanms","20") , bg = "brown"
            ,command = b1_brown)
b2.pack(side = "top", pady = "6",anchor = "w")

b3 = Button(f2,text = ("   RED    "),fg = "red", font = ("comicsanms","20") , bg = "red"
            ,command = b1_red)
b3.pack(side = "top", pady = "6",anchor = "w")

b4 = Button(f2,text = (" ORANGE"),fg = "orange", font = ("comicsanms","20") , bg = "orange"
            ,command = b1_orange)
b4.pack(side = "top", pady = "6",anchor = "w")

b5 = Button(f2,text = (" YELLOW "),fg = "yellow", font = ("comicsanms","20") , bg = "yellow"
            ,command = b1_yellow)
b5.pack(side = "top", pady = "6",anchor = "w")

b6 = Button(f2,text = (" GREEN "),fg = "green", font = ("comicsanms","20") , bg = "green"
            ,command = b1_green)
b6.pack(side = "top", pady = "6",anchor = "w")

b7 = Button(f2,text = (" BLUE  "),fg = "blue", font = ("comicsanms","20") , bg = "blue"
            ,command = b1_blue)
b7.pack(side = "top", pady = "6",anchor = "w")

b8 = Button(f2,text = (" VIOLTE  "),fg = "violet", font = ("comicsanms","20") ,
            bg = "violet",command = b1_violet)
b8.pack(side = "top", pady = "6",anchor = "w")

b9 = Button(f2,text = (" GREY  "),fg = "grey", font = ("comicsanms","20") , bg = "grey"
            ,command = b1_grey)
b9.pack(side = "top", pady = "6",anchor = "w")

b10 = Button(f2,text = (" WHITE  "),fg = "black", font = ("comicsanms","20") ,
             bg = "white",command = b1_white)
b10.pack(side = "top", pady = "6",anchor = "w")

b11 = Button(f2,text = (" GOLD  "),fg = "gold", font = ("comicsanms","20") , bg = "gold")
b11.pack(side = "top", pady = "6",anchor = "w")

b12 = Button(f2,text = (" SILVER"),fg = "silver", font = ("comicsanms","20") , bg = "silver")
b12.pack(side = "top", pady = "6",anchor = "w")

#condition for 2nd band
b14= Button(f4,text = (" BLACK   "),fg = "black", font = ("comicsanms","20") ,
           bg = "black" ,command = b2_black )
b14.pack(side = "top", pady = "6",anchor = "w")

b15 = Button(f4,text = (" BROWN  "),fg = "brown", font = ("comicsanms","20") ,
             bg = "brown",command = b2_brown )
b15.pack(side = "top", pady = "6",anchor = "w")

b16 = Button(f4,text = (" RED  "),fg = "red", font = ("comicsanms","20") , bg = "red"
             ,command = b2_red )
b16.pack(side = "top", pady = "6",anchor = "w")

b17 = Button(f4,text = (" ORANGE"),fg = "orange", font = ("comicsanms","20") ,
             bg = "orange",command = b2_orange)
b17.pack(side = "top", pady = "6",anchor = "w")

b18 = Button(f4,text = (" YELLOW "),fg = "yellow", font = ("comicsanms","20") ,
             bg = "yellow",command = b2_yellow)
b18.pack(side = "top", pady = "6",anchor = "w")

b19 = Button(f4,text = (" GREEN "),fg = "green", font = ("comicsanms","20") , bg = "green"
             ,command = b2_green)
b19.pack(side = "top", pady = "6",anchor = "w")

b20 = Button(f4,text = (" BLUE  "),fg = "blue", font = ("comicsanms","20") , bg = "blue"
             ,command = b2_blue)
b20.pack(side = "top", pady = "6",anchor = "w")

b21 = Button(f4,text = (" VIOLTE  "),fg = "violet", font = ("comicsanms","20") ,
             bg = "violet",command = b2_violet)
b21.pack(side = "top", pady = "6",anchor = "w")

b22 = Button(f4,text = (" GREY  "),fg = "grey", font = ("comicsanms","20") , bg = "grey"
             ,command = b2_grey)
b22.pack(side = "top", pady = "6",anchor = "w")

b23 = Button(f4,text = (" WHITE  "),fg = "black", font = ("comicsanms","20") ,
             bg = "white",command = b2_white)
b23.pack(side = "top", pady = "6",anchor = "w")

b24 = Button(f4,text = (" GOLD  "),fg = "gold", font = ("comicsanms","20") , bg = "gold")
b24.pack(side = "top", pady = "6",anchor = "w")

b25 = Button(f4,text = (" SILVER"),fg = "silver", font = ("comicsanms","20") , bg = "silver")
b25.pack(side = "top", pady = "6",anchor = "w")

#condition for 3nd band
b26 = Button(f3,text = (" BLACK   "),fg = "black", font = ("comicsanms","20") ,
            bg = "black",command = b3_black)
b26.pack(side = "top" ,pady = "6" ,anchor = "w")

b27 = Button(f3,text = ("BROWN"),fg = "brown", font = ("comicsanms","20") , bg = "brown",
             command = b3_brown)
b27.pack(side = "top", pady = "6",anchor = "w")

b28 = Button(f3,text = ("   RED    "),fg = "red", font = ("comicsanms","20") , bg = "red"
             ,command = b3_red)
b28.pack(side = "top", pady = "6",anchor = "w")

b29 = Button(f3,text = (" ORANGE"),fg = "orange", font = ("comicsanms","20") ,
             bg = "orange",command = b3_orange)
b29.pack(side = "top", pady = "6",anchor = "w")

b30 = Button(f3,text = (" YELLOW "),fg = "yellow", font = ("comicsanms","20") ,
             bg = "yellow",command = b3_yellow)
b30.pack(side = "top", pady = "6",anchor = "w")

b31 = Button(f3,text = (" GREEN "),fg = "green", font = ("comicsanms","20") , bg = "green"
             ,command = b3_green)
b31.pack(side = "top", pady = "6",anchor = "w")

b32 = Button(f3,text = (" BLUE  "),fg = "blue", font = ("comicsanms","20") , bg = "blue"
             ,command = b3_blue)
b32.pack(side = "top", pady = "6",anchor = "w")

b33 = Button(f3,text = (" VIOLTE  "),fg = "violet", font = ("comicsanms","20") ,
             bg = "violet",command = b3_violet)
b33.pack(side = "top", pady = "6",anchor = "w")

b34 = Button(f3,text = (" GREY  "),fg = "grey", font = ("comicsanms","20") , bg = "grey",
             command = b3_grey)
b34.pack(side = "top", pady = "6",anchor = "w")

b35 = Button(f3,text = (" WHITE  "),fg = "black", font = ("comicsanms","20") ,
             bg = "white",command = b3_white)
b35.pack(side = "top", pady = "6",anchor = "w")

b36 = Button(f3,text = (" GOLD  "),fg = "gold", font = ("comicsanms","20") , bg = "gold"
             ,command = b3_gold)
b36.pack(side = "top", pady = "6",anchor = "w")

b37 = Button(f3,text = (" SILVER"),fg = "silver", font = ("comicsanms","20") ,
             bg = "silver",command = b3_silver)
b37.pack(side = "top", pady = "6",anchor = "w")


#condition for 4th band
b38 = Button(f5,text = (" GOLD  "),fg = "gold", font = ("comicsanms","20") , bg = "gold"
             ,command = b4_gold)
b38.pack(side = "top", pady = "6",anchor = "w")

b39 = Button(f5,text = (" SILVER"),fg = "silver", font = ("comicsanms","20"),bg = "silver"
             ,command = b4_silver)
b39.pack(side = "top", pady = "6",anchor = "w")
#label
l7 = Label(f6 , text = ("1st band choice"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l7.pack()
#taking entry
entry = Entry(f6)
entry.config(font=("ink free",30),textvariable = var_1)
entry.pack(side = "top")

l8 = Label(f6 , text = ("2nd band choice"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l8.pack()
entry_1 = Entry(f6)
entry_1.config(font=("ink free",30),textvariable = var_2)
entry_1.pack(side = "top")

l9 = Label(f6 , text = ("3rd band choice"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l9.pack()

entry_2 = Entry(f6)
entry_2.config(font=("ink free",30),textvariable = var_3)
entry_2.pack(side = "top")

l10 = Label(f6 , text = ("4st band choice"),bg = "grey", fg = "white",relief = "groove"
           ,font = ("comicsanms","20"))
l10.pack()
entry_3 = Entry(f6)
entry_3.config(font=("ink free",30),textvariable = var_4)
entry_3.pack(side = "top")

b50 = Button(f6,text = "RESULT", fg = "black" ,bg = "black",
             font = ("comicsanms","20"),command=final)
b50.pack(pady = "20")

entry_4 = Entry(f6)
entry_4.config(font=("ink free",30) ,textvariable = var_5 )
entry_4.pack(side = "top")

b51 = Button(f6,text = "RESET", fg = "black" ,bg = "black",
             font = ("comicsanms","20"),command = res)
b51.pack(pady = "20")

root.mainloop()
