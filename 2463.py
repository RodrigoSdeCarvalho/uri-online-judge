# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Corredor, 2463

salas = int(input()) #Entrada do número de salas
vidas = [int(x) for x in input().split()] #Entrada das vidas em cada sala.
pontos = 0 #Armazena a pontuação.
soma = 0 #Armazena a soma de vidas.

for i in range(0, salas): #Percorre todas as salas.
    soma += vidas[i] #Adiciona o valor da sala à soma.
    if soma < 0: #Se a soma for negativa, volta-se a soma a zero.
        soma = 0
    elif soma > pontos: #Se a soma for maior que pontos, a pontuação muda para a soma.
        pontos = soma

print(pontos) #Imprime-se o resultado.