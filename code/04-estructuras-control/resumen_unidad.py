"""Ejemplos integradores de la Unidad 04."""


def clasificar_nota(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 8:
        return "Muy bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Reprobado"


def posiciones_del_maximo(valores):
    maximo = max(valores)
    posiciones = []
    for posicion, valor in enumerate(valores):
        if valor == maximo:
            posiciones.append(posicion)
    return maximo, posiciones


def posiciones_del_minimo(valores):
    minimo = min(valores)
    posiciones = []
    for posicion, valor in enumerate(valores):
        if valor == minimo:
            posiciones.append(posicion)
    return minimo, posiciones


def sin_repetidos(valores):
    resultado = []
    for valor in valores:
        if valor not in resultado:
            resultado.append(valor)
    return resultado


def falta_para_meta(saldo, meta):
    return saldo < meta


notas = [7.2, 9.4, 5.8]
for nota in notas:
    print(nota, clasificar_nota(nota))

ventas = [85, 120, 90, 120, 75]
maximo, posiciones = posiciones_del_maximo(ventas)
print("Máximo:", maximo, "Posiciones:", posiciones)

tiempos = [42, 38, 45, 38]
minimo, posiciones = posiciones_del_minimo(tiempos)
print("Mínimo:", minimo, "Posiciones:", posiciones)

datos = [3, 1, 3, 2, 1, 4]
print("Sin repetidos:", sin_repetidos(datos))

saldo = 0
meta = 60
while falta_para_meta(saldo, meta):
    saldo = saldo + 15
    print("Saldo:", saldo)
