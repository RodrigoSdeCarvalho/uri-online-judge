# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Pares de Números, 3059
N,MinSoma,MaxSoma=map(int,input().split()) #input do número de elementos do Vetor, do  valor mínimo da soma entre estes elementos e do valor máximo entre estes elementos, respectivamente.
Vetor=[int(x) for x in input().split()] #Input do Vetor.
NumPares=0 #Variável que armazena o número de pares cuja soma é válida.
for i in range(0, N): #Dois "for"s que fazem a soma dos elementos do Vetor e somam "1" a "NumPares" para cada soma válida.
    for k in Vetor:
        if k!=Vetor[i]:
            if  MinSoma<=(k+Vetor[i])<=MaxSoma:
                NumPares+=1
print(int(NumPares/2)) #Imprime-se o valor de somas válidas, mas dividido por dois, já que os "for"s consideram o par {a,b} diferente de {b,a}.