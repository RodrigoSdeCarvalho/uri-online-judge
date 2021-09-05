# -*- coding: utf-8 -*-
# Rodrigo - Prova 2, Estados do Norte, 2803
EstadoBr=str(input()) #Input do estado em questão.
EstadosDoNorte=['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins'] #Lista de estados da região Norte.
if EstadoBr in EstadosDoNorte:
    print("Regiao Norte") #Se o estado em questão pertencer ao Norte, será impresso "Regiao Norte".
else:
    print("Outra regiao") #Se o estado em questão não pertencer ao Norte, será impresso "Outra regiao".