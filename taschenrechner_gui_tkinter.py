import tkinter as tk
import operator
win = tk.Tk()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

entry = tk.Entry(win)
entry1 = tk.Entry(win)
win.geometry("200x400")

selected = tk.StringVar(value="+")
menu = tk.OptionMenu(win, selected, "+", "-", "*", "/")
menu.pack()

result_var = tk.StringVar(value="Your result is ...")
tk.Label(win, textvariable=result_var).pack()
def entryaddnumbers():
    num1 = int(entry.get())
    num2 = int(entry1.get())
    op = selected.get()
    res = ops[op](num1,num2)
    return res
def allfuncs():
    res = entryaddnumbers()
    result_var.set(f"Your result is {res}") 
b = tk.Button(
    win,
    text="calc",
    command=allfuncs
)

menu.pack()
b.pack()
entry.pack()
entry1.pack()
win.mainloop()
