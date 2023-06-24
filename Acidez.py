num=0
while num != -1: 
    num = float(input(""))
    if num < 7 and num > 0:
        print("ACIDA")
    if num > 7:
        print("BASICA")
    if num == 7:
        print("NEUTRA")