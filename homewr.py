from tkinter import *


def print_to_console(phrase="<<Все работает хорошо>>"):
    print(phrase)

root = Tk()
root.title("Большая кнопка")
root.geometry("640x480")

btn = Button(text="Это кнопка",
             height="10",
             width="60",
             fg="blue",
             command=print_to_console,
             )
btn.pack()

root.mainloop()
