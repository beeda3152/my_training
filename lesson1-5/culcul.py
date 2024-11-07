import tkinter as tk
def g_v():
    num1 = int(n1.get())
    num2 = int(n2.get())
    return num1, num2
def i_v(res):
    #n3.delete(0, 'end')
    n3.insert(0, res)

def add():
    num1, num2 = g_v()
    res = num2 + num1
    i_v(res)
def sub():
    num1, num2 = g_v()
    res = num1 - num2
    i_v(res)
def mul():
    num1, num2 = g_v()
    res = num2 * num1
    i_v(res)
def div():
    num1, num2 = g_v()
    res = num1 / num2
    i_v(res)
def ex1():
    win1.quit()

win1 = tk.Tk()

win1.title('Калкулятор')
win1.geometry("350x350")
win1.resizable(False,False)
button_add = tk.Button(win1, text="+", width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(win1, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(win1, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(win1, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)
button_ex = tk.Button(win1, text="Выход", width=10, command=ex1)
button_ex.place(x=150, y=315)
n1 =tk.Entry(win1, width=28)
n1.place(x=100, y=75)
n2 =tk.Entry(win1, width=28)
n2.place(x=100, y=150)
n3 =tk.Entry(win1, width=28)
n3.place(x=100, y=280)
n11 = tk.Label(win1, text="Ввудите первое число: ")
n11.place(x=100, y=50)
n12 = tk.Label(win1, text="Ввудите второе число: ")
n12.place(x=100, y=125)
n13 = tk.Label(win1, text="Ответ: ")
n13.place(x=100, y=260)

win1.mainloop()