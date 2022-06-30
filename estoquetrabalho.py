from Produtotrabalho import *

class Estoque:
    def __init__(self):
        self.puxar = []
        self.puxar.append(Produto(1, 'Lapis', 'aa', 0))


    def salvar_produtos(self):
        entrada_cod = int(input('Informe o codigo:\n'))
        entrada_desc = input('Informe a descricao:\n')
        entrada_fab = input('Informe o fabricante:\n')
        entrada_quant = int(input('Informe a quantidade:\n'))
        self.puxar.append(Produto(cod=entrada_cod, desc=entrada_desc, fab=entrada_fab, quant=entrada_quant))
        print('Produto salvo')

    def listar_produtos(self):
        for i in range(len(self.puxar)):
            print('Cod:', self.puxar[i].cod, 'Descrição:', self.puxar[i].desc, 'Fabricante:', self.puxar[i].fab, 'Quantidade',
                  self.puxar[i].quant)

    def trocar_produto(self):
        coloca = input('Informe o codigo do produto:\n')
        for i in range(len(self.puxar)):
            if coloca == self.puxar[i].cod:
                self.puxar[i].desc = input('Digite a descrição nova:\n')

