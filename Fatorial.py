n = int(input("Digite um numero inteiro:"))
n2 = n

for i in range (1, n+1):
    if n>1:
        frl = n*(n2-1)
        n = frl
        if n2>2:    
            n2 = n2 - 1
    else:
        break
print(n)

