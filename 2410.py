# -*- coding: utf-8 -*-
# Rodrigo - Prova 3, Frequencia na Aula, 2410
quant_reg = int(input()) #Recebe a quantidade de registros.
alunos = [] #Lista com os registros.

for i in range(0, quant_reg): #Vai permitir o input dos registros dos alunos e adicionar à lista de registros.
    reg = int(input())
    alunos.append(reg) #Adiciona aluno presente na lista de presença.

alunos = set(alunos) #Cria um conjunto com os elementos da lista, removendo os valores repetidos e ordenando-os.
quantAlunos = len(alunos) #Informa a quantidade de alunos presentes.

print(quantAlunos) #Imprime o resultado na tela.