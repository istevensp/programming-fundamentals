def convertir_minutos(minutos):
    horas = minutos // 60
    restantes = minutos % 60
    return horas, restantes


def esta_en_rango(valor, minimo=0, maximo=100):
    return minimo <= valor <= maximo


horas, minutos = convertir_minutos(145)
print(f"145 minutos = {horas} h y {minutos} min")
print(esta_en_rango(75))

