import tkinter

def hello(event):
    print("Double Click to Exit ,HMR?")
    
def quit(event):
    print("Bye. I'm getting out of here")
    import sys
    sys.exit(0)

def main():
    top = tkinter.Tk()
    
    label1 = tkinter.Label(top, text="HEllo")
    label1.pack(side="left")

    btn = tkinter.Button(top, text="Hello Event World")
    btn.pack(side="right")
    btn.bind("<Button-1>",hello)
    btn.bind("<Double-1>",quit)
    tkinter.mainloop()

main()