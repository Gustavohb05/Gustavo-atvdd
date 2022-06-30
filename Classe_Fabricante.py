from Classe_Venda import *
class Fabricante():
    def __init__(self):
        self.fab = []

    def cadastrar(self):
        print('digite o código do fabricante:')
        receba = int(input('código:\n'))
        self.fab.append(Produto(

