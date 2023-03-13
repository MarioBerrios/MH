import random


def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud


def obtenerMejorVecino(solucion, datos):
    # Obtención de los vecinos
    vecinos = []
    longitud_datos = len(solucion)
    for i in range(longitud_datos):
        for j in range(i+1, longitud_datos):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    # Obtención del mejor vecino
    mejorVecino = vecinos[0]
    mejorLongitud = evaluarSolucion(datos, mejorVecino)
    for vecino in vecinos:
        longitud = evaluarSolucion(datos, vecino)
        if longitud < mejorLongitud:
            mejorLongitud = longitud
            mejorVecino = vecino
    return mejorVecino, mejorLongitud


def hillClimbing(datos):
    longitud_datos = len(datos)
    # Creamos una solucion aleatoria
    ciudades = list(range(longitud_datos))
    solucion = []
    for i in range(longitud_datos):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)

    print("Longitud de la ruta: ", longitud)
    # Obtenemos el mejor vecino hasta que no haya vecinos mejores
    vecino = obtenerMejorVecino(solucion, datos)
    while vecino[1] < longitud:
        solucion = vecino[0]
        longitud = vecino[1]
        print("Longitud de la ruta: ", longitud)
        vecino = obtenerMejorVecino(solucion, datos)

    return solucion, longitud


def main():
    datos = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

    solucion = hillClimbing(datos)
    print("--------------")
    print("Solucion final: ", solucion[0])
    print("Longitud de la ruta final: ", solucion[1])


if __name__ == "__main__":
    main()
