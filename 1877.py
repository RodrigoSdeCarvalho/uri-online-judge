# -*- coding: utf-8 -*-
quant,picos=list(map(int,input().split()))
torres=[int(x) for x in input().split()] 
quantPicos=0
for x in range (1, quant-1):
    if torres[x]>torres[x-1] and torres[x]>torres[x+1]:
        quantPicos+=1
if quantPicos==picos:
    print('beautiful')
else:
    print('ugly')