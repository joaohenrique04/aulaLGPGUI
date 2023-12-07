## TESTE DE GUI COM JANELA E BOTAO

from tkinter import *
from tkinter.ttk import Combobox

qtd_clicks = 0

def clicked():
    lbl.configure(text="você clicou ;)")

def botaoClicado(par):
    global qtd_clicks 
    qtd_clicks += 1
    lbl.configure(text="você clicou " + str(qtd_clicks) + " vezes no botão")    

window = Tk()
window.title("Bem-vindo, NERD B)")
window.geometry("400x400")

# lbl = Label(window, text="Olá")
# lbl.pack()

lbl=Label(window, text="Isso é um Label Widget", fg="red",
          font=("Helvetica", 16))
lbl.place(x=60, y=10)

txtfld=Entry(window, text="Isso é uma caixa de entrada po", bd=2)
txtfld.place(x=80, y=150)

## btn = Button(window, text="me clica por favor", command=clicked)
btn = Button(window, text="me clica por favor")
btn.place(x=200, y=350)
btn.bind("<Button-1>", botaoClicado)

data = ("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=170)

lb=Listbox(window, height=4, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Programação", variable=v0, value=1)
r2=Radiobutton(window, text="Infra", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=200, y=50)

v1=IntVar()
v2=IntVar()
C1 = Checkbutton(window, text="Futebol", variable=v1)
C2 = Checkbutton(window, text="Tenis", variable=v1)
C1.place(x=100, y=100)
C2.place(x=200, y=100)

window.mainloop()