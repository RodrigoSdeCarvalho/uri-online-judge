# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Peça Perdida, 2322
N=int(input()) #Input do último número da sequência.
Numeros=[int(x) for x in input().split()] #Input da lista dos números.
NumeroFaltante=0 #Variável que irá definir o número que falta.
i=1 #Será usado no "While" abaixo.
while True: #Serve para testar se o valor "i" está na lista de Números; se ele não estiver, ele será impresso. 
    if i not in Numeros and i<=N: #Condições para "i" ser o número faltante.
        NumeroFaltante=i 
        print(NumeroFaltante) #Impressão do Número faltante. 
        break #Sair do loop caso o número faltante seja encontrado.
    i+=1 #Próximo valor de "i" a ser testado.
    