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
            sa['foreground'] = 'green'
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
janela.geometry('1980x820')

janela.bind('<Return>', lambda event: cal())



#tudo que vai aparecer na tela
pes = Label(janela, font='ARIAL 50', text='peso')
alt = Label(janela, font='ARIAL 50', text='altura')
pes2 = Entry(janela, font='ARIAL 50')
alt2 = Entry(janela, font='ARIAL 50')
imc = Button(janela, font='ARIAL 50', text='imc', command=cal)
res = Label(janela, font='ARIAL 50', text='resultado')
sa = Label(janela, font='ARIAL 50', text='')

#executar tudo que vai aparecer na tela
pes.grid()
pes2.grid()
alt.grid()
alt2.grid()
imc.grid()
res.grid()
sa.grid()

#executar a janela
janela.mainloop()
