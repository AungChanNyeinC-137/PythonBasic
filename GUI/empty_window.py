import tkinter
def main():
    top = tkinter.Tk()
    label1 = tkinter.Label(top,text="HEllo World")
    label1.pack()

    button1 = tkinter.Button(top,text="Click Me",command=top.quit())
    button1.pack(side="left")
    top.mainloop()
main()