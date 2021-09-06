# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Samuel O Cafeicultor, 3152
def area(lados): #Função que calcula a área de um polígono por meio das coordenadas dos vértices (Método de Gauss). 
    coordenadas = [[]]*lados #Cria-se uma matriz "lados"x1.
    for i in range(0, lados): #Este for possibilita que o usuário insira as coordenadas do polígono.
        coordenadas[i] = [int(x) for x in input().split()] #Modifica cada linha da matriz para as coordenadas (x, y) do polígono.

    soma1 = 0 #Armazena o primeiro valor da soma do Método de Gauss.
    for i in range(0, lados): #Percorre todas linhas da matriz.
        if i == lados - 1: #Se for o último caso do For, a coordenada "x" do último vértice, considerando o sentido horário ou antihorário, será multiplicada à coordenada "y" do primeiro vértice. E este produto será somado à soma1.
            soma1 += coordenadas[lados - 1][0] * coordenadas[0][1] #Soma a coordenada "x" da i-ésima coordenada com o a coordenada "y" da coordenada seguinte, e soma-se isto à soma1.
            break #Evita erro de "list index out of range".
        soma1 += (coordenadas[i][0] * coordenadas[i+1][1]) #Realiza a soma mencionada.
    
    soma2 = 0 #Armazena o segundo valor da soma do Método de Gauss.
    for i in range(0, lados): #Percorre todas linhas da matriz.
        if i == lados - 1: #Se for o último caso do For, a coordenada "y" do último vértice, considerando o sentido horário ou antihorário, será multiplicada à coordenada "x" do primeiro vértice.E este produto será somado à soma2.
            soma2 += coordenadas[lados - 1][1] * coordenadas[0][0] #Soma a coordenada "x" da i-ésima coordenada com o a coordenada "y" da coordenada seguinte, e soma-se isto à soma1.
            break #Evita erro de "list index out of range"
        soma2 += (coordenadas[i][1] * coordenadas[i+1][0]) #Realiza a soma mencionada.

    area = (soma1 - soma2) / 2 #Soma a soma1 e a soma2, divindo isto por dois, o que resulta na área do polígono.

    return area #Retorna o valor da área à função.

lados = 4 #Define o lado como sendo 4, já que a questão pede a área de quadrados.
Area_A = abs(area(lados)) #Consideram-se os módulos das áreas para não ter conflito de sinal caso o usuário escolha calcular as áreas com as coordenadas na ordem horário ou antihorária.
Area_B = abs(area(lados))

if Area_A > Area_B: #Se o terreno A for maior, imprime-se "terreno A". Senão, imprime-se  "terreno B".
    print("terreno A")
else:
    print("terreno B")