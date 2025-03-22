class Navegador:
    def __init__(self, link: str, nome:str):
        self.link = link
        self.nome = nome

    def exibirSite(self):
        print(f'Site acessado: {self.link} Nome do site: {self.nome}')
