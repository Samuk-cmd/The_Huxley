n = int(input())

while n != 0:
    cal = (n // 1) % 10
    cal2 = n//10
    resul = cal*5+cal2
    if resul%7 == 0:
        print("S")
    else:
        print("N")
    n = int(input())