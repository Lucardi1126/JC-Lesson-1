    #  Solucion Reto_01


print('Inserte el numero "a"')
a = input()
print('Inserte el numero "b"')
b = input()

#  Se realiza el cast

int_a = int(a)
int_b = int(b)

#    Concatenacion de a y b 

concat = a + b 

#    Suma de a y b con el cast hecho 

suma = int_a + int_b

#     Imprimiendo los resultados 

print('El resultado de la concatenacion es:{}'format(concat))
print(suma)



# Solucion reto 02

print('Inserte un numero')
a = input()
print('Inserte un segundo numero')
b = input()

num1 = int(a)
num2 = int(b)

# Resta
print('El resultado de la resta es:')
print(num1 - num2)

# Modulo
print('El modulo de los numeros es:')
print(num1 % num2)

# Operador logico 

dato1 = True
dato2 = False

print('Operación OR de un dato Trure y un False')
print(dato1 or dato2)

# Solucion Reto03

print('¿Que tabla quieres calcular?')
numero = int(input())
numero2 = 1

#Crea e imprime cadenas de texto
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )
numero2 += 1
print("{} * {} = {}".format(numero, numero2, numero*numero2) )

# Solución Reto04


print("Qué topping quieres en tu helado?")
topping = input()

if topping == "oreo":
	precio = 19
elif topping == "m&m":
	precio = 25
elif topping == "fresas":
	precio = 22
elif topping  == "brownie":
	precio = 28
else:
	print("producto no disponible")

print("El precio es ${}".format(precio))

# Solucion Reto05

#Se solocotan los datos
print("inserta el primer numero")
num1 = int(input())
print("inserta el segundo numero")
num2 = int(input())
print("Selecciona operación a realizar")
print("+ -> Suma")
print("- -> Resta")
print("* -> Multiplicaión")
print("/ -> División")
print("% -> Modulo")
operacion = input()

#Estructura de condicionales
if operacion == '+':
	resultado = num1 + num2
elif operacion == '-':
	resultado = num1 + num2
elif operacion == '*':
	resultado = num1 + num2
elif operacion == '/':
	if num2 == '0':
		print("ERROR: División entre 0")
		resultado = 'ERROR'
	else:
		resultado = num1 / num2
elif operacion == '%':
	resultado = num1 % num2
else:
	resultado = 'ERROR'
	print("Operacion no definida")

#Imprime el resultado
print("{} {} {} = {}".format(num1,operacion, num2, resultado))
