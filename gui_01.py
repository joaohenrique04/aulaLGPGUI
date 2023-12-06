## TESTE DE GUI COM JANELA E BOTAO

from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text="você clicou ;)")

window = Tk()
window.title("Bem-vindo, NERD B)")
window.geometry("400x400")

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

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

window.mainloop()