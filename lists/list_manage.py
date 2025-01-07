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
	"""
    Suma todos los números en una lista.

    Args:
        lista_numeros (list): Lista de números a sumar.

    Returns:
        int: La suma total de los números en la lista.
    """
	total_suma = 0
	for numero in lista_numeros:
		print(f"total suma: {total_suma} - numero: {numero}")
		total_suma += numero
		print(f"resultado: {total_suma}")
	
	return total_suma

def calcular_promedio(suma, lista_numeros):
	"""
    Calcula el promedio de una lista de números.

    Args:
        suma (int): La suma de los números de la lista.
        lista_numeros (list): Lista de números.

    Returns:
        float: El promedio de los números en la lista.
    """
	conteo = len(lista_numeros)
	promedio = suma / conteo
	
	return promedio

def filtrar_pares(lista_numeros):
	"""
    Filtra los números pares de una lista.

    Args:
        lista_numeros (list): Lista de números a filtrar.

    Returns:
        list: Lista de números pares encontrados en la lista original.
    """
	numeros_pares = []

	for numero in lista_numeros:
		if numero % 2 == 0:
			numeros_pares.append(numero)
	
	return numeros_pares

def analizar_lista(lista_numeros):
	"""
    Analiza una lista de números realizando varias operaciones:
    suma total, promedio y filtrado de números pares.
    Muestra los resultados al usuario.

    Args:
        lista_numeros (list): Lista de números a analizar.

    Returns:
        None
    """
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