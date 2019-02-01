Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mis_valores = [5, 6, 10, 13, 3, 4]
>>> mis_valores
[5, 6, 10, 13, 3, 4]
>>> cantidad = len(mis_valores)
>>> cantidad
6
>>> suma = 0
>>> suma
0
>>> for i in mis_valores :
	suma += i

	
>>> suma
41
>>> promedio = suma / cantidad
>>> print('El promedio de los valores de la lista es: %.2f' % promedio)
El promedio de los valores de la lista es: 6.83
>>> 
