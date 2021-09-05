# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Loteria, 2473
ApostaFla=[int(x) for x in input().split()] #Input, em lista, dos números escolhidos por Flavinho e dos números sorteados
Sorteio=[int(x) for x in input().split()]
Premio=0 #Variável que armazena o total de apostas corretas de Flavinho.
for i in range(0, 6): #Dois "for"s que vão verificar se o valor de uma aposta é igual ao valor sorteado.
    for k in Sorteio:
        if ApostaFla[i]==k:
            Premio+=1
if Premio<3: #Dependendo do número de apostas corretas, imprimir-se-á a palavra correspondente ao prêmio condizente com tal número de acerto.
    print("azar")
elif Premio==3:
    print("terno")
elif Premio==4:
    print("quadra")
elif Premio==5:
    print("quina")
else:
    print("sena")