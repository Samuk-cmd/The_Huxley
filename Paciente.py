temp = float(input(""))
sec = input("")

if sec != "S":
    if sec!= "N":
        print("Erro")
        
if (temp>=37) and (sec == "S"):
    print("Exames Especiais")
if (temp>=37) and (sec == "N"):
    print("Exames Basicos")
if (temp<37) and (sec == "N"):
    print("Liberado")
if (temp<37) and (sec == "S"):
    print("Exames Basicos")

