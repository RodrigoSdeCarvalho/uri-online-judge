#Problema 2116 do URI
#Rodrigo Santos de Carvalho
import math #Será usada no cálculo de números primos.
N,M=map(int, input().split()) #Juilherme escolhe um número N e Jogério escolhe um número M. Estes números estarão em uma única linha.

PrimosP1=[] #Lista com números primos entre 0 e N.
for x in range (2,N+1): #Método para definir os primos entre 0 e N, para achar P1.
    x_notprime=False #Valor lógico que vai definir se x é primo ou não, sendo x um possível número para P1.
    y=int(math.sqrt(x)) #Técnica para agilizar a determinação de se x é primo ou não.
    for i in range(2, y+1): #Teste de se x é primo ou não; se x for divisível por algum i, não é primo, mas se não for divisível, então é primo.
        if x%i==0: 
            x_notprime=True
            break
    if x_notprime==False:
        PrimosP1.append(x) #Adicionar x à lista de possíveis P1.

PrimosP2=[] #Lista com números primos entre 0 e M.
for x in range (2,M+1): #Método para definir os primos entre 0 e N, para achar P2
    x_notprime=False #Valor lógico que vai definir se x é primo ou não, sendo x um possível número para P2.
    y=int(math.sqrt(x)) #Técnica para agilizar a determinação de se x é primo ou não.
    for i in range(2, y+1):  #Teste de se x é primo ou não; se x for divisível por algum i, não é primo, mas se não for divisível, então é primo.
        if x%i==0:
            x_notprime=True
            break
    if x_notprime==False:
        PrimosP2.append(x) #Adicionar x à lista de possíveis P1.

PrimosP1=sorted(PrimosP1, reverse=True) #Ordenar os possíveis P1s e P2s, do maior para o menor, para facilitar a busca do primos mais próximos a N e M
PrimosP2=sorted(PrimosP2, reverse=True)

Saida=PrimosP1[0]*PrimosP2[0] #Multiplicação dos primos mais próximos a N e M.
print(Saida) #Saida do problema.
