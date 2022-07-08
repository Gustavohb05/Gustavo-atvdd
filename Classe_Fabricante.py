from Classe_Venda import *


class Salvar_Fabricante():
   def __init__(self, nome):
        self.nome = nome






class Fabricante():
    def __init__(self):
        self.fab = []

    def cadastrar(self):
        receba = int(input('código:\n'))
        receba_nome = str(input(' nome:\n'))
        self.fab.append(Salvar_Fabricante(cod=receba, nome=receba_nome))

