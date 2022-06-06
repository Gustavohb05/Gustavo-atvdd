from tkinter import *



def sus(car):
    if car == '=':
        try:
            vivo['text'] = str(eval(vivo["text"]))
        except ZeroDivisionError:
            vivo['text'] = 'não há como realizar essa conta'
            vivo['foreground'] = 'red'
        except SyntaxError:
            vivo['text'] = 'não há como realizar essa conta'
            vivo['foreground'] = 'red'
    elif car == 'CE':
        vivo['text'] = ''
    elif car == 'del':
        vivo['text'] = vivo['text'][:-1]
    else:
        if vivo['text'] == 'não há como realizar essa conta':
           vivo['text'] = ''
           vivo['text'] += car
           vivo['foreground'] = '#10a4e3'
        else:
           vivo['text'] += car
           vivo['foreground'] = '#10a4e3'

janela = Tk()


janela.geometry('1200x500')

janela.bind('0', lambda event:sus(car='0'))
janela.bind('1', lambda event:sus(car='1'))
janela.bind('2', lambda event:sus(car='2'))
janela.bind('3', lambda event:sus(car='3'))
janela.bind('4', lambda event:sus(car='4'))
janela.bind('5', lambda event:sus(car='5'))
janela.bind('6', lambda event:sus(car='6'))
janela.bind('7', lambda event:sus(car='7'))
janela.bind('8', lambda event:sus(car='8'))
janela.bind('9', lambda event:sus(car='9'))
janela.bind('<BackSpace>', lambda event:sus(car='del'))
janela.bind('<Return>', lambda event:sus(car='='))
janela.bind('<Escape>', lambda event:sus(car='CE'))
janela.bind('+', lambda event:sus(car='+'))
janela.bind('/', lambda event:sus(car='/'))
janela.bind('*', lambda event:sus(car='*'))
janela.bind('-', lambda event:sus(car='-'))

for linha in range (4):
    janela.grid_columnconfigure(linha, weight=1)

b1 = Button(janela, font='ARIAL 30', text='0', command= lambda : sus(car='0'))
b2 = Button(janela, font='ARIAL 30', text='1',command= lambda : sus(car='1'))
b3 = Button(janela, font='ARIAL 30', text='2', command= lambda : sus(car='2'))
b4 = Button(janela, font='ARIAL 30', text='3', command= lambda : sus(car='3'))
b5 = Button(janela, font='ARIAL 30', text='4', command= lambda : sus(car='4'))
b6 = Button(janela, font='ARIAL 30', text='5', command= lambda : sus(car='5'))
b7 = Button(janela, font='ARIAL 30', text='6', command= lambda : sus(car='6'))
b8 = Button(janela, font='ARIAL 30', text='7', command= lambda : sus(car='7'))
b9 = Button(janela, font='ARIAL 30', text='8', command= lambda : sus(car='8'))
b10 = Button(janela, font='ARIAL 30', text='9', command= lambda : sus(car='9'))
vivo = Label(janela, font='ARIAL 30', foreground='#10a4e3')
claro = Label(janela, font='ARIAL 30', text='')
mais = Button(janela, font='ARIAL 35', text='+', command= lambda : sus(car='+'))
menos = Button(janela, font='ARIAL 35', text='-', command= lambda : sus(car='-'))
dividir = Button(janela, font='ARIAL 35', text='/', command= lambda : sus(car='/'))
mult = Button(janela, font='ARIAL 35', text='x', command= lambda : sus(car='*'))
b25 = Button(janela, font='ARIAL 30', text='CE', command= lambda : sus(car='CE'))
b20 = Button(janela, font='ARIAL 30', text='=', command= lambda : sus(car='='))
b30 = Button(janela, font='ARIAL 30', text='del', command= lambda : sus(car='del'))


vivo.grid(columnspan=4, column=0)
b1.grid(row=1, column=0, sticky=NSEW)
b2.grid(row=1, column=1, sticky=NSEW)
b3.grid(row=1, column=2, sticky=NSEW)
b4.grid(row=2, column=0, sticky=NSEW)
b5.grid(row=2, column=1, sticky=NSEW)
b6.grid(row=2, column=2, sticky=NSEW)
b7.grid(row=3, column=0, sticky=NSEW)
b8.grid(row=3, column=1, sticky=NSEW)
b9.grid(row=3, column=2, sticky=NSEW)
b10.grid(row=4, column=1, sticky=NSEW)
mais.grid(row=1, column=3, sticky=NSEW)
menos.grid(row=2, column=3, sticky=NSEW)
dividir.grid(row=3, column=3, sticky=NSEW)
mult.grid(row=4, column=3, sticky=NSEW)
claro.grid(row=5, column=1, sticky=NSEW)
b25.grid(row=4, column=0, sticky=NSEW)
b20.grid(row=4, column=2, sticky=NSEW)
b30.grid(row=5, column=0, sticky=NSEW)



janela.mainloop()