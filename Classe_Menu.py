
from bancodedados import *



class Menu:
    def __init__(self):
        self.data = Data()
        while True:
            entrada = input('1-Cadastrar\n2-Listar\n3-Trocar Produto\n4-Comprar\n5-Vender\n6-Cadastrar Fabricante\n7-Sair:\n')
            print(80 * '\033[34m=', '\033[m')
            if entrada == '1':
               nome = input('digite o nome:')
               quanti = input('digite a quantidade:')
               fab = int(input('qual o codigo:'))

               self.data.cadastro_produto(nome=nome, quant=quanti, fabri=fab)
            elif entrada == '6':
                nome = input('digite seu nome: ')
                self.data.cadastro_fabricante(nome=nome)
            elif  entrada =='2':
                self.data.listar()
            elif entrada == '7':
                break
