n1 = int(input())

while (n1>9) or (n1<1):
    print("Insira um número inicial entre 1 e 9")
    n1 = int(input())

n2 = int(input())

while n2>9 or n2<1:
    print("Insira um número final entre 1 e 9")
    n2 = int(input())

if n1>n2:
    print("Nenhuma tabuada nesse intervalo")

for i in range(n1,n2+1,1):

    print(f"{n1} x 1 = {n1*1}")
    print(f"{n1} x 2 = {n1*2}")
    print(f"{n1} x 3 = {n1*3}")
    print(f"{n1} x 4 = {n1*4}")
    print(f"{n1} x 5 = {n1*5}")
    print(f"{n1} x 6 = {n1*6}")
    print(f"{n1} x 7 = {n1*7}")
    print(f"{n1} x 8 = {n1*8}")
    print(f"{n1} x 9 = {n1*9}")

    print("")

    n1+=1

