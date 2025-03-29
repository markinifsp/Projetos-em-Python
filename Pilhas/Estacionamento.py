from carro import carros
from typing import List
import string

class estacionamento:

    def __init__(self):
            self.vagas:List[carros] = []


    #VERIFICA SE O ESTACIONAMENTO ESTÁ VAZIO
    def verificaVazio(self):
        if len(self.vagas) == 0:
            print("O estacionamento está vázio") 
            return True
        
        else:
            print(f"Não está vazio tem, {len(self.vagas)} carros no estacionamento")
            return False
    
    #ADICONA O CARRO NA FILA / ESTACIONAMENTO
    def estacionar(self,carro):
        self.vagas.append(carro)

    #VERIFICA SE O ESTACIONAMENTO ESTÁ VAZIO E RETORNA QUAIS ESTÃO ESTACIONADOS
    def verificarEstacionamento(self):
        print(f"Tem {len(self.vagas)} carros no estacionameto")
        for a in (self.vagas):
            print("====================")
            a.detalhesCarros()
            print("====================")

    #EXIBE O CARRO QUE VAI SARI DO ESTACIONAMENTO
    def ordemSaida(self):
        car = self.vagas[0]
        print(f"O carro que vai sair do estacionamento agora é:")
        car.detalhesCarros()
    
    #VERIFICA O CARRO QUE ESTA NA FRENTE DA FILA
    def verificarCarroFrente(self):
        if self.verificaVazio():
            print("O estacionamento está vazio!!")
        
        else:
            carroFrente = self.vagas[0]
            print("O carro que está na frente da fila é o: ")
            carroFrente.detalhesCarros()
    
    #CALCULAR O VALOR GERAL DO ESTACIONAMENTO
    def calcularGanhos(self):
        valorGanho = 0.0
        for a in (self.vagas):
            tipo = a.tipo
            if tipo == "Hatch":
                valorGanho+=5
            
            elif tipo =="Sedan":
                valorGanho+=8
            
            elif tipo =="Camionete":
                valorGanho+=12
        print(f"o lucro ganho no estacionamento é de R${valorGanho}")



