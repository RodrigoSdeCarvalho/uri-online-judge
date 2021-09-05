while True:
    try:
        while True: #Cria um loop que será capaz de traduzir tantas frases quanto se queira.
            Frase=str(input()) #Entrada para a frase em formato de string.
            Frase=Frase.replace('@','a') #Os "replace"'s abaixo fazem a tradução dos caracteres para a devida vogal.
            Frase=Frase.replace('&','e')
            Frase=Frase.replace('!','i')
            Frase=Frase.replace('*','o')
            Frase=Frase.replace('#','u')
            print(Frase) #Imprime na tela a frase traduzida.
    except EOFError: #Como o programa termina em EOF, este except encerra o programa sem dar erro no URI.
        break