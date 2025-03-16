import string

lanches = {
    'lanche1':{
        'Nome': '[1] BigMac',
        'valor': 10},
    
    'lanche2':{
        'Nome': '[2] BigTasty',
        'valor': 15},
    
    'lanche3':{
        'Nome': '[3] McMelt',
        'valor': 25}
}

sobremesas = {
    'sobremesa1':{
        'Nome': '[1] MilkShake',
        'valor': 10},
    
    'sobremesa2':{
        'Nome': '[2] Brownie',
        'valor': 15},
    
    'sobresa3':{
        'Nome': '[3] McFlury',
        'valor': 25}
}

cupom = 'ABC5F'
cupom = 'WER2A'
cupom = 'BNM9R'
cupom = 'QDG8X'



categoria = int(input('Seja bem vindo ao McDonalds você deseja ver a categoria lanches ou sobremesas? ([1]Lanches - [2]Sobremesas)\n'))

def Cardapio(categoria):
    if categoria == 1:
        for lanche in lanches.values():
            print(lanche)
        pedido = int(input("Qual opção você deseja? "))
         
        if pedido ==1:
            print('Você escolheu o BigMac seu pedido deu R$10')
            valor = 10
        
        if pedido ==2:
            print('Você escolheu o BigTasty seu pedido deu R$15')
            valor = 15
        
        if pedido ==3:
            print('Você escolheu o McMelt seu pedido deu R$20')
            valor= 20
            
    elif categoria == 2:
        for sobre in sobremesas.values():
            print(sobre)

        pedido = int(input("Qual opção você deseja? "))
         
        if pedido ==1:
            print('Você escolheu o MilkShake seu pedido deu R$10')
            valor = 10
        
        if pedido ==2:
            print('Você escolheu o Brownie seu pedido deu R$15')
            valor = 15
        
        if pedido ==3:
            print('Você escolheu o McFlury seu pedido deu R$20')
            valor= 20
    return valor


valor = Cardapio(categoria)

cupom = int(input('Deseja colocar um cupom? [1]Sim - [2]Não'))

if cupom == 1:
    cp = str(input('Digite um cupom valido'))
    if cp == 'ABC5F':
        resultado = valor-valor*0.05
        print(f'Seu pedido deu R${resultado}')
    
    elif cp == 'WER2A':
        resultado = valor-valor*0.08
        print(f'Seu pedido deu R${resultado}')

    elif cp == 'BNM9R':
        resultado = valor-valor*0.10
        print(f'Seu pedido deu R${resultado}')
    
    elif cp == 'QDG8X':
        resultado = valor-valor*0.18
        print(f'Seu pedido deu R${resultado}')

else:
    print(f'Cupom inválido\nSeu pedido deu R${valor}')



