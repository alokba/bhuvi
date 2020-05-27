from tkinter import *
import random
import time
from math import *

#creating window
root=Tk()
root.geometry("1600x800+0+0")
root.title('Restuarent Management System')

text_input=StringVar()
operator=""
#=========creating 3 frames==========
Tops=Frame(root,width=1600,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#=============Headings Info===========
localtime=time.asctime(time.localtime(time.time()))
lb1Info=Label(Tops,font=('arial',50,'bold'),text="Restuarent Management Systems",fg="steel Blue",bd=10,anchor='w')
lb1Info.grid(row=0,column=0)
lb1DateTime=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="orange",bd=10,anchor='w')
lb1DateTime.grid(row=1,column=0)

#============Calculator===============
def btnClick(numbers):
    global operator
    operator+=str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    CoF=float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicken_Burger = float(Chicken_Burger.get())
    CoCheese_Burger= float(Cheese_Burger.get())

    CostofFries=CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet= CoFilet * 2.99
    CostofBurger = CoBurger * 2.87
    CostChicken_Burger= CoChicken_Burger * 2.89
    CostCheese_Burger= CoCheese_Burger * 2.69

    CostofMeal="Rs.",str('%.2f' %(CostofFries+CostofDrinks+CostofFilet+CostofBurger
                                 +CostChicken_Burger+CostCheese_Burger))
    PayTax=((CostofFries+CostofDrinks+CostofFilet+CostofBurger
                                 +CostChicken_Burger+CostCheese_Burger)*0.2)
    TotalCost=(CostofFries+CostofDrinks+CostofFilet+CostofBurger
                                 +CostChicken_Burger+CostCheese_Burger)
    Ser_Charge=((CostofFries+CostofDrinks+CostofFilet+CostofBurger
                                 +CostChicken_Burger+CostCheese_Burger)/99)
    Service="Rs.",str('%.2f' %Ser_Charge)
    OverAllCost="Rs.",str('%.2f' % (PayTax +TotalCost+Ser_Charge))
    PaidTax="Rs.",str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")

txtdisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,insertwidth=4,bg="powder blue",bd=30,justify='right')
txtdisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda : btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda : btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda : btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda : btnClick("+")).grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda : btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda : btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda : btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda : btnClick("-")).grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda : btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda : btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda : btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda : btnClick("*")).grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda : btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda :btnClick("/")).grid(row=5,column=3)
#=====================Restuarent Info 1=============
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()

lb1Reference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lb1Reference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtReference.grid(row=0,column=1)

lb1Fries=Label(f1,font=('arial',16,'bold'),text="Large Fries",bd=16,anchor='w')
lb1Fries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtFries.grid(row=1,column=1)

lb1Burger=Label(f1,font=('arial',16,'bold'),text="Burger Meal",bd=16,anchor='w')
lb1Burger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtBurger.grid(row=2,column=1)

lb1Filet=Label(f1,font=('arial',16,'bold'),text="Filet_o_Meal",bd=16,anchor='w')
lb1Filet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtFilet.grid(row=3,column=1)

lb1Chicken=Label(f1,font=('arial',16,'bold'),text="Chicken Meal",bd=16,anchor='w')
lb1Chicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtChicken.grid(row=4,column=1)

lb1Cheese=Label(f1,font=('arial',16,'bold'),text="Cheese Meal",bd=16,anchor='w')
lb1Cheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtCheese.grid(row=5,column=1)
#======================Restuarent Info 2=========
lb1Drinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lb1Drinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtDrinks.grid(row=0,column=3)

lb1cost=Label(f1,font=('arial',16,'bold'),text="cost of Meal",bd=16,anchor='w')
lb1cost.grid(row=1,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtcost.grid(row=1,column=3)

lb1Service=Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lb1Service.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtService.grid(row=2,column=3)

lb1StateTax=Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lb1StateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtStateTax.grid(row=3,column=3)

lb1SubTotal=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w')
lb1SubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtSubTotal.grid(row=4,column=3)

lb1TotalCost=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lb1TotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify=RIGHT)
txtTotalCost.grid(row=5,column=3)

#==================Three Different Buttons==========================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
            text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
            text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
            text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

