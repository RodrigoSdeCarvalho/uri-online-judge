#Problema 1986 do URI
#Rodrigo Santos de Carvalho
maisSuspeito=0
criminoso=0
while True:
    testes=int(input())
    if testes==0:
        break
    suspeitos=[int(x) for x in input().split()]
    suspeitosEmOrdem=sorted(suspeitos, reverse=True)
    for i in range(0, testes):
        if suspeitos[i]==suspeitosEmOrdem[1]:
            criminoso=i+1
    print(criminoso)
