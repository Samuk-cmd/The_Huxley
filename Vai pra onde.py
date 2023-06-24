lugar = "bola"

while lugar != "FIM":

    lugar = input("")

    if lugar == "FIM":
        print("SEM DESTINO")
        break

    km = int(input())  
    din = float(input())
    
    lugar2 = input("")

    if lugar2 == "FIM":
        print(lugar)
        break

    km2 = int(input())  
    din2 = float(input())

    if km>km2 and din*2<=300:
        print(lugar)
    elif km2>km and din2*2<=300:
        print(lugar2)


    
    
    

