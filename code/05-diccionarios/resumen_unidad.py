"""Ejemplos integradores de la Unidad 05."""


def contar(elementos):
    frecuencias = {}
    for elemento in elementos:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    return frecuencias


def filtrar_minimo(datos, minimo):
    seleccion = {}
    for clave, valor in datos.items():
        if valor >= minimo:
            seleccion[clave] = valor
    return seleccion


def agrupar_por_valor(datos):
    grupos = {}
    for clave, valor in datos.items():
        if valor not in grupos:
            grupos[valor] = []
        grupos[valor].append(clave)
    return grupos


texto = "datos python datos código python datos"
print("Frecuencias:", contar(texto.split()))

notas = {"A": 8.5, "B": 5.4, "C": 9.0, "D": 6.0}
print("Aprobadas:", filtrar_minimo(notas, 6))

paralelos = {"Ana": "A", "Luis": "B", "Marta": "A", "José": "B"}
print("Por paralelo:", agrupar_por_valor(paralelos))
