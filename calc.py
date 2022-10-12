
import tkinter as Tk
from tkinter import*

root = Tk()
root.title("Advanced Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column = 0, columnspan = 3,padx=10, pady =10)

f_num = opr = None

def button_click(number=None):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current+str(number))

def button_opr(op):
    global f_num, opr
    # save the first number and operator
    try:
        f_num = int(e.get())
        opr = op
        # clear the entry
        e.delete(0, END)
    except Exception as ex:
        print(ex)

def button_clear():
    global f_num, opr
    e.delete(0, END)
    # reset first number and operator
    f_num = opr = None

def button_equal():
    global f_num, opr
    if f_num and opr:
        try:
            current = int(e.get())
            e.delete(0, END)
            if opr == "+":
                e.insert(0, f_num+current)
            elif opr == "-":
                e.insert(0, f_num-current)
            elif opr == "*":
                e.insert(0, f_num*current)
            elif opr == "/":
                e.insert(0, f_num/current)
            elif opr == "^":
                e.insert(0, f_num**current)
        except Exception as ex:
            print(ex)
    # reset first number and operator
    f_num = opr = None

def button_subtract():
    
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

    


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

    


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

    


def button_decimal():
    return
def button_sb1():
    return

def button_sb2():
    return

def button_cb1():
    return

def button_cb2():
    return


def button_Sin():
    return

def button_Cos():
    return

def button_Tan():
    return

def button_Cot():
    return

def button_Squar_Root():
    return

def button_Percentage():
    return

def button_Power():
    return

def button_Ln():
    return

def button_Log():
    return

def button_Square_Root():
    return

def button_Back_Space():
    return

# making buttons
button_1 = Button(root, text = "1", padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx=40, pady=20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx=40, pady=20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx=40, pady=20, command= lambda: button_opr("+"))
button_clear = Button(root, text = "Clear", padx=40, pady=20, command = button_clear)

button_subtract = Button(root, text = "-", padx=40, pady=20, command = lambda: button_opr("-"))
button_multiply = Button(root, text = "*", padx=40, pady=20, command = lambda: button_opr("*"))
button_divide = Button(root, text = "/", padx=40, pady=20, command = lambda: button_opr("/"))
button_equal = Button(root, text = "=", padx=40, pady=20, command = button_equal)

button_decimal = Button(root, text = ".", padx=40, pady=20, command = lambda: button_click("."))

button_sb1 = Button(root, text = "(", padx=40, pady=20, command = lambda: button_click("("))
button_sb2 = Button(root, text = ")", padx=40, pady=20, command = lambda: button_click(")"))
button_cb1 = Button(root, text = "{", padx=40, pady=20, command =  lambda: button_click("{"))
button_cb2 = Button(root, text = "}", padx=40, pady=20, command = lambda:  button_click("}"))

button_Sin = Button(root, text = "Sin", padx=40, pady=20, command = lambda: button_click("Sin"))
button_Cos = Button(root, text = "Cos", padx=40, pady=20, command = lambda: button_click("Cos"))
button_Tan = Button(root, text = "Tan", padx=40, pady=20, command = lambda: button_click("Tan"))
button_Cot = Button(root, text = "Cot", padx=40, pady=20, command = lambda: button_click("Cot"))
button_Square_Root = Button(root, text = "Sqrt", padx=40, pady=20, command = lambda: button_click("Sqrt"))
button_Back_Space = Button(root, text = "BackSpace", padx=30, pady=20, command =  button_Back_Space)

button_Power = Button(root, text = "^", padx=40, pady=20, command = lambda: button_click("^"))
button_Percentage = Button(root, text = "%", padx=40, pady=20, command = lambda: button_click("%"))
button_Ln = Button(root, text = "Ln", padx=40, pady=20, command = lambda: button_click("Ln"))
button_Log = Button(root, text = "Log(10)", padx=40, pady=20, command = lambda: button_click("Log"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=0)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)

button_9.grid(row=1, column=2)


button_0.grid(row=4, column=0)


button_clear.grid(row=6, column=4)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)

button_decimal.grid(row=5, column=3)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=2)

button_divide.grid(row=5, column=2)
button_sb1.grid(row=1, column=3)
button_sb2.grid(row=2, column=3)
button_cb1.grid(row=3, column=3)
button_cb2.grid(row=4, column=3)

button_Sin.grid(row=1, column=4)
button_Cos.grid(row=2, column=4)
button_Tan.grid(row=3, column=4)
button_Cot.grid(row=4, column=4)

button_Square_Root.grid(row=5, column=4)

button_Back_Space.grid(row=4, column=1)
button_Ln.grid(row=6, column=0)
button_Log.grid(row=6, column=1)
button_Percentage.grid(row=6, column=2)
button_Power.grid(row=6, column=3)



#myButton = Button(root, text= "Perform calculation")

#myButton.pack()
root.mainloop()



