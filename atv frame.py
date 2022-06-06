#importando o tkinter
from tkinter import *

#def para clicar com enter, achar o imc, e aparcer na tela o imc da pessoa
def cal():
    if pes2.get().replace('.', '', 1).isdigit() and alt2.get().replace('.', '', 1).isdigit():
        imc2 = float(pes2.get()) / (float(alt2.get()) * float(alt2.get()))
        res['text'] = f'{imc2:.2f}'

        if imc2 < 18.5:
            sa['text'] = ('Abaixo do peso')
            sa['foreground'] = 'red'
        elif 18.5 < imc2 <= 25:
            sa['text'] = ('Saudável')
            sa['foreground'] = 'black'
        elif 25 < imc2 <= 30:
            sa['text'] = ('Peso em excesso')
            sa['foreground'] = 'yellow'
        elif 30 < imc2 <= 35:
            sa['text'] = ('Obsidade Grau 1')
            sa['foreground'] = 'orange'
        elif 35 < imc2 <= 40:
            sa['text'] = ('Obsidade Grau 2')
            sa['foreground'] = 'red'
        elif imc2 >= 40:
            sa['text'] = ('Obsidade Grau 3')
            sa['foreground'] = 'red'

    else:
        res['text'] = 'digite apenas numeros'
        res['foreground'] = 'red'
        sa['text'] = ''

#criando a janela
janela  = Tk()

#clicar com o enter
janela.bind('<Return>', cal)

#definindo tamanho da tela
janela.geometry('1080x820')



#tudo que vai aparecer na tela
f1 = Frame(janela, bg='blue')
f2 = Frame(janela, bg='green')
pes = Label(f1, font='ARIAL 30', text='peso')
alt = Label(f1, font='ARIAL 30', text='altura')
pes2 = Entry(f1, font='ARIAL 30')
alt2 = Entry(f1, font='ARIAL 30')
imc = Button(f2, font='ARIAL 30', text='imc', command=cal)
res = Label(f2, font='ARIAL 30', text='resultado', bg='green')
sa = Label(f2, font='ARIAL 30', text='', bg='green')

#executar tudo que vai aparecer na tela
f1.grid(row=0, column=0)
f2.grid(row=0, column=1)
pes.grid(row=0, column=0)
pes2.grid(row=0, column=1)
alt.grid(row=1, column=0)
alt2.grid(row=1, column=1)
imc.grid(row=1, column=0)
res.grid(row=1, column=1)
sa.grid(row=1, column=2)

#executar a janela
janela.mainloop()