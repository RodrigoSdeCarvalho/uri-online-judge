# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Contando em Chinês, 2102

T = int(input()) #Número de instâncias.

for i in range(0, T): #Loop para cada instância.
    matriz = {}
    dimensão, entradas = [int(x) for x in input().split()] #Entrada para a dimensão e as entradas da matriz.

    for x in range(0, entradas): #Soma das entradas na matriz.
        a, linha, coluna, v = input().split()
        v = int(v)
        if (linha, coluna) in matriz: 
            matriz[linha, coluna] += v 
        else:
            matriz[linha, coluna] = v
    indice = sorted(matriz.keys()) #Possibilita a impressão em ordem.

    for x in indice: #Impressão das saídas desejadas.
        print(f'{x[0]} {x[1]} {matriz[x]}')

    if i != (T - 1): #Impressão de linhas vazias. 
        print()
    else:
        break