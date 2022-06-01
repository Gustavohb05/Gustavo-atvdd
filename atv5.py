#importando o tkinter
from tkinter import *

#def para converter e para dar erro quando digitar letras
def converte(event):
    if grau2.get().replace('.', '', 1).isdigit():
        converte2 = float(grau2.get()) * 1.8 + 32
        res['text'] = f'{converte2:.2f}'
    else:
        res['text'] = 'digite apenas numeros'
        res['foreground'] = 'red'

#chamando a janela
janela  = Tk()

#definindo o tamanho da janela
janela.geometry('1980x820')

#função para clicar com o botão enter em vez de clicar com o mouse
janela.bind('<Return>', converte)

#criando as coisas que vai aparcer na tela
grau = Label(janela, text='c°:', font='ARIAL 50')
grau2 = Entry(janela, font='ARIAL 50')
res = Label(janela, text='resultado', font='ARIAL 50')
bot = Button(janela, font='ARIAL 30', text='Converte °F', command=converte)
res = Label(janela, font='Arial 30', text='')

#para executar tudo o que vai aparecer na tela
grau.grid(row=0, column=0)
grau2.grid(row=0, column=1)
res.grid(row=1, column=1)
bot.grid(row=1, column=0)
res.grid(row=1, column=1)



#para executar a janela
janela.mainloop()
