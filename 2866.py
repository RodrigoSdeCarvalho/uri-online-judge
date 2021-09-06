n=int(input())
for i in range(0,n):
    codigo=str(input())
    codigo_traduzido=list(codigo)
    for i in range (0, len(codigo)):
        if codigo[i]==codigo[i].upper():
            codigo_traduzido.remove(codigo[i])
    codigo_traduzido.reverse()
    codigo_traduzido=''.join(codigo_traduzido)
    print(codigo_traduzido)