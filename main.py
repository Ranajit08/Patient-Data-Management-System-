from tkinter import * 
from tkinter import ttk
import tkinter.font as font
import datetime

def data():
    data = ["CBC", "Fasting Blood Suger", "Lipid Profile", "LFT", "HBsAg"]
    return data

def datev():
    today = datetime.date.today()
    return today


def gui():
    def list_func():
        t = tests.get()
        if t:
            list.insert(END, t)

    def remove_func():
        sel = list.curselection()
        if sel:
            index = sel[0]
            list.delete(index)

    window = Tk()

    window.title("PATIENT DATA MANAGEMENT SYSTEM")
    my_font = font.Font(family='Arial', size=11, weight="bold")
    window.geometry("550x500")
    window.config(bg="#abcbff")

    # tabs 
    style = ttk.Style()
    style.theme_use("default")
    style.configure("TNotebook.Tab", font=my_font, background= "#abcbff", padding= [10,5])
    style.map("TNotebook.Tab", background=[("selected", "#abcbff")])
    notebook = ttk.Notebook(window)

    tab1 = Frame(notebook, bg="#abcbff")
    tab2 = Frame(notebook, bg="#abcbff")
    tab3 = Frame(notebook, bg="#abcbff")

    notebook.add(tab1, text="  Patient Details  ")
    notebook.add(tab2, text="  Paitents data  ")
    notebook.add(tab3, text="  Settings  ")
    
    notebook.pack(expand=True, fill="both")
    

    frame1 = Frame(tab1, bg="#abcbff")
    frame1.grid(row=0, column=0, ipadx=1, ipady=1)

    Label(frame1, text= "", bg="#abcbff").grid(row=0, column=0, columnspan=6)                                                  
    Label(frame1, text= "Date", font=my_font, anchor="w", bg="#abcbff").grid(row=1, column=0, ipadx=23, ipady=2)
    Label(frame1, text= "Name", font=my_font, anchor="w", bg="#abcbff").grid(row=2, column=0, ipadx=19, ipady=2)
    Label(frame1, text= "Age", font=my_font, anchor="w", bg="#abcbff").grid(row=2, column=2, ipadx=25, ipady=2)
    Label(frame1, text= "Gender", font=my_font, anchor="w", bg="#abcbff").grid(row=3, column=0, ipadx=12, ipady=2)
    Label(frame1, text= "Address", font=my_font, anchor="w", bg="#abcbff").grid(row=3, column=2, ipadx=10, ipady=2)
    Label(frame1, text= "Phone No.", font=my_font, anchor="w", bg="#abcbff").grid(row=4, column=0, ipadx=2, ipady=2)
    Label(frame1, text= "Center", font=my_font, anchor="w", bg="#abcbff").grid(row=4, column=2, ipadx=14, ipady=2)
    Label(frame1, text= "", bg="#abcbff").grid(row=4, column=0, columnspan=6)

    date = Entry(frame1, font=('Arial', 11))
    date.grid(row=1, column=1, ipadx=1, ipady=1)
    d = datev()
    date.insert(0, d)
    name = Entry(frame1, font=('Arial', 11)).grid(row=2, column=1, ipadx=1, ipady=1)
    age = Entry(frame1, font=('Arial', 11)).grid(row=2, column=3, ipadx=1, ipady=1)
    gender = ttk.Combobox(frame1, values=["Male", "Female", "Others"], state="readonly", font=('Arial', 10)).grid(row=3, column=1, ipadx=5, ipady=1)
    address = Entry(frame1, font=('Arial', 11)).grid(row=3, column=3, ipadx=1, ipady=1)
    ph = Entry(frame1, font=("Arial", 11)).grid(row=4, column=1, ipadx=1, ipady=1)
    center = Entry(frame1, font=('Arial', 11)).grid(row=4, column=3, ipadx=1, ipady=1)

    val = data()


    frame2 = Frame(tab1, bg="#abcbff")
    frame2.grid(row=1, column=0, ipadx=0, ipady=0)

    Label(frame2, text= "Tests", font=my_font, bg="#abcbff").grid(row=0, column=0, ipadx=0, ipady=0)
    tests = ttk.Combobox(frame2, values=val, state="readonly", font=('Arial', 10))
    tests.grid(row=0, column=1, ipadx=0, ipady=2)
    Button(frame2, text="Add", font=my_font, command=list_func, bg="#4c78be", fg="white").grid(row=0, column=2, ipadx=17, ipady=0)
    Button(frame2, text="Remove", font=my_font, command=remove_func, bg="#4c78be", fg="white").grid(row=0, column=3, ipadx=5, ipady=0)

    list = Listbox(frame2, height=10, width=60)
    list.grid(row=2, column=0, ipadx=0, ipady=0, columnspan=4)

    Label(frame2, text= "  ", bg="#abcbff").grid(row=3, column=0, ipadx=1, ipady=1)
    Label(frame2, text= "Total  →", font=my_font, anchor="e", bg="#abcbff").grid(row=3, column=1, ipadx=1, ipady=1)
    t = Label(frame2, font=my_font, borderwidth=2, text="0000", relief='sunken', bg="#ffffff").grid(row=3, column=2, ipadx=1, ipady=1)
    Button(frame2, text="Calculate", font=my_font, command=remove_func, bg="#4c78be", fg="white").grid(row=3, column=3, ipadx=1, ipady=1)

    frame4 = Frame(tab1, bg="#abcbff")
    frame4.grid(row=3, column=0, ipadx=0, ipady=0)
    Label(frame4, text=" ", bg="#abcbff").grid(row=0, column=0, ipadx=0, ipady=0, columnspan=3)
    Button(frame4, text="Print", font=my_font, bg="#4c78be", fg="white").grid(row=1, column=0, ipadx=5, ipady=0)
    Label(frame4, text="", bg="#abcbff").grid(row=1, column=1, ipadx=15, ipady=0)
    Button(frame4, text="Save", font=my_font, bg="#4c78be", fg="white").grid(row=1, column=2, ipadx=5, ipady=0)


    window.mainloop()


if __name__=='__main__':
    gui()