import random

nombre = "Ana"
edad = int("18")
ciudades = ["Guayaquil", "Quito", "Cuenca", "Loja"]
elegida = random.choice(ciudades)
registro = "  ESPOL - Guayaquil  "
registro_limpio = registro.strip().lower().replace("espol", "ESPOL")
codigos = ["A", "B", "A", "C", "A"]

print(f"Estudiante: {nombre} | Edad: {edad}")
print("Registro limpio: {}".format(registro_limpio))
print("Primera A:", codigos.index("A"), "| Repeticiones:", codigos.count("A"))
print("Dado:", random.randint(1, 6))
print(f"Ciudad seleccionada: {elegida}")
print("Con reemplazo:", random.choices(ciudades, k=3))
print("Sin reemplazo:", random.sample(ciudades, k=3))
random.shuffle(ciudades)
print("Orden mezclado:", ciudades)
print(f"La lista contiene {len(ciudades)} ciudades")

