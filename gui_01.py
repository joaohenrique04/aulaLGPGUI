## TESTE DE GUI COM JANELA E BOTAO

from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text="você clicou ;)")

window = Tk()
window.title("Bem-vindo, NERD B)")
window.geometry("350x200")

# lbl = Label(window, text="Olá")
# lbl.pack()

lbl=Label(window, text="Isso é um Label Widget", fg="red",
          font=("Helvetica", 16))
lbl.place(x=60, y=50)

txtfld=Entry(window, text="Isso é uma caixa de entrada po", bd=2)
txtfld.place(x=80, y=150)

btn = Button(window, text="me clica por favor", command=clicked)
btn.pack()

data = ("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=170)

window.mainloop()