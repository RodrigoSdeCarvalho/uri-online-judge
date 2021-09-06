# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Matriz Escada, 2450

N, M = map(int, input().split()) #Entrada das dimensões da Matriz.
Indice = -1 #Mostra que o Indice não foi definido.
Escada = 'S' #Valor padrão do formato da matriz.

for i in range(N): #Testará todas as linhas da matriz.
    try: #Evita erros em relação ao último elemento.
        Linha = [int(x) for x in input().split()] #Entrada da linha da matriz
        if Indice != -1: #Se o indice ainda foi definido, ele segue este if.
            if Indice < M - 1: #Se for menos que o maior indice, ele soma 1.
                Indice += 1 #Aumenta o indice, para o da próxima linha.
            for j in range(Indice + 1): #Testa se o elemento da matriz é zero.
                if Linha[j] != 0:
                    Escada = 'N' #Se não for zero, não tem formato de escada.
            for i in Linha: #Para elementos da matriz, testa-se os diferentes de zero e troca-se o indice baseado nisso.
                if i != 0:
                    indic = Linha.index(i)
                    Indice = indic - 1
                    break #Sai do loop pois já se alterou o indice.
                Indice = M - 1 #Altera o indice caso este não tenha sido alterado.
        else: #Se o Indice já estiver definido.
            if Linha[0] == 0: #Se o primeiro elemento da linha, troca-se o indice.
                for i in Linha:
                    if i != 0: #Se algum elemento da linha for diferente de zero, troca-se o indice.
                        indic = Linha.index(i)
                        Indice = indic - 1 
                        break
                if Indice == -1: #Se o indice for -1, defini-se como M - 1.
                    Indice = M - 1
    except: 
        break

print(Escada) #Imprime o resultado.