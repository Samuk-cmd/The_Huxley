n1 = int(input(""))
n2 = int(input(""))

while n1 <= n2:
    cal = n1%2!=0
    if cal == True:
        impar = n1
        print(impar)
        n1+=1
    else:
        n1+=1
        