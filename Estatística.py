home = 0
mul = 0
media = 0
mediah = 0
cont = 0
conth = 0

maiorsal = 0
maiorsex = ''

for i in range (1,11):

    sal = float(input(""))
    sex = input("")

    if sex == 'm':
        home +=1
        mediah+=sal
        media +=sal
        cont+=1
        conth+=1

        if sal > maiorsal:
            maiorsal = sal
            maiorsex = 'm'
            

    if sex == 'f':
        mul +=1
        media+=sal
        cont+=1

        if sal > maiorsal:
            maiorsal = sal
            maiorsex = 'f'

print(home)
print(mul)
print(media/cont)
print(maiorsex)
print(f'{mediah/conth:.1f}')
