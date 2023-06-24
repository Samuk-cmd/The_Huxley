sal = float(input())
if sal > 500:
    ns = sal * 0.1
    salariof = ns+sal
elif sal > 300:
    ns = sal * 0.07
    salariof = ns+sal
else:
    ns = sal* 0.05
    salariof = ns+sal
print(f"{salariof:.2f}")
