import mysql.connector as mys
from Classe_Fabricante import *
from Estoquetrabalho import *


class Data:
    def __init__(self):
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Banco_Senac')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant, fabri):
        self.cursor.execute('select cod from fabricante')
        veri = self.cursor.fetchall()
        for cod in veri:
            if int(fabri) == cod[0]:
                produto = Produto(nome, fabri, quant)
                print('Cadastrado Com Sucesso')
                self.cursor.execute(f'insert into Produtos (nome, quant, cod_fabricante) values ("{produto.nome}", {produto.quant}, {produto.fabri})')
                self.database.commit()

    def cadastro_fabricante(self, nome):
        fabricante = Salvar_Fabricante(nome)
        print('Cadastrado Com Sucesso')
        self.cursor.execute(f'insert into fabricante (nome) values ("{fabricante.nome}")')
        self.database.commit()

    def listar(self):
        self.cursor.execute('select Produtos.cod, Produtos.nome,Produtos.quant, Fabricante.nome from Produtos, Fabricante where Fabricante.cod = Produtos.cod_fabricante')
        Produtos = self.cursor.fetchall()
        for prod in Produtos:
            print(70 * '\033[34m=', '\033[m')
            print(f'codigo: {prod[0]}'
              f'\nproduto: {prod[1]}'
              f'\nquantidade: {prod[2]}'
              f'\nfabricante: {prod[3]}')

    def altera_produtos(self, cod, mudar, valor):
        try:
            self.cursor.execute(f'update Produtos set {mudar} = "{valor}" where id = {cod}')
            self.database.commit()
        except:
            print('codigo não encontrado')










