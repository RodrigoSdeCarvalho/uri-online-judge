# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Brinquedos do Papai Noel, 3039
NumCriancas=int(input()) #Input do número de crianças
Carrinhos=0 #Variáveis que armazenam a quantidade de carrinhos e bonecas
Bonecas=0
for _ in range(0,NumCriancas): #Este "for" vai checar o sexo da criança e atribuir o presente lhe dado em função deste sexo. 
    NomeCrianca,SexoCrianca=input().split()
    if SexoCrianca=='M':
        Carrinhos+=1 #Adiciona "1" à variável de carrinhos.
    else:
        Bonecas+=1 #Adiciona "1" à variável de bonecas.
print(f'{Carrinhos} carrinhos') #Serão impressos as quantidades de carrinhos e bonecas dadas pelo Papai Noel
print(f'{Bonecas} bonecas')