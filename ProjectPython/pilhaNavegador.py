from navegador import Navegador
from typing import List

class pilhaNavegador:
    #Criando uma lista de navegador tipando ele para ser apenas uma lista do bjeto navegador
    def __init__(self):
        self.navegador:list[Navegador] = []

    def verificarVazias(self):
        #o len pega a quantidade de itens presenetes na list
        qtdeNavegador = len(self.navegador)

        #se len for 0 o historico de navegação vai estar vazias
        if qtdeNavegador == 0:
            print("Seu historico está vazio")
            return True
        
        else:
            print(f"Você tem {len(self.navegador)} abas abertas")
            return False
    
    def AcessarSite(self, navegador: Navegador):
        #Adicionando o objeto a pilha/lista
        self.navegador.append(navegador)

    def tamanho(self):
        #Pega o tamanho com o len e retorna a quantidade
        print(f"Você tem {len(self.navegador)} abas abertas")
    
    def apagarHistorico(self):
        #remove um item do historico
        if self.verificarVazias():
            print("O seu historico já está vazio!!")
        
        else:
            navegador = self.navegador.pop()
            print(f"A site {Navegador.nome} foi removido do historico")

     
    def ultimoAcesso(self):
        # Exibe o último site acessado
        if self.verificarVazias():  # Chama o método com parênteses
            print("Não há pesquisas no histórico.")
        else:
            navAcessado = self.navegador[-1]  # Pega o último site da pilha
            print("O último site acessado foi:")
            navAcessado.exibirSite()


    def exibirHistorico(self):
        print("Os sites acessados foram:")
        for navegador in reversed(self.navegador):
            navegador.exibirSite()
    
