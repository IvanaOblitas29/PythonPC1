costo_comida=float(input('¿Cuanto fue el costo total de su comida?:s/ '))
porcentaje_comida=float(input('¿Que % de propina le dara al mesero?: '))

propina=costo_comida*porcentaje_comida/100

print('Monto de propina a dejar:s/' + str(propina))