import random
import sys
import time


def randomPermutation(ciudades):
    permutacion = []
    longitud = len(ciudades)
    for _ in range(0, longitud):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        permutacion.append(ciudad)
        ciudades.remove(ciudad)
    return permutacion


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

    solucion = randomPermutation(ciudades)
    longitud = evaluarSolucion(datos, solucion)

    # print("Longitud de la ruta: ", longitud)
    # Obtenemos el mejor vecino hasta que no haya vecinos mejores
    vecino = obtenerMejorVecino(solucion, datos)
    while vecino[1] < longitud:
        solucion = vecino[0]
        longitud = vecino[1]
        # print("Longitud de la ruta: ", longitud)
        vecino = obtenerMejorVecino(solucion, datos)

    return solucion, longitud


def main():
    if len(sys.argv) != 2:
        sys.exit()

    datos = []
    ruta_fichero = sys.argv[1]

    with open(ruta_fichero) as fichero:
        for linea in fichero:
            datos.append([eval(dato) for dato in linea.split()])

    tiempo_acumulado = 0
    iteraciones = 100
    solucion = []
    caminos = []
    longitudes = []
    for _ in range(iteraciones):
        # print("--------------")
        inicio = time.time()
        solucion = hillClimbing(datos)
        final = time.time()
        caminos.append(solucion[0])
        longitudes.append(solucion[1])
        tiempo_acumulado += (final - inicio)

    print("--------------")
    print("Solucion final: ", caminos)
    print("Longitud de la ruta final: ", longitudes)
    print("Tiempo necesitado medio: ", (tiempo_acumulado/iteraciones) * 10**3,
          "ms")


if __name__ == "__main__":
    main()
