valorInvestimento = float(input('Quanto deseja investir? '))
meses = float(input('Quantos meses deseja investir? [1]24, [2]60, [3]120 '))
risco = float(input('Você deseja um investimento de [1]baixo, [2]médio ou [3]alto risco? Digite o numero da operação'))

def calcularInv(valorInvestimento, meses, risco):
    #Baixo risco
    if risco == 1 and meses ==1:
        meses=24
        print(f'O investimento de R${valorInvestimento} rendendo a 0,5 ao mes no periodo de {meses} meses te da o lucro de R${meses*0.5*valorInvestimento}')
    
    elif risco == 1 and meses ==2:
        meses = 60
        print(f'O investimento de R${valorInvestimento} rendendo a 0,8 ao mes no periodo de {meses} meses te da o lucro de R${meses*0.8*valorInvestimento}')
    
    elif risco == 1 and meses ==3:
        meses = 120
        print(f'O investimento de R${valorInvestimento} rendendo a 1,2 ao mes no periodo de {meses} meses te da o lucro de R${meses*1.2*valorInvestimento}')


    #Risco médio
    elif risco == 2 and meses ==1:
        meses = 24
        print(f'O investimento de R${valorInvestimento} rendendo a 1.1 ao mes no periodo de {meses} meses te da o lucro de R${meses*1.1*valorInvestimento}')
    
    elif risco == 2 and meses ==2:
        meses = 60
        print(f'O investimento de R${valorInvestimento} rendendo a 1.5 ao mes no periodo de {meses} meses te da o lucro de R${meses*1.5*valorInvestimento}')
    
    elif risco == 2 and meses ==3:
        meses = 120
        print(f'O investimento de R${valorInvestimento} rendendo a 1.9 ao mes no periodo de {meses} meses te da o lucro de R${meses*1.9*valorInvestimento}')


    #Risco alto
    elif risco == 3 and meses ==1:
        meses = 24
        print(f'O investimento de R${valorInvestimento} rendendo a 2.1 ao mes no periodo de {meses} meses te da o lucro de R${meses*2.1*valorInvestimento}')
    
    elif risco == 3 and meses ==2:
        meses = 60
        print(f'O investimento de R${valorInvestimento} rendendo a 2.8 ao mes no periodo de {meses} meses te da o lucro de R${meses*2.8*valorInvestimento}')
    
    elif risco == 3 and meses ==3:
        meses = 120
        print(f'O investimento de R${valorInvestimento} rendendo a 3.9 ao mes no periodo de {meses} meses te da o lucro de R${meses*3.9*valorInvestimento}')


calcularInv(valorInvestimento, meses, risco)