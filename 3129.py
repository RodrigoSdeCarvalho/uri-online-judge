# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Figurinhas Repetidas, 3129

quantFigurinhas = int(input()) #Entrada da quantidade de figurinhas.
Figurinhas = [] #Armazena as figurinhas.
quantRepetidas = 0 #Armazena as repetidas.
quantDiferentes = 0 #Armazena as diferentes.

for _ in range(quantFigurinhas): #Recebe o número de cada figurinha e adiciona à lista.
    num = int(input())
    Figurinhas.append(num)

Conferidos = [] #Armazena as figurinhas conferidas.
for i in Figurinhas: #Percorre todas as figurinhas. Se uma destas já existe no "Conferidos", será somado 1 a quantRepetidas; ela não estiver lá, soma-se 1 a quantDiferentes e adiciona-se esse número a Conferidos.
    if i not in Conferidos:
        quantDiferentes += 1
        Conferidos.append(i)
    else:
        quantRepetidas += 1
print(quantDiferentes) #Imprime os resultados.
print(quantRepetidas)