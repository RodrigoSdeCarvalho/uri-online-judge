n=int(input())
hexadecimal=input().split()
dec=hexadecimal
for i in range(0,len(hexadecimal)):
    dec[i]=int(hexadecimal[i], 16)
message=dec
for i in range(0, len(message)):
    message[i]=chr(dec[i])
print(''.join(message))