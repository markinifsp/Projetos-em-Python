from documento import documentos
from typing import List
import string

class imprepossora:

    def __init__(self):
        self.fdocumento:List[documentos] = []


    def verificaVazio(self):
        if len(self.fdocumento) == 0:
            print("A impressora está vázia")
            return True
        
        else:
            print(f"Não está vazia, tem {len(self.fdocumento)} na impressora")
            return False

    
    def addImressora (self,documento):
        self.fdocumento.append(documento)
    

    def exibirFila(self):
        if self.verificaVazio:
            for a in (self.fdocumento):
                print("====================")
                a.exibirFolha()
                print("====================")
    
    def ordemSaida(self):
        folha = self.fdocumento[0]
        print(f"O carro que vai sair agora é: ")
        folha.exibirFolha
    
    def imprimir(self):
        if self.verificaVazio:
            print("A impressora está vázia")
        else:
            folha = self.fdocumento.pop(0)
            print("A folha que está sendo impressa é: ")
            folha.exibirFolha

    
    def calcularValor(self):
        valorTotal = 0.0
        for a in (self.fdocumento):
            cor = a.cor
            fv = a.frenteVerso
            pg = a.paginas
            if cor == "Preto" and fv == True:
                valorteste = 0.25*pg
                if valorteste >10:
                    print("A impressão foi negada")
                else:
                    print(f"O doc foi aceito R${valorteste}")
                    valorTotal += 0.25 * pg
                
            elif cor == "Colorido" and fv == True:
                valorteste = 0.45*pg
                if valorteste >10:
                    print("A impressão foi negada")
                else:
                    print(f"O doc foi aceito R${valorteste}")
                    valorTotal += 0.45 * pg
            
            elif cor == "Preto" and fv ==False:
                valorteste = 0.35*pg
                if valorteste >10:
                    print("A impressão foi negada")
                else:
                    print(f"O doc foi aceito R${valorteste}")
                    valorTotal += 0.35 * pg
            
            elif cor == "Colorido" and fv == False:
                valorteste = 0.55*pg
                if valorteste >10:
                    print("A impressão foi negada")
                else:
                    valorTotal += 0.55 * pg

        
            
        print(f"O valor total da impressão é R${valorTotal}")
            



