# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Gabarito, 2947
numQuestoes=int(input()) #Entrada do número de questões.
Desafortunato=str(input()) #Entrada das respostas do Desafortunato.
numAlunos=int(input()) #Entrada do número de alunos que fizeram a prova.
nota=0 #Armazena a nota possível total da turma.

RespostasProvaveis=[] #Lista para as respostas prováveis, com elementos que também são listas, uma para cada questão.
for _ in range(numQuestoes):
    RespostasProvaveis.append([])

RespostasAlunos=[] #Lista para as respostas dos alunos, com elementos que também são listas, uma para cada questão.
for _ in range(numQuestoes):
    RespostasAlunos.append([])

for i in range(numAlunos): #"For" que testará cada resposta de cada aluno e considerará uma resposta possível se ela for diferente da resposta do Desafortunato.
    respAluno=str(input()) #Entrada das respostas do aluno.
    for k in range(numQuestoes): #Testará cada resposta do aluno "i".
        RespostasAlunos[k].append(respAluno[k]) #Adicionará a resposta da questão "k" do aluno "i" à lista de "RespostasAlunos", no elemento "k", que é uma lista das respostas da pergunta "k".
        if respAluno[k]!=Desafortunato[k]: #Se a resposta for diferente da resposta do Desafortunato, ela será adicionada ao elemento "k" da lista "RespostasProvaveis", que também é uma lista das respostas possíveis da questão k.
            RespostasProvaveis[k].append(respAluno[k])

for j in range(numQuestoes): #Considera a resposta mais provável da questão "j" e faz a contagem da maior nota possível.
    if len(RespostasProvaveis[j])!=0:
        gabaritoQuestãoJ=max(RespostasProvaveis[j], key=RespostasProvaveis[j].count) #Define o gabarito da questão J como a resposta que mais repete para cada questão, encontrada pela função "Max" do elemento "J" da lista "RespostasPossiveis", que é uma lista das respostas possiveis dadas por cada aluno.
        for l in range(numAlunos): #Percorre as respostas dadas para questão e soma 1 para cada resposta que for igual ao gabarito definido.
            if RespostasAlunos[j][l]==gabaritoQuestãoJ:
                nota+=1 

print(nota) #Imprime na tela a maior nota