# Program Kalkulator
# Kalkulator.py
 
# mengimport module Tkinter
from Tkinter import *
 
# mendefinisikan variabel awal
bil1="0"
bil2="0"
operator="nihil"
hasil = "kosong"
<br># method untuk menginputkan . 
def points():
    global bil1
    global bil2
    getv = masukan.get()
    if "." not in getv:
       masukan.delete(0, END)
       masukan.insert(0, getv+".")
       if getv == bil1:
           bil1 = getv+"."
       else:
           bil2 = getv+"."
 
def input_field(x):
    global bil1
    global bil2
    global operator
    global hasil
    if operator == "nihil" and hasil == "kosong":
        get_value = masukan.get()
        masukan.delete(0,END)
        masukan.insert(0 , get_value+x)
        bil1 = get_value+x
    elif operator != "nihil" and hasil == "kosong":
        get_value = masukan.get()
        if get_value == bil1:
            masukan.delete(0,END)
            masukan.insert(0 , x)
            bil2 = x
        else :
            masukan.delete(0,END)
            masukan.insert(0 , get_value+x)
            bil2 = get_value+x
    elif operator == "nihil" and hasil != "kosong" and bil1 != "0":
        getv = masukan.get()
        if "." in getv:
            masukan.delete(0,END)
            masukan.insert(0, getv+x)
            bil1 = getv+x
        else :
            masukan.delete(0,END)
            masukan.insert(0,x)
            bil1 = x
        hasil = "kosong"
    elif operator != "nihil" and hasil != "kosong":
        g = masukan.get()
        if g == bil1:
            masukan.delete(0 , END)
            masukan.insert(0, x)
            bil2 = x
        else :
            masukan.delete(0, END)
            masukan.insert(0, g+x)
            bil2 = g+x
def clear():
    global bil1
    global bil2
    global operator
    global hasil
    masukan.delete(0,END)
    bil1 = "0"
    bil2 = "0"
    operator = "nihil"
    hasil = "kosong"
 
def set_operator(x):
    global operator
 
    if operator == "nihil":
        operator = x
    else :
        eksekusi()
        operator = x
     
         
 
def eksekusi():
    global bil1
    global bil2
    global operator
    global hasil
    if operator != "nihil":
        if operator == "/" and bil2 == "0":
            masukan.delete(0, END)
            masukan.insert(0, "Error!")
            hasilnya = "susah"
            bil1 = hasilnya
        else:
            exec("hasilnya = %s %s %s" % (bil1,operator,bil2))
            masukan.delete(0,END)
            masukan.insert(0, hasilnya)
            bil1 = "%i" % hasilnya
    else :
        hasilnya = bil1
        bil1 = hasilnya
    bil2 = "0"
    operator = "nihil"
def bilbul():
    global bil1
    global bil2
    global opertor
    getv = masukan.get()
    if getv == bil1:
        masukan.delete(0, END)
        exec("res = %s * -1" % getv)
        masukan.insert(0, res)
        bil1 = "%i" % res
    else :
        masukan.delete(0, END)
        exec("res = %s * -1" % getv)
        masukan.insert(0, res)
        bil2 = "%i" % res
         
root = Tk()
 
# mendefinisikan setiap komponen
masukan = Entry(width=20, font=("verdana",20), justify="right")                 # membuat text field
satu = Button(text="1", width=5, font=("verdana",13, "bold"), command= lambda x="1": input_field(x))                   # membuat tombol angka 1
dua = Button(text="2",width=5,font=("verdana",13, "bold"), command= lambda x="2": input_field(x))                      # membuat tombol angka 2
tiga = Button(text="3",width=5, font=("verdana",13, "bold"), command= lambda x="3": input_field(x))                    # membuat tombol angka 3
clear = Button(text="C", width=11,font=("verdana",13, "bold"), command=clear)                  # membuat tombol clear
empat = Button(text="4",width=5, font=("verdana",13, "bold"), command= lambda x="4": input_field(x))                   # membuat tombol angka 4
lima = Button(text="5",width=5, font=("verdana",13, "bold"), command= lambda x="5": input_field(x))                    # membuat tombol angka 5
enam = Button(text="6",width=5, font=("verdana",13, "bold"), command= lambda x="6": input_field(x))                    # mebuat tombol angka 6
plus = Button(text="+", width=5, font=("verdana", 13, "bold"), command= lambda x="+": set_operator(x))                  # membuat tombol plus
tujuh = Button(text="7",width=5, font=("verdana",13, "bold"), command= lambda x="7": input_field(x))                   # mmebuat tombol angka 7
delapan = Button(text="8",width=5, font=("verdana",13, "bold"), command= lambda x="8": input_field(x))                 # mmebuat tombol angka 8
sembilan = Button(text="9",width=5, font=("verdana",13, "bold"), command= lambda x="9": input_field(x))                # mmebuat tombol angka 9
minus = Button(text="-",width=5, font=("verdana",13, "bold"), command= lambda x="-": set_operator(x))                   # mmebuat tombol minus
plusminus = Button(text="-/+",width=5, font=("verdana",13, "bold"), command= bilbul)             # membuat tombol -/+
nol = Button(text="0",width=5, font=("verdana",13, "bold"), command= lambda x="0": input_field(x))                     # mmebuat tombol 0
point = Button(text=".",width=5, font=("verdana",13, "bold"), command= points)                   # membuat tombol point
kali = Button(text="x",width=5, font=("verdana",13, "bold"), command= lambda x="*": set_operator(x))                    # membuat tombol kali
bagi = Button(text="/",width=5, font=("verdana",13, "bold"), command= lambda x="/": set_operator(x))                    # membuat tombol bagi
samadengan = Button(text="=",width=5, height=3, font=("verdana",13, "bold"), command=eksekusi)
 
# mengatur letak komponen kalkulator
masukan.grid(column=0, row=0, columnspan=5)
satu.grid(column=0, row=1)
dua.grid(column=1, row=1)
tiga.grid(column=2, row=1)
clear.grid(column=3, row=1, columnspan=2)
empat.grid(column=0, row=2)
lima.grid(row=2, column=1)
enam.grid(column=2, row=2)
plus.grid(row=2, column=3)
tujuh.grid(row=3, column=0)
delapan.grid(row=3, column=1)
sembilan.grid(row=3, column=2)
minus.grid(row=3, column=3)
plusminus.grid(row=4, column=0)
nol.grid(row=4, column=1)
point.grid(row=4, column=2)
kali.grid(row=4, column=3)
bagi.grid(row=2, column=4)
samadengan.grid(row=3, column=4, rowspan=2)
 
mainloop(}
