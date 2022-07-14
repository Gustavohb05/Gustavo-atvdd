import posiciona
from tkinter import *
from bancodedados import *
from tkinter import ttk






data = Data()



janela = Tk()

janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))

janela.geometry('600x600')

bg = PhotoImage(file='1.png')

f1 = Frame(janela)
label1 = Label(f1, image=bg)

label1.grid()

bt = Button(f1, font='ARIAL 25', text='SAIR', bg='#ff19cf', fg='white', bd=0, command=quit, activebackground='#ff19cf')
bt.place(width=262, height=87, x=450, y=651)

bt2 = Button(f1, font='ARIAL 25', text='CADASTRAR', bg='#ff19cf', fg='white', bd=0,
             command=lambda: [f1.forget(), f2.pack()], activebackground='#ff19cf')
bt2.place(width=247, height=92, x=1124, y=647)

f2 = Frame(janela)
bg2 = PhotoImage(file='2.png')

label2 = Label(f2, image=bg2)

bt3 = Button(f2, font='ARIAL 25', text='Fabricante', bg='#ff19cf', fg='white', bd=0,
             command=lambda: [f1.forget(), f2.forget(), f3.pack(), f4.forget(), f5.forget()], activebackground='#ff19cf')
bt3.place(width=317, height=123, x=738, y=209)

bt4 = Button(f2, font='ARIAL 25', text='Produtos', bg='#ff19cf', fg='white', bd=0,
             command=lambda: [f1.forget(), f2.forget(), f3.forget(), f4.pack(), f5.forget()], activebackground='#ff19cf')
bt4.place(width=329, height=125, x=729, y=491)

bt5 = Button(f2, font='ARIAL 25', text='Listar', bg='#ff19cf', fg='white', bd=0,
             command=lambda: [f1.forget(), f2.forget(), f3.forget(), f4.forget(), f5.pack(), data.listar(tabela)],
             activebackground='#ff19cf')
bt5.place(width=328, height=123, x=729, y=773)

b = PhotoImage(file= 'saida (1).png')

b1 = Button(f2, image=b, bg='black', activebackground='black', bd=0, command=lambda: [f1.pack(), f2.forget(), f3.forget(), f4.forget(), f5.forget()])
b1.place(width=68, height=67, x=44, y=136)

f3 = Frame(janela)

bg3 = PhotoImage(file='3.png')

label3 = Label(f3, image=bg3)

e1 = Entry(f3, bg='white', foreground='black', font='ARIAL 30', bd=0)
e1.place(width=758, height=54, x=550, y=482)

bt5 = Button(f3, font='ARIAL 25', text='Cadastrar', bg='#ff19cf', fg='white', bd=0, command=lambda: data.cadastro_fabricante(e1.get()))
bt5.place(width=261, height=91, x=803, y=730)

bt6 = Button(f3, image=b, bg='black', activebackground='black', bd=0, command=lambda: [f1.forget(), f2.pack(), f3.forget(), f4.forget(), f5.forget()])
bt6.place(width=68, height=68, x=32, y=25)

f4 = Frame(janela)

bg4 = PhotoImage(file='4.png')

label4 = Label(f4, image=bg4)

e2 = Entry(f4, bg='white', foreground='black', font='ARIAL 30', bd=0)
e2.place(width=765, height=54, x=535, y=402)

e3 = Entry(f4, bg='white', foreground='black', font='ARIAL 30', bd=0)
e3.place(width=773, height=43, x=532, y=618)

e4 = Entry(f4, bg='white', foreground='black', font='ARIAL 30', bd=0)
e4.place(width=777, height=49, x=535, y=829)

bt7 = Button(f4, image=b, bg='black', activebackground='black', bd=0, command=lambda: [f1.forget(), f2.pack(), f3.forget(), f4.forget(), f5.forget()])
bt7.place(width=68, height=66, x=26, y=17)

bt8 = Button(f4, text='Cadastrar', font='ARIAL 25', bg='#ff19cf', activebackground='black', bd=0, command= lambda: data.cadastro_produto(e2.get(), e3.get(), e4.get()))
bt8.place(width=233, height=73, x=1613, y=878)

f5 = Frame(janela)

bg5 = PhotoImage(file='PYDRUTOS.png')

label5 = Label(f5, image=bg5)


bt9 = Button(f5, text='Listar', font='ARIAL 25', bg='#ff19cf', activebackground='black', bd=0)

bt10 = Button(f5, image=b, bg='black', activebackground='black', bd=0, command=lambda: [f1.forget(), f2.pack(), f3.forget(), f4.forget(), f5.forget()])
bt10.place(width=68, height=64, x=38, y=25)

tabela = ttk.Treeview(f5, columns=["cod", "nome", "quant", "fabri"], selectmode='browse',
show='headings')
tabela.place(width=1379, height=837, x=259, y=175)

rolar = ttk.Scrollbar(f5, orient='vertical', command=tabela.yview())
tabela.config(xscrollcommand=rolar.set)
tabela.column("cod", width=10)
tabela.column("nome", width=150)
tabela.column("quant", width=30)
tabela.column("fabri", width=150)
tabela.heading("cod", text='cod')
tabela.heading("nome", text='Nome do produto')
tabela.heading("quant", text='Quantidade')
tabela.heading("fabri", text='Fabricante')



f1.pack()
f2.pack()
f3.pack()
f5.pack()

label2.grid()

label3.grid()
f4.pack()
f4.pack()
label4.grid()
label5.grid()




janela.mainloop()
