dias = int(input("Quantos dias você deseja alugar o carro?"))
km = float(input("Qunatos km você deseja rodar?"))
diasValor = 0.0
kmValor = 0.0

def valorDias(dias):
    if dias <=3:
        diasValor = 109.90

    elif dias > 3 and dias <= 7:
        diasValor = 99.90

    elif dias > 7 and dias <= 15:
        diasValor = 89.90

    else:
        diasValor = 69.90
    return diasValor

diasValor = valorDias(dias)


def valorKm(km):
    if km <= 500:
        kmValor=0.85
    
    elif km >500 and km <=900:
        kmValor = 0.75
    
    elif km >900 and km <=2000:
        kmValor = 0.69

    else:
        kmValor =0.65
    return kmValor

kmValor = valorKm(km)

print(f"O valor total ficou R${kmValor*km + diasValor}")