# Primero Función lambda que clasifique si un numero es par
clasificar2 = lambda numero : numero%2==0

print(clasificar2(100))
print(clasificar2(100))

if(clasificar2(100)):
    print("es par")
else:
    print("no es par")
print("")
print("////////////////SEPARADOR///////////////////")
print("")


# Segundo Función lambda que clasifique números mayores a 10 en una lista
numeros = [1,2,3,8,7,10,80,100]
clasificar3 = lambda numero : numero>10
for numero in numeros:
    print(clasificar3(numero))

print("")
print("////////////////SEPARADOR///////////////////")
print("")

# Tercero Función lambda que recibe nombre, edad y ocupación de una persona y devuelva un diccionario con esta información

nombre =input("digite su nombre: ")
edad = input("digite su edad: ")
ocupacion = input("digite ocupacion: ")

datosPersonales = lambda nombre, edad, ocupacion :{nombre, edad, ocupacion}
print (datosPersonales(nombre, edad, ocupacion))

print("")
print("////////////////SEPARADOR///////////////////")
print("")


# Cuarto Función lambda que sume dos números
sumarNumeros = lambda numero1, numero2: numero1 + numero2
print(sumarNumeros(5,10))

print("")
print("////////////////SEPARADOR///////////////////")
print("")

# Quinto Función que multiplique un número por 100
clasificar10 = lambda numero1 : numero1

print(clasificar10(3*100))

print("")
print("////////////////FIN DEL PROGRAMA///////////////////")
print("")