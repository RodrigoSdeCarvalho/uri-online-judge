# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Atrasadinhos, 3117
Alunos,minPessoas=map(int,input().split()) #Input do número de alunos e do mínimo de pessoas para realizar o treinamento.
HorarioChegada=[int(x) for x in input().split()] #Input, em formato de lista, convertendo "HorarioChegada[i]" para inteiro, dos valores correspondentes à hora de chegada dos alunos.
NumAtrasados=0 #Valor onde será armazenada a soma dos alunos atrasados.
for i in HorarioChegada: #"For" que permite calcular o número de atrasados.
    if i>0: #Se o tempo do aluno indicar atraso, somar-se-á "1" à varável "NumAtrasados".
        NumAtrasados+=1
if Alunos-NumAtrasados<minPessoas: #Se o número de alunos presentes for menor que o mínimo dado, será impresso "NO" na tela; do contrário, será impresso "YES" na tela.
    print("NO")
else:
    print("YES")