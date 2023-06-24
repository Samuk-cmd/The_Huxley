num = int(input(""))
cont = 0

while num != -1:
    for i in range (1, num+1):
        if num%i == 0:
            cont+=1
        else:
            cont+=0

    if num != 1 and num!= 0:
        if cont>2:
            
            print("0")
            cont = 0
        else:
            print("1")
            cont = 0
    else:
        print("0")
        cont = 0

    num = int(input(""))
