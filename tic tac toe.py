import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

linhas,colunas = [0,1,2],[0,1,2]
casas = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def valor(coluna,linha):
    var 
    if 
    casas[coluna][linha] = "X"
    botao()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

#for coluna in colunas:
#    for linha in linhas:
#        ttk.Button(frm, text=casas[linha][coluna], command=lambda: valor(linha,coluna) ).grid(column=coluna, row=linha)


def botao():
    ttk.Button(frm, text=casas[0][0], command=lambda: valor(0,0)).grid(column=0, row=1)
    ttk.Button(frm, text=casas[0][1], command=lambda: valor(0,1)).grid(column=0, row=2)
    ttk.Button(frm, text=casas[0][2], command=lambda: valor(0,2)).grid(column=0, row=3)
    ttk.Button(frm, text=casas[1][0], command=lambda: valor(1,0)).grid(column=1, row=1)
    ttk.Button(frm, text=casas[1][1], command=lambda: valor(1,1)).grid(column=1, row=2)
    ttk.Button(frm, text=casas[1][2], command=lambda: valor(1,2)).grid(column=1, row=3)
    ttk.Button(frm, text=casas[2][0], command=lambda: valor(2,0)).grid(column=2, row=1)
    ttk.Button(frm, text=casas[2][1], command=lambda: valor(2,1)).grid(column=2, row=2)
    ttk.Button(frm, text=casas[2][2], command=lambda: valor(2,2)).grid(column=2, row=3)

botao()

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)

root.mainloop()

print(casas)