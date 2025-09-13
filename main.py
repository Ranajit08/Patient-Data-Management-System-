from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font
from logics import data_logic

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
    window.geometry("1400x1500")
    window.config(bg="#abcbff")

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
    
    tab1_frame = Frame(tab1, bg="#abcbff" )
    tab1_frame.pack(expand = True)
    frame1 = Frame(tab1_frame, bg="#abcbff")
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
    date_i = data_logic.datev()
    date.insert(0, date_i)
    name = Entry(frame1, font=('Arial', 11))
    name.grid(row=2, column=1, ipadx=1, ipady=1)
    age = Entry(frame1, font=('Arial', 11))
    age.grid(row=2, column=3, ipadx=1, ipady=1)
    gender = ttk.Combobox(frame1, values=["Male", "Female", "Others"], state="readonly", font=('Arial', 10))
    gender.grid(row=3, column=1, ipadx=5, ipady=1)
    address = Entry(frame1, font=('Arial', 11))
    address.grid(row=3, column=3, ipadx=1, ipady=1)
    ph = Entry(frame1, font=("Arial", 11))
    ph.grid(row=4, column=1, ipadx=1, ipady=1)
    center = Entry(frame1, font=('Arial', 11))
    center.grid(row=4, column=3, ipadx=1, ipady=1)

    val = data_logic.data()

    frame2 = Frame(tab1_frame, bg="#abcbff")
    frame2.grid(row=1, column=0, ipadx=0, ipady=0)

    Label(frame2, text= "Tests", font=my_font, bg="#abcbff").grid(row=0, column=0, ipadx=0, ipady=0)
    tests = ttk.Combobox(frame2, values=val, state="readonly", font=('Arial', 10))
    tests.grid(row=0, column=1, ipadx=0, ipady=2)
    Button(frame2, text="Add", font=my_font, command=list_func, bg="#4c78be", fg="white").grid(row=0, column=2, ipadx=17, ipady=1)
    Button(frame2, text="Remove", font=my_font, command=remove_func, bg="#4c78be", fg="white").grid(row=0, column=3, ipadx=1, ipady=1)

    list = Listbox(frame2, height=10, width=60)
    list.grid(row=2, column=0, ipadx=0, ipady=0, columnspan=4)

    def calculate():
        test_list = list.get(0, END)
        lebel_calc = t.get()
        if lebel_calc:
            t.delete(0, END)
            calc = data_logic.calculate(test_list)
            t.insert(0, calc)
        else:
            e_clac =  data_logic.calculate(test_list)
            t.insert(0, e_clac)
            
    Label(frame2, text= "Total→", font=my_font, anchor="e", bg="#abcbff").grid(row=3, column=0, ipadx=1, ipady=1)
    t = Entry(frame2, font=('Arial', 10))
    t.grid(row=3, column=1, ipadx=1, ipady=1)
    Button(frame2, text="Calculate", font=my_font, command=calculate, bg="#4c78be", fg="white").grid(row=3, column=2, ipadx=1, ipady=1)

    def clear_all():
        date_12 = date.get()
        if date_12:
            date.delete(0, END)
            date.insert(0, date_i)
        else:
            date.insert(0, date_i)
        n = name.get()
        if n:
            name.delete(0, END)
        a = age.get()
        if a:
            age.delete(0, END)
        ad = address.get()
        if ad:
            address.delete(0, END)
        p = ph.get()
        if p:
            ph.delete(0, END)
        c = center.get()
        if c:
            center.delete(0, END)
        list.delete(0, END)

    def save():
        i_date = date.get()
        i_name = name.get()
        i_age = age.get()
        i_gender = gender.get()
        i_address = address.get()
        i_ph = ph.get()
        i_center = center.get()  
        i_list = list.get(0, END)

        if all([ i_date, i_name, i_age, i_gender, i_address, i_ph, i_center, i_list]):
            bool = data_logic.save_data([i_date, i_name, i_age, i_gender, i_ph, i_center, i_list, i_address])
            if bool == True:
                messagebox.showinfo("Save", "Data successfully saved :)")
            if bool == False:
                messagebox.showwarning("Save", "Some problem occurs :(")
        else:
            if i_date and not any([i_name, i_age, i_gender, i_address, i_ph, i_center, i_list]):
                messagebox.showerror("Error", "Some fields are blank :(")
            else:
                messagebox.showerror("Error", "Some fields are blank :(")


    frame4 = Frame(tab1_frame, bg="#abcbff")
    frame4.grid(row=3, column=0, ipadx=0, ipady=0)
    Label(frame4, text="", bg="#abcbff").grid(row=0, column=0, ipadx=15, ipady=0, columnspan=5)
    Button(frame4, text="Clear All", font=my_font, bg="#4c78be", fg="white", command=clear_all).grid(row=1, column=0, ipadx=5, ipady=0)
    Label(frame4, text="", bg="#abcbff").grid(row=1, column=1, ipadx=15, ipady=0)
    Button(frame4, text="Print", font=my_font, bg="#4c78be", fg="white", command=data_logic.pdf).grid(row=1, column=2, ipadx=5, ipady=0)
    Label(frame4, text="", bg="#abcbff").grid(row=1, column=3, ipadx=15, ipady=0)
    Button(frame4, text="Save", font=my_font, bg="#4c78be", fg="white", command=save).grid(row=1, column=4, ipadx=5, ipady=0)
    

    tab2_frame = Frame(tab2, bg="#abcbff" )
    tab2_frame.pack(expand = True)
    
    frame1_tab2 = Frame(tab2_frame, bg="#abcbff")
    frame1_tab2.grid(row=0, column=0, ipadx=1, ipady=1)

    l = Text(frame1_tab2, height=50, width=170, wrap="word")
    l.grid(row=1, column=0, ipadx=0, ipady=0, columnspan=4)
    d = data_logic.user_data()
    l.insert(END, d)
    l.config(state="disabled")


    window.mainloop()


if __name__=='__main__':
    gui()