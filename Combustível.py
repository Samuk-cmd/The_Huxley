print("Digite o tempo gasto (em horas) e a velocidade media (em km/h):")
temp = int(input())
vm = int(input())

lito = (vm*temp)/12

print(f"Quantidade de litros gastos na viagem: {lito:.6f}")