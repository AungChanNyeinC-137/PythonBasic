import tkinter

class DollarToKyat:
    def __init__(self):
        self.dollartokyat = tkinter.Tk()
        self.dollartokyat.title("US Dollar To Kyat")

        self.var1 = tkinter.IntVar()
        self.entry1 = tkinter.Entry(self.dollartokyat,
                                    textvariable = self.var1, width=8)
        self.var2 = tkinter.IntVar()
        self.entry2 = tkinter.Entry(self.dollartokyat,
                                    textvariable = self.var2, width=8)
        
        self.label1 = tkinter.Label(self.dollartokyat, text= "Dollar")
        self.label2 = tkinter.Label(self.dollartokyat, text= "is qeuivalent to")
        self.label3 = tkinter.Label(self.dollartokyat, text= "Kyat")
        
        self.mulbutton = tkinter.Button(self.dollartokyat, text="Calculate",
                                        command=self.calculate)
        self.entry1.grid(row=0, column=1)
        self.label1.grid(row=0, column=2)
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.label3.grid(row=1, column=2)
        self.mulbutton.grid(row=2, column=2)

    def calculate(self):
        d = int(self.entry1.get())
        self.entry2.delete(0,'end')
        self.entry2.insert(0, d * 4000)
        self.dollartokyat.mainloop()

top = tkinter.Tk()
top.title("Assignment I")
top.geometry("500x500")

IMButton = tkinter.Button(top, text ="US Dollar To Kyat" , command= DollarToKyat)
IMButton.pack()
tkinter.mainloop()