n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if (n1 > n2 > n3):
    print(f"Os números em ordem crescente: {n3}, {n2}, {n1}")
elif (n2 > n3 > n1):
    print(f"Os números em ordem crescente: {n1}, {n3}, {n2}")
elif (n3 > n1 > n2):
    print(f"Os números em ordem crescente: {n2}, {n1}, {n3}")
elif (n3 > n2 > n1):
    print(f"Os números em ordem crescente: {n1}, {n2}, {n3}")
else:
    print(f"Os números em ordem crescente: {n2}, {n3}, {n1}")