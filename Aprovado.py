n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))

cal = (n1+n2+n3)/3

if cal>=7:
    print("aprovado")
if cal<3:
    print("reprovado")
if (cal<7) and (cal>=3):
    print("prova final")
