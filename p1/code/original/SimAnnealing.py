import random
import math


def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud


def obtenerVecino(solucion, datos):
    # Obtención de los vecinos
    vecinos = []
    longitud_datos = len(solucion)
    for i in range(longitud_datos):
        for j in range(i+1, longitud_datos):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    # Obtengo un vecino aleatorio
    vecino = vecinos[random.randint(0, len(vecinos) - 1)]
    longitud = evaluarSolucion(datos, vecino)

    return vecino, longitud


def simAnnealing(datos, t0):
    temperatura = t0
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
    print("Temperatura: ", temperatura)

    it = 0
    while temperatura > 0.05:
        # Obtenemos un vecino al azar
        vecino = obtenerVecino(solucion, datos)
        incremento = vecino[1]-longitud

        if incremento < 0:
            longitud = vecino[1]
            solucion = vecino[0]
        elif random.random() < math.exp(-abs(incremento) / temperatura):
            longitud = vecino[1]
            solucion = vecino[0]

        it += 1
        temperatura = 0.99*temperatura
        print("Longitud de la ruta: ", longitud)
        print("Temperatura: ", temperatura)
    return solucion, longitud


def main():
    datos = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    t0 = 10

    solucion = simAnnealing(datos, t0)
    print("--------------")
    print("Solucion final: ", solucion[0])
    print("Longitud de la ruta final: ", solucion[1])


if __name__ == "__main__":
    main()
