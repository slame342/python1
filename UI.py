# импортируем библиотеку с интерфейсом
# tkinter  pyqt5 pyside6

# импорт всей библиотеки
import time

#импортируем библиотеку с окнами (интерфейсом) все библиотеки: tkinter, pyqt5, pyside6
#импорт всех функций и переменных из библиотеки ! может вызвать коллизию имен!
# from tkinter import *

#вызов всей библиотеки с присвоением псевдонима
# import tkinter as tk

#импорт отдельной функции из модуля (из нашего файла)
# from .calc import calc_3

#импортируем библиотеку с окнами (интерфейсом) все библиотеки: tkinter, pyqt5, pyside6
# from tkinter import *
# from tkinter import ttk

# import tkinter
# import tkinter.ttk as ttk
#
#
# root = tkinter.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
from tkinter import ttk

#инициализация инстанса - создание объекта tkinter
root = Tk()

# создание внешнего окна
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="1 ").grid(column=0, row=0)
ttk.Label(frm, text="2").grid(column=1, row=0)
ttk.Label(frm, text="3").grid(column=2, row=0)
ttk.Label(frm, text="Any").grid(column=0, row=1)
ttk.Label(frm, text="Alex").grid(column=1, row=1)
ttk.Label(frm, text="Ivan").grid(column=2, row=1)


#  1    2    3
# Any Alex Ivan


# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()