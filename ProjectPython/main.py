from navegador import Navegador
from pilhaNavegador import pilhaNavegador


Youtube = Navegador("youtube.com","Youtube")
Instagram = Navegador("instagram.com","Instagram")
GitHub = Navegador("github.com","GitHub")

print("Consulta exibir site youtbe")
Youtube.exibirSite()
print('\n')

print("Consulta Verificar Vazias")
PilhaSites = pilhaNavegador()
print(PilhaSites.verificarVazias())


PilhaSites.AcessarSite(Youtube)
PilhaSites.AcessarSite(Instagram)
PilhaSites.AcessarSite(GitHub)


print(PilhaSites.verificarVazias())

PilhaSites.ultimoAcesso()



PilhaSites.exibirHistorico()