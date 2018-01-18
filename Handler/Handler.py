import tkinter as tk

window = tk.Tk()
window.title("test")
window.geometry("300x400")
var = tk.StringVar()
l = tk.Label(window,
             textvariable=var,
             bg="green",
             width=15,
             height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit:
        on_hit = False
        var.set("")
    else:
        on_hit = True
        var.set("you hit me")

b = tk.Button(window,
              text="hit me",
              width=15, height=2,
              command=hit_me)
b.pack()

listBox = tk.Listbox(window,
                     width=15,height=2
                     )
listBox.insert(0,"has2")
listBox.insert(0,"has1")
listBox.insert(0,"hasa")
listBox.pack()

window.mainloop()