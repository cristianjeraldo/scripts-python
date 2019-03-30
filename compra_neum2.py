n = int(input('Ingrese la cantidad de neumaticos: '))
p = float(input('Ingrese el precio unitario: '))
if n>6:
    s = n*p
    d = s*0.15
    total = s-d
else:
    s = n*p
    d = s*0.1
    total = s-d
Print('El total a pagar es: ', total)
Print('El descuento es: ', d)

