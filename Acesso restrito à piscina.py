max = int(input(""))

cont = 0
cont2 = 0
cont3 = 0

adulto = int(input(""))

while adulto >= 0:
    resi = int(input(""))
    convi = int(input(""))
    cont += resi+convi
    cont2 += resi
    cont3 +=adulto
    

    if cont2<max and cont<max:
        print("Acesso permitido!")
    elif cont>max and convi != 0:
        print("Acesso permitido devido a presenca de convidado(s).")

    if adulto != 0 and cont>max and resi == 0 and convi == 0:
        print("Acesso permitido!")

    elif cont>max and convi == 0:
        print("Capacidade maxima de criancas atingida/excedida.")
        print(f"Tem {(cont-resi)-max} crianca(s) a mais que as {max} permitidas.")
        cont-= resi+convi
        cont2-= resi
        cont3-= adulto

    print(f"Adultos na piscina: {cont3}")
    print(f"Criancas na piscina: {cont}")
    print("***")

    adulto = int(input(""))
