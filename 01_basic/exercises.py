###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre, cuidad = input("Introduce tu nombre y tu ciudad separados por una coma: ").split(",")

print(f"Hola! Me llamo {nombre} y vivo en {cuidad}.")
print(nombre)
print(cuidad)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"El tipo de dato de a es: {type(a)}")
print(f"El tipo de dato de a es: {type(b)}")
print(f"El tipo de dato de a es: {type(c)}")
print(f"El tipo de dato de a es: {type(d)}")
print(f"El tipo de dato de a es: {type(e)}")

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

texto = "12345" 

numero_entero = int(texto)
print(f"El número entero es: {numero_entero}")

numero_float = float(numero_entero)
print(f"El número float es: {numero_float}")

numero_f = 3.99
numero_entero_f = int(numero_f)
print(f"El número entero es: {numero_entero_f}")

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "Jefferson Lopez"
edad = 21
altura = 1.65

# esto es un f string print(f"")
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

numero_pi = 3.14159

redondeado = round(numero_pi)

#para realizar una division hay que usar el simbolo // 
#para mi eso es un poco raro ya que vengo de js 
division = redondeado // 2

print(f"El número PI es: {numero_pi}")
print(f"El número PI redondeado es: {redondeado}")
print(f"La división entera es: {division}")
