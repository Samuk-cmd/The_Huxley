dia = int(input(""))

dias = ['0', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

if dia > 0 and dia < 8:
    print(dias[dia])
else:
    print("valor invalido")
