class documentos:
    def __init__(self,paginas,cor,frenteVerso:bool):
        self.paginas=paginas
        self.cor=cor
        self.frenteVerso=frenteVerso
    
    def exibirFolha(self):
        print(f"A cor da folha é: {self.cor}\nA quantidade de paginas são: {self.paginas} \nA impressão é frente e verso: {'Sim' if self.frenteVerso else 'Não'}")