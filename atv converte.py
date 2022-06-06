#importando o tkinter
from tkinter import *

#def para converter e para dar erro quando digitar letras
def converte():
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
janela.bind('<Return>', lambda event: converte())

#criando as coisas que vai aparcer na tela
f1 = Frame(janela, bg='green')
f2 = Frame(janela, bg='blue')
grau = Label(f1, text='c°:', font='ARIAL 50')
grau2 = Entry(f1, font='ARIAL 50')
res = Label(f2, text='resultado', font='ARIAL 50')
bot = Button(f2, font='ARIAL 30', text='Converte °F', command=converte)


#para executar tudo o que vai aparecer na tela
f1.grid(row=0, column=0)
f2.grid(row=0, column=1)
grau.grid(row=0, column=0)
grau2.grid(row=1, column=0)
res.grid(row=1, column=2)
bot.grid(row=1, column=1)




#para executar a janela
janela.mainloop()
