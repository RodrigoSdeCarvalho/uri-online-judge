#Problema 1652 do URI
#Rodrigo Santos de Carvalho
NumIrregular,NumPalavra=map(int, input().split())
consoantes=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
IrregularesPlu=[]
IrregularesSing=[]
RegraDePluralES1=["o", "s", "x"]
RegraDePluralES2=['c', 's']
for i in range(0, NumIrregular):
    IrregularSing, IrregularPlu=map(str, input().split())
    IrregularesPlu.append(IrregularPlu)
    IrregularesSing.append(IrregularSing)
for k in range(0, NumPalavra):
    Palavra=str(input())
    if Palavra in IrregularesSing:
        for j in range(0, len(IrregularesSing)):
            if Palavra==IrregularesSing[j]:
                print(IrregularesPlu[j])       
    elif Palavra[len(Palavra)-1]=='y' and Palavra[len(Palavra)-2] in consoantes:
        Palavra=Palavra.replace('y','')
        Palavra+='ies'
        print(Palavra)
    elif Palavra[len(Palavra)-1] in RegraDePluralES1:
        Palavra+='es'
        print(Palavra)
    elif (Palavra[len(Palavra)-2] in RegraDePluralES2) and ((Palavra[len(Palavra)-1]=='h')):
        Palavra+='es'
        print(Palavra)
    else:
        Palavra+='s'
        print(Palavra)
