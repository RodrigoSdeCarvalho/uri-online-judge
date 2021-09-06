# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Campo de Batalha, 3090
comp, larg, soldados = map(int, input().split()) #Entrada dos dados do problema.
coefAngRio = larg/comp #Δy/Δx, coeficiente angular da reta. 
habEx1 = 0 #Soma das habilidades do exército 1.
habEx2 = 0 ##Soma das habilidades do exército 2.

for _ in range(soldados): #Entrada dos dados do soldado.
    x, y, habilidade = map(int, input().split()) #Dados do soldado.
    if x == 0: #Se "x=0", y é diferente de zero (condição do problema) e sempre acima do rio.
        habEx1 += habilidade #Soma-se a habilidade do soldado ao exército 1.
    elif (y/x) > coefAngRio : #Se é maior, a inclinação do soldado é maior que a do rio, logo acima do rio.
        habEx1 += habilidade #Soma-se a habilidade do soldado ao exército 1.
    elif (y/x) < coefAngRio: #Se é menor, a inclinação do soldado é menor que a do rio, logo abaixo do rio.
        habEx2 += habilidade #Soma-se a habilidade do soldado ao exército 2.

print(f'{habEx1} {habEx2}') #Imprime-se os resultados.