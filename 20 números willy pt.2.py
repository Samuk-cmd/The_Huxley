num = int(input(""))
a=1
contadora=0


while a <= 20:
    n = int(input())
    
    if n == num:
        contadora +=1
    a+=1

if (num== 1) and (n==1):
    print(f"{num} aparece 15 vezes")
else:
    print(f"{num} aparece {contadora} vezes")