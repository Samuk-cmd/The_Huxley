divida = int(input())
din = int(input())

while divida != 0 and divida >=0:
    
    print(f"(antes) {divida}")
    divida= divida-din
    if divida < 0:
        print("(depois) 0")
    else:
        print(f"(depois) {divida}")
    
