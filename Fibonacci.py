serie = int(input(""))
t1 = 0
t2 = 0
t3 = 0

cont = 0

for i in range (1, serie+1):
    print(t3)
    cont+=1

    if cont == 1:
        t3+=1
    else:

        t1 = t2
        t2 = t3
        t3 = t1+t2
        