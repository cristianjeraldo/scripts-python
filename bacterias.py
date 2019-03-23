from random import *
inicial = int(input('Ingrese la cantidad inicial: '))
max = int(input('Ingrese la cantidad maxima: '))
dia = 0
while inicial<=max:
    inicial=2*inicial
    dia=dia+1
print('La cantidad de bacterias excede el max el dia: ', dia)

