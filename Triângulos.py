r1 = float(input())
r2 = float(input())
r3 = float(input())

if (r1+r2<=r3) or (r1+r3<=r2) or (r3+r2<=r1):
    print("impossivel")
else:
    if (r1==r2) and (r2==r3):
        print("equilatero")
    elif (r1!=r2) and (r1!=r3) and (r3!=r2):
        print("escaleno")
    else:
        print("isoceles")
