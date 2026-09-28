"""Ejemplo integrador de la Unidad 06."""

import numpy as np
import pandas as pd


datos = {
    "nombre": ["Ana", "Luis", "Marta", "José", "Elena", "Diego"],
    "carrera": [
        "Computación",
        "Mecánica",
        "Computación",
        "Industrial",
        "Mecánica",
        "Industrial",
    ],
    "nota": [8.5, 5.4, 9.0, 6.8, 7.6, 5.9],
    "asistencia": [0.90, 0.75, 0.95, 0.82, 0.88, 0.79],
}

tabla_desde_lista = pd.DataFrame([8.5, 7.2, 9.1], columns=["nota"])
arreglo_notas = np.array([8.5, 7.2, 9.1])
tabla_desde_arreglo = pd.DataFrame(arreglo_notas, columns=["nota"])
print("DataFrame desde lista:")
print(tabla_desde_lista)
print("DataFrame desde arreglo 1D:")
print(tabla_desde_arreglo)

estudiantes = pd.DataFrame(datos, index=["E01", "E02", "E03", "E04", "E05", "E06"])

print("Primera fila por etiqueta:")
print(estudiantes.loc["E01"])
print("Primera fila por posición:")
print(estudiantes.iloc[0])

estudiantes["nota_porcentual"] = estudiantes["nota"] * 10
estudiantes["estado"] = "Aprobado"
estudiantes["estado"] = estudiantes["estado"].mask(
    estudiantes["nota"] < 6,
    "Reprobado",
)

seleccion = estudiantes[
    (estudiantes["nota"] >= 6) &
    (estudiantes["asistencia"] >= 0.80)
]
print("Selección:")
print(seleccion[["nombre", "nota", "asistencia"]])

print("Código con nota máxima:", estudiantes["nota"].idxmax())
print("Carreras únicas:", estudiantes["carrera"].unique())
print("Frecuencias:")
print(estudiantes["carrera"].value_counts())

ordenados = estudiantes.sort_values(
    ["carrera", "nota"],
    ascending=[True, False],
)
print("Ordenados:")
print(ordenados[["nombre", "carrera", "nota"]])

resumen = estudiantes.groupby("carrera")[["nota", "asistencia"]].mean()
print("Resumen por carrera:")
print(resumen)
