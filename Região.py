codigo = int(input(""))

if codigo == 1:
    print("Nordeste")
if codigo == 2:
    print("Norte")
if codigo == 3 or codigo == 4:
    print("Centro-Oeste")
if codigo >= 5 and codigo <=9:
    print("Sul")
if codigo >= 10 and codigo <= 15:
    print("Sudeste")