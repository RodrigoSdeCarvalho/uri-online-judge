# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Correção de Texto, 3088
while True: #Repetirá o código até todos os casos forem testados.
    try: #Serve para evitar o erro de EOF.
        Frase=str(input()) #Entrada da frase a ser corrigida.
        i=0 #Será usado abaixo.
        while True:
            if Frase[i]==' ' and (Frase[i+1]==',' or Frase[i+1]=='.'):
                Frase=list(Frase) #Transforma a string em lista, facilitando a análise.
                del Frase[i] #Remove o espaço antes da vírgula.
                Frase=''.join(Frase) #Retorna a variável "Frase" à forma de string.
            if (len(Frase)-1)==i: #Impede o erro "Out of index", ao garantir que o loop se encerre antes de o i superar o tamanho da string "frase".
                break
            i+=1 #Define o próximo valor a ser testado no primeiro "if" deste loop.
        print(Frase) #Imprime na tela a frase corrigida.
    except EOFError: #Realiza o término da execução do código até a ocorrência do EOF, como pede o problema.
        break 