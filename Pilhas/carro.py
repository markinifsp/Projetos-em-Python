class carros:
    def __init__(self,modelo,placa,tipo):
        self.modelo = modelo
        self.placa = placa
        self.tipo = tipo
    
    #Exibir detalhes
    def detalhesCarros(self):
        print(f"Modelo: {self.modelo}\nPlaca: {self.placa}\nTipo: {self.tipo}")