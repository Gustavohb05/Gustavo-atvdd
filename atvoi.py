from  tkinter import *

#def condicional

def imprimir() :
    if entry.get().isnumeric() and entry2.get().isnumeric():
        Print['text'] = float(entry.get()) + float(entry2.get())
        Print['foreground'] = 'black'
    else:
        Print['text'] = 'valor inválido'
        Print['foreground'] = 'red'

#abrir janela

janela = Tk()
janela.geometry('1280x720')
janela.config(bg='blue')


#widgets

Print = Label(janela, text='Calculadora', bg='blue', font='Arial 50 bold')
text = Label(janela, text='Valor 1', font='Arial 50 bold', bg='blue')
entry = Entry(janela, font='Arial 40')
text2 = Label(janela, text='Valor 2', font='Arial 50 bold', bg='blue')
entry2 = Entry(janela, font='Arial 40')
botao2 = Button(janela, text='somar', font='Arial 50 bold', command=imprimir)
botao = Button(janela, text='Sair', font='Arial 30', command=quit)



#organizar

Print.pack()
text.pack()
entry.pack()
text2.pack()
entry2.pack()
botao2.pack()
botao.pack(side=BOTTOM)




#executar

janela.mainloop()