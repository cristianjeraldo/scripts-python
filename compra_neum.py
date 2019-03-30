precio = 1000
neum = int(input('Por favor indique cuantos: '))
if neum >6:
    valor15 = precio*neum*0.85
    print(int(valor15))
else:
    valor10 = precio*neum*0.90
    print(int(valor10))