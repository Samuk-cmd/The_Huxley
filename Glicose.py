glico = int(input())
media = 0
cont = 0

while glico != 0:
    cont+=1
    media += glico
    glico = int(input()) 

media2 = media/cont

if media2 >= 200:
    print("Glicose Muito Alta")
if media2 < 110:
    print("Glicose Normal")
if (media2 > 110) and (media2 < 200):
    print("Glicose Alterada")