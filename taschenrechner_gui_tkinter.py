import tkinter as tk
win = tk.Tk()

entry = tk.Entry(win)
win.geometry("200x400")
win.resizable(True,True)
def allfuncs():
    expression = list(str(entry.get()))
    expression = tokenize(expression)
    expression = solution(expression)
    res = expression
    result_var.set(f"Your result is {res}") 
#rechnungs functionen
def tokenize (arr):
    final = []
    temp = ""

    for idx in range(len(arr)):
        if arr[idx].isdigit() or arr[idx] == ".":
            temp += arr[idx]
        elif arr[idx] == "-" and (idx == 0 or arr[idx-1] in "-*/+"):
            temp += arr[idx]
        elif arr[idx] in "+*-/" and idx != 0:
            final.append(temp)
            temp = ""
            final.append(arr[idx])
    final.append(temp)    
    return final
def solution(arr):
    try:
        i = 0
        while i < len(arr):
            if arr[i] == "*":
                result = float(arr[i-1]) * float(arr[i+1])
                arr[i-1:i+2] = [str(result)]

            elif arr[i] == "/":
                result = float(arr[i-1]) / float(arr[i+1])
                arr[i-1:i+2] = [str(result)]

            else:
                i += 1
        i = 0
        while i < len(arr):
            if arr[i] == "+":
                result = float(arr[i-1]) + float(arr[i+1])
                arr[i-1:i+2] = [str(result)]
            elif arr[i] == "-":
                result = float(arr[i-1]) - float(arr[i+1])
                arr[i-1:i+2] = [str(result)]

            else:
                i += 1
        return arr[-1]

    except (ZeroDivisionError, ValueError, TypeError):
        return "Invalid expression."
result_var = tk.StringVar(value="Your result is ...")
tk.Label(win, textvariable=result_var,wraplength=200).pack()
b = tk.Button(
    win,
    text="Calculator",
    command=allfuncs
)
b.pack()
entry.pack()
win.mainloop()
