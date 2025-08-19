import tkinter

class IntegerMultiply:
    def __init__(self):
        self.intmultiply = tkinter.Tk()
        self.intmultiply.title("Integer Multiply")
        self.var1 = tkinter.IntVar()
        self.entry1 = tkinter.Entry(self.intmultiply,
                                    textvariable = self.var1, width=20)
        self.entry1.pack()
        self.mulbutton = tkinter.Button(self.intmultiply, text="Multiply",
                                        command=self.multiply)
        self.mulbutton.pack()
        
    def multiply(self):
        import random
        a = random.randint(1,100)
        b = int(self.entry1.get())
        self.entry1.delete(0,'end')
        self.entry1.insert(0,a*b)
        self.intmultiply.mainloop()

top = tkinter.Tk()
top.title("Assignment")
top.geometry("500x500")

IMButton = tkinter.Button(top, text ="Integer Multiply" , command= IntegerMultiply)
IMButton.pack()
tkinter.mainloop()