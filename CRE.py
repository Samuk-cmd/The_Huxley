matricula = input("")

media = 0
menorm = 0
menorcre = 0
cont = 0

while matricula != "999":
    cre = float(input(""))
    cont +=1
    media += cre
    
    if cont == 1:
        menorcre = cre
        menorm = matricula
    if cont > 1:
        if cre < menorcre:
            menorcre = cre
            menorm = matricula
    matricula = input("")

media2 = media/cont
    
print(menorm)
print(f"{media2:.2f}")