print("   Valor    | pensão | adicionais ")
print("[1]2500,00  - Não    - Não")
print("[2]4900,00  - Sim    - Não")
print("[3]2500,00  - Não    - Sim")



pacote = int(input("Qual pacote de viagem você quer?"))


def verificaPacote(pacote):
    if pacote == 1:
        valor = 2500
        
    
    elif pacote == 2:
        valor = 4900
       
    
    elif pacote == 3:
        valor = 2500
        
    return valor
    
valor = verificaPacote(pacote)

def descPacote(pacote):
    if pacote == 1:
        desc ="Você escoolhe o pacote 1 sem pensão e sem adiconal com o valor de R$2500"
    elif pacote == 2:
         desc ="Você escoolhe o pacote 2 com pensão e sem adiconal com o valor de R$4900"
    elif pacote == 3:
        desc ="Você escoolhe o pacote 3 sem pensão e com adiconal com o valor de R$2500"
    return desc

desc = descPacote(pacote)

pagamento = int(input("Qual a forma de pagamento?\n[1]À vista\n[2]Parcelar"))

def pagas(pagamento):
    if pagamento == 2:
        parcela = int(input("Em quantas vezes você deseja parcelar?"))
        if parcela < 12:
            print(f"O valor final ficou de R${valor} com parcelas de R${valor / parcela}")

        elif parcela > 12 and parcela<=24:
            print(f"O valor final ficou de R${valor * (1 + 0.3 / 100) ** parcela:.2f} com parcelas de R${(valor * (1 + 0.3 / 100) ** parcela) / parcela:.2f}")
        
        elif parcela >24 and parcela<=36:
            print(f"O valor final ficou de R${valor * (1 + 0.35/ 100) ** parcela:.2f} com parcelas de R${(valor * (1 + 0.5 / 100) ** parcela) / parcela:.2f}")
    else:
        print(f"O valor final ficou de R${valor}")

verificaPacote(pacote)
pagas(pagamento)