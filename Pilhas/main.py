from carro import carros
from Estacionamento import estacionamento

Fusca = carros ("Fusca", "AEO-123","Hatch")
S10 = carros ("Corsel-2", "UYT-987","Camionete")
Diplomata = carros ("Diplomata", "JKE-740","Sedan")
Maverick = carros ("Diplomata", "JKE-740","Sedan")

vagas = estacionamento()

#vagas.verificaVazio()

#Fusca.detalhesCarros()

vagas.estacionar(Fusca)
vagas.estacionar(S10)
vagas.estacionar(Diplomata)
vagas.estacionar(Maverick)
#vagas.verificaVazio()

vagas.verificarEstacionamento()

#vagas.ordemSaida()

#vagas.verificarCarroFrente()

vagas.calcularGanhos()