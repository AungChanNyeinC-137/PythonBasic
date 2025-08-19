class HelloClass:
    def __init__(self):
        import tkinter
        self.top = tkinter.Tk()

        self.btn = tkinter.Button(self.top,text="ClickMe", command=self.quit)
        self.btn.pack(side="right")

        tkinter.mainloop()
    
    def quit(self):
        import sys
        print("Bye. Have a beautiful day ")
        sys.exit(0)

HelloClass()