# импортируем библиотеку с интерфейсом
# tkinter  pyqt5 pyside6

# импорт всей библиотеки
import time

#импортируем библиотеку с окнами (интерфейсом) все библиотеки: tkinter, pyqt5, pyside6
#импорт всех функций и переменных из библиотеки ! может вызвать коллизию имен!
from tkinter import *

#вызов всей библиотеки с присвоением псевдонима
# импорт всей библиотеки
import time
from threading import Thread

# pip install pyinstaller
# pyinstaller --onefile ui.py
# python -m PyInstaller --onefile ui.py

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !
# from tkinter import *

# импорт всей библиотеки с присвоением псевдонима
# import tkinter as tk


# импорт отдельной функции из модуля(из нашего файла)
# from .calc import calc_3


# импортируем библиотеку для работы с окнами(интерфейсом) все библиотеки: tkinter pyqt5 pyside6


import tkinter
import tkinter.ttk as ttk
from threading import Thread

result="something"



hours = 0
minutes = 0
seconds = 0



def start_timer():
       global hours
       hours = 0
       global minutes
       minutes = 0
       global seconds
       seconds = 0

       while minutes < 5:
       # while True:
              # seconds = seconds + 1
              seconds += 1

              if seconds > 59:
                     minutes += 1
                     seconds = 0

              if minutes > 59:
                     hours += 1
                     minutes = 0

              if hours > 23:
                     minutes = 0
                     seconds = 0
                     hours = 0
              # if minutes > 30:
              #        break

              time.sleep(0.001)
              print(f"{hours}:{minutes}:{seconds}")

def start_new_thread():
    Thread(target=start_timer).start()

# инициализация инстанса - создание объекта tkinter
root = tkinter.Tk()

#создание внешнего окна
frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на PYTHON")
root.geometry("640x480")
frm.grid()


#часы
ttk.Label(frm, text="00").grid(column=0, row=0)
# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)
# минуты
ttk.Label(frm, text="00").grid(column=2, row=0)
# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)
# секунды
ttk.Label(frm, text="00").grid(column=4, row=0)

# кнопка СТОП
Button(text="stop",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       # command=stop_timer,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
       ).grid(column=1, row=1)

# кнопка СТОП
Button(text="start",
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",
       # command=start_timer
       command=start_new_thread
       ).grid(column=3, row=1)





#   0  1  2   3  4
#1 Any : Alex : Ivan

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)



root.mainloop()


# Thread(target=autoc).start()













