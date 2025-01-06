"""
Vas a escribir un programa que utilice funciones para analizar una
lista de números. El programa debe:
1. Sumar todos los números de la lista.
2. Calcular el promedio de los números.
3. Devolver una lista con los números pares encontrados.
4. Crear una función que muestre todos estos resultados al usuario.

Paso a paso
1. Crear una función llamada sumar_lista:
  - Recibe una lusta de números como argumento.
  - Devuelve la suma de todos los números.
2. Crear una función llamada calcular_promedio:
  - Recibe una lista de números como argumento.
  - Devuelve el promedio de los números (suma de los números
    dividido por la cantidad de elementos).
3. Crear una función llamada filtrar_pares:
  - Recibe una lista de números como argumento
  - Devuelve una lista que contiene solo los números pares
    de la lista original.
4. Crear una función llamada analizar_lista:
  - Llama a las tres funciones anteriores.
  - Imprime los resultados de manera clara.
"""

def sumar_lista(lista_numeros):
	total_suma = 0
	for numero in lista_numeros:
		total_suma += numero
	
	return total_suma

def calcular_promedio(suma, lista_numeros):
	conteo = len(lista_numeros)
	promedio = suma / conteo
	
	return promedio

def filtrar_pares(lista_numeros):
	numeros_pares = []

	for numero in lista_numeros:
		if numero % 2 == 0:
			numeros_pares.append(numero)
	
	return numeros_pares

def analizar_lista(lista_numeros):
	total_suma = sumar_lista(lista_numeros)
	total_promedio = calcular_promedio(total_suma, lista_numeros)
	pares = filtrar_pares(lista_numeros)

	print(f"La lista: {lista_numeros}")
	print(f"la suma de todos los numeros: {total_suma}")
	print(f"el promedio de todos los numeros: {total_promedio}")
	print(f"La lista de numeros pares: {pares}")

	pass


lista_numeros = [3,7,2,8,15,17,37,43,66]
analizar_lista(lista_numeros)