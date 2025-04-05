from documento import documentos
from impressora import imprepossora

notaFiscal = documentos (10,"Preto",True)
xeroxRG = documentos (1000,"Preto",False)
desenho = documentos (10,"Colorido",True)

impressora = imprepossora()

impressora.addImressora(notaFiscal)
impressora.addImressora(xeroxRG)
impressora.addImressora(desenho)

#impressora.verificaVazio()

#impressora.exibirFila()

impressora.calcularValor()