# Used tkinter GUI to create a calculator application
from tkinter import*

# This is a simple calculator built with lambda fuction
# It has Addition,Subtraction,Division and Multiplication functionalties.
# It contain 0 to 9 button numbers, clear button and an equal button.


# Used In-built functions for the three below buttons (Button: click, clear and Equal).
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    total=str(eval(operator))
    text_input.set(total)
    operator = ""
    
cal = Tk()
cal.title("Siba's Calculator")
operator = ""
text_input = StringVar()

# ====================Buttons: (7, 8, 9, and +) Displayed and clickable========================

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="pink", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="7",command=lambda:btnClick(7),bg="pink").grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="8",command=lambda:btnClick(8),bg="pink").grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="9",command=lambda:btnClick(9),bg="pink").grid(row=1,column=2)

Addition=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="+",command=lambda:btnClick('+'),bg="pink").grid(row=1,column=3)

# ====================Buttons: (4, 5, 6, and -) Displayed and clickable========================

btn4=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="4",command=lambda:btnClick(4),bg="pink").grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="5",command=lambda:btnClick(5),bg="pink").grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="6",command=lambda:btnClick(6),bg="pink").grid(row=2,column=2)

Subtractio=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="-",command=lambda:btnClick('-'),bg="pink").grid(row=2,column=3)

# ====================Buttons: (1, 2, 3, and *) Displayed and clickable========================

Btn1=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="1",command=lambda:btnClick(1),bg="pink").grid(row=3,column=0)

Btn2=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="2",command=lambda:btnClick(2),bg="pink").grid(row=3,column=1)

Btn3=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="3",command=lambda:btnClick(3),bg="pink").grid(row=3,column=2)

Multiplication_sign=Button(cal,padx=16,bd=8, fg='black', font= ('arial',20,'bold'),
            text="*",command=lambda:btnClick('*'),bg="pink").grid(row=3,column=3)

# ====================Buttons: (C, 0, =, and /) Displayed and clickable========================


BtnClear=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="C",bg="pink",command=btnClearDisplay).grid(row=4,column=0)

Btn0=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="0",command=lambda:btnClick('0'),bg="pink").grid(row=4,column=1)

Equal_sign=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="=",bg="pink" ,command=btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,padx=16,bd=8, fg="black", font= ('arial',20,'bold'),
            text="/",command=lambda:btnClick('/'),bg="pink").grid(row=4,column=3)











cal.mainloop()
