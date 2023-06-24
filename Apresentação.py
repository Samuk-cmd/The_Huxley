ig = int(input("Trabalho aborda Interface Gráfica? (0 - Nao 1 - Sim)"))
print("")
ia = int(input("Trabalho aborda Inteligência Artificial? (0 - Nao 1 - Sim)"))
print("")
encap = int(input("Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)"))
print("")
indent = int(input("Trabalho aborda Indentação? (0 - Nao 1 - Sim)"))
print("")
structs = int(input("Trabalho aborda Structs? (0 - Nao 1 - Sim)"))
print("")

if (ig or ia == 1):
    if (encap and indent == 1):
        if (structs == 1):
            print("Seu trabalho sera avaliado.")
        else:
            print("Seu trabalho nao sera avaliado, nota 0.")
    else:
        print("Seu trabalho nao sera avaliado, nota 0.")
else:
    print("Seu trabalho nao sera avaliado, nota 0.")
