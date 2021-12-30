from BMI import BMI
from tkinter import *
import tkinter as tk

from tkinter import *

ws = Tk()
ws.title("BMI Calculator")
ws.geometry('500x500')
ws['bg'] = '#ffbf00'


def get_info():
    pweight = player_weight.get() if player_weight.get().isdigit() is True else print('Use an Int!')
    pheight = player_height.get()
    pname = player_name.get()
    v = Label(ws, text=f'Your weight is {pweight} lbs, Your height is {pheight} and Your name is {pname} ', pady=20,
              bg='#ffbf00').pack()
    person1 = BMI(int(pweight), pheight, pname)
    print('Height', person1.get_height())
    print('BMI', person1.get_bmi())
    b = Label(ws, text=f'Your BMI is {person1.get_bmi()} and {person1.get_criteria()}', pady=20,
              bg='#ffbf00').pack()


def clear_field():
    player_weight.delete(0, END)
    player_height.delete(0, END)
    player_name.delete(0, END)


def close_window():
    ws.destroy()


weight_label = Label(ws, text='Weight', font=('calibre', 10, 'bold')).pack()
player_weight = Entry(ws)
player_weight.pack(pady=10)

height_label = Label(ws, text='Height', font=('calibre', 10, 'bold')).pack()
player_height = Entry(ws, text='height', font=('calibre', 10, 'bold'))
player_height.pack(pady=10)

name_label = Label(ws, text='Name', font=('calibre', 10, 'bold')).pack()
player_name = Entry(ws, text='name', font=('calibre', 10, 'bold'))
player_name.pack(pady=10)

Button(
    ws,
    text="Get Results",
    padx=10,
    pady=5,
    command=get_info
).pack(pady=10)

Button(
    ws,
    text="Clear",
    padx=10,
    pady=5,
    command=clear_field
).pack(pady=10)

Button(
    ws,
    text="Exit",
    padx=10,
    pady=5,
    command=close_window
).pack(pady=10)
ws.mainloop()
