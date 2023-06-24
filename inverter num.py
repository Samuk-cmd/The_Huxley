num = int(input())

unidade = (num // 1) % 10
dezena = (num // 10) % 10
centena = num // 100

print(f'{unidade}{dezena}{centena}')