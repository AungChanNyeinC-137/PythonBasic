import tkinter

def quit():
    print("Bye. I'm getting out of here")
    import sys
    sys.exit(0)

def main():
    top = tkinter.Tk()
    
    label1 = tkinter.Label(top, text="HEllo")
    label1.pack(side="left")

    btn = tkinter.Button(top, text="Click ME", command=quit)
    btn.pack(side="right")

    tkinter.mainloop()

main()