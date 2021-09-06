# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Colheita de Café, 2871

while True: #Testa vários casos.
    try:
        m, n = map( int, input().split()) #Dimensões da matriz

        matriz = [[]]*m #Matriz nxm

        soma = 0 #Soma dos litros de café.
        for i in range(m): #Percorre a matriz e a preenche com os valores dados pelo usuário.    
            matriz[i] = [int(x) for x in input().split()]
            for j in range(n):
                soma += matriz[i][j]  #Guarda a quantidade de litros informada pelo usuário.

        sacas = soma // 60 #Total de sacas, com cada saca tendo 60 L.
        sobra = soma % 60 #Sobra que não enche uma saca inteira.

        print(f'{sacas} saca(s) e {sobra} litro(s)') #Imprime o resultado.
    except EOFError: #Faz o programa parar quando termina o arquivo de testes.
        break