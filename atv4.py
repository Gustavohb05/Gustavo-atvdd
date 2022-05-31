from  tkinter import *



def aumenta():
   if texto['text'] < 10:
       texto['text'] +=1
   else:
       pass


def diminui():
    if texto['text'] > -10:
        texto['text'] -=1
    else:
        pass



janela = Tk()
janela.geometry('1980x720')

janela.grid_rowconfigure(0, weight=1)
janela.bind('a', lambda event: diminui())
janela.bind('d', lambda event: aumenta())

for linha in range (3):
    janela.grid_columnconfigure(linha, weight=1)

menos = Button(janela, text='-', font='Arial 50', bg='green', command=diminui)
mais = Button(janela, text='+', font='Arial 50', bg='green', command=aumenta)
texto = Label(janela, text=0, font='Arial 50')

menos.grid(row=0, column=0, sticky=NSEW)
texto.grid(row=0, column=1, sticky=NSEW)
mais.grid(row=0, column=2, sticky=NSEW)

janela.mainloop()