from tkinter import *
from tkinter import messagebox
def clearAll():
    dayField.delete(0,END)
    monthField.delete(0,END)
    yearField.delete(0,END)

    given_dayField.delete(0,END)
    given_monthField.delete(0,END)
    given_yearField.delete(0,END)

    result_dayField.delete(0,END)
    result_monthField.delete(0,END)
    result_yearField.delete(0,END)

def checkError():
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or given_dayField.get()=="" 
        or given_monthField.get() == "" or given_yearField.get() == ""):
        messagebox.showerror("Input Error")
        clearAll()
        return -1


def calculateAge():
    value = checkError()
    if value == -1 :
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(given_dayField.get())
        given_month = int(given_monthField.get())
        given_year = int(given_yearField.get())

        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

        if (birth_day > given_day):
            given_month = given_month -1
            given_day = given_day + month[birth_month-1] 
        if(birth_month>given_month):
            given_year = given_year -1
            given_month = given_month +12
        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year
        result_dayField.insert(10,str(calculated_day))
        result_monthField.insert(10,str(calculated_month))
        result_yearField.insert(10,str(calculated_year))
if __name__=="__main__":
    gui = Tk()
    gui.configure(background='light green')
    gui.title('Age Calculator')
    gui.geometry('525x260')
    lbl_dob = Label(gui,text='Date of Birth',bg='blue')
    lbl_givenDate = Label(gui,text='Given Date',bg='blue')
    lbl_day= Label(gui,text='Day',bg='light green')
    lbl_month= Label(gui,text='Month',bg='light green')
    lbl_year= Label(gui,text='Year',bg='light green')

    lbl_givenDay= Label(gui,text='Given Day',bg='light green')
    lbl_givenMonth= Label(gui,text='Given Month',bg='light green')
    lbl_givenYear= Label(gui,text='Given Year',bg='light green')

    lbl_rsltDay= Label(gui,text='Result Day',bg='light green')
    lbl_rsltMonth= Label(gui,text='Result Month',bg='light green')
    lbl_rsltYear= Label(gui,text='Result Year',bg='light green')

    resualtantAge= Button(gui,text='Resultant Age' ,fg='Black' ,bg='Red' ,command=calculateAge)
    clearAllEntry= Button(gui,text='Clear All Entry' ,fg='Black' ,bg='Red' ,command=clearAll)
    
    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)

    given_dayField = Entry(gui)
    given_monthField = Entry(gui)
    given_yearField = Entry(gui)
    
    result_dayField = Entry(gui)
    result_monthField = Entry(gui)
    result_yearField = Entry(gui)

    lbl_dob.grid(row = 0, column = 1) 
    lbl_day.grid(row = 1, column = 0) 
    dayField.grid(row = 1, column = 1) 
    lbl_month.grid(row = 2, column = 0) 
    monthField.grid(row = 2, column = 1) 
    lbl_year.grid(row = 3, column = 0) 
    yearField.grid(row = 3, column = 1) 
    lbl_givenDate.grid(row = 0, column = 4) 
    lbl_givenDay.grid(row = 1, column = 3) 
    given_dayField.grid(row = 1, column = 4) 
    lbl_givenMonth.grid(row = 2, column = 3) 
    given_monthField.grid(row = 2, column = 4) 
    lbl_givenYear.grid(row = 3, column = 3) 
    given_yearField.grid(row = 3, column = 4) 
    resualtantAge.grid(row = 4, column = 2) 
    lbl_rsltYear.grid(row = 5, column = 2) 
    result_yearField.grid(row = 6, column = 2) 
    lbl_rsltMonth.grid(row = 7, column = 2) 
    result_monthField.grid(row = 8, column = 2) 
    lbl_rsltDay.grid(row = 9, column = 2) 
    result_dayField.grid(row = 10, column = 2) 
    clearAllEntry.grid(row = 12, column = 2) 
    gui.mainloop()
