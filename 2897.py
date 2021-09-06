# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Histórico de Comandos, 2897
while True: #Continuará os casos de teste até a condição de break.
    quantComandos=int(input()) #Input do número de comandos para o caso de teste.
    if quantComandos==0: #Condição de break, isto é, o código encerra sua execução quanto "quantCodigos" é zero.
        break
    Comandos= [int(i) for i in input().split()] #Entrada da posição de cada comando a ser realizado no histórico de comandos.
    Comandos_realizados=[] #Lista do histórico de comandos realizados, que será preenchido com cada novo comando deste caso de teste.
    pressTotal=0 #Valor de vezes que a tecla ‘↑’ foi pressionada.
    num_posicao=0 #A cada comando realizado, somar-se-á um a esta variável, já que a posição para o próximo comando aumenta em um para cada comando realizado.
    for i in Comandos: #"For" para definir quantas vezes a tecla ‘↑’ será pressionada para realizar o comando de posição i.
        if i not in Comandos_realizados: #Se "i" não foi realizado ainda neste caso de teste, a tecla ‘↑’ será pressionada "i" vezes mais o número de comandos realizados até então neste caso de teste.
            pressTotal+=(i+num_posicao)
        else: #
            pressTotal+=(Comandos_realizados.index(i)+1)
            '''
            Se o comando de posição "i" já foi realizado neste caso teste, ele foi inserido no histórico de comandos realizados pela segunda vez.
            Assim, será considerada a nova posição desse comando no neste histórico, que é o índice desse comando na lista "Comandos_realizados", acrescido de "1", pois no python a lista 
            começa com índice zero.
            '''
        num_posicao+=1 #Soma-se 1 a esta variável pois se considera que um novo comando foi realizado.
        Comandos_realizados.insert(0,i) #Insere-se o novo comando realizado a esta lista.
    print(pressTotal) #Imprime-se o valor total de vezes que a tecla ‘↑’ foi pressionada.