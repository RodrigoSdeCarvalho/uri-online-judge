# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Area Inferior, 1188
Operacao = str(input()) #Input da operação.

soma = 0 #Armazenará a soma dos elementos da matriz.
M = [[' ']*12]*12 #Criação da matriz 12x12
for i in range(0, 12): #Dois For's que vão percorrer a matriz 12x12 e somar os elementos.
    for j in range(0, 12):
        M[i][j] = float(input())
        if (i >= 7) and (j <= i - 1) and (j >= 12 - i) and (i + j != 11) and (i != j): #Condição pra acessar só os elementos da área inferior.
            soma += M[i][j]

media = soma / 144 #Média dos elementos da matriz.

if Operacao == 'S': #Dependendo do input da operação, será impresso a soma ou a média na tela.
    print(f'{soma:.1f}')
elif Operacao == 'M': 
    print(f'{media:.1f}')