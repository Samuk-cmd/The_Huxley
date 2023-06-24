n = int(input(""))

contadora = 0
contadora2 = 0

while n!=n+1:
    num = int(input())
    contadora2 +=1
    if num == n:
        contadora +=1
    else:
        contadora += 0
    if num == -1:
        break
    if contadora2 == 20:
        print(f"{n} aparece {contadora} vezes")
        break
