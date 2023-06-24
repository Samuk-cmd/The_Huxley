escala = input("")
temp = float(input(""))

celsiuspf = (temp*1.8)+32
celsiuspk = temp+273.15

kelvinpc = temp-273.15
kelvinpf = (temp-273.15)*1.8+32

fahpc = (temp-32)/1.8
fahpk = (temp-32)/1.8+273.15



if escala == "C":
    print(f'{celsiuspf} F')
    print(f'{celsiuspk} K')
if escala == "K":
    print(f'{kelvinpc} C')
    print(f'{kelvinpf} F')
if escala == "F":
    print(f'{fahpc} C')
    print(f'{fahpk} K')
