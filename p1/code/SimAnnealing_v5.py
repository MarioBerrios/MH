import random
import math
import sys
import time


def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud


def obtenerVecino(solucion, datos):
    vecinos = []
    longitud_datos = len(solucion)
    for i in range(longitud_datos):
        for j in range(i+1, longitud_datos):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    vecino = vecinos[random.randint(0, len(vecinos) - 1)]
    longitud = evaluarSolucion(datos, vecino)

    return vecino, longitud


def simAnnealing(datos, t0, alpha, ann_function):
    temperatura = t0
    longitud_datos = len(datos)
    ciudades = list(range(longitud_datos))
    solucion = []
    for _ in range(longitud_datos):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)

    soluciones = []
    it = 0

    while temperatura > 0.05:
        vecino = obtenerVecino(solucion, datos)
        incremento = vecino[1]-longitud
        if incremento < 0:
            longitud = vecino[1]
            solucion = vecino[0]
        elif random.random() < math.exp(-abs(incremento) / temperatura):
            if ann_function in (2, 3, 4):
                temperatura = temperatura + temperatura * 0.35
            soluciones.append((solucion, longitud))
            longitud = vecino[1]
            solucion = vecino[0]

        it += 1
        if ann_function == 1:
            temperatura = alpha*temperatura
        elif ann_function == 2:
            # Logarítmico
            temperatura = alpha*t0 / math.log(1 + it)
        elif ann_function == 3:
            # Geométrico
            temperatura = (alpha**it) * t0
        elif ann_function == 4:
            # Lineal
            temperatura = t0 * (500 - it)/500

    soluciones.append((solucion, longitud))
    print("Iteraciones funcion: ", it)
    return min(soluciones, key=lambda solucion: solucion[1]), it


def main():
    if len(sys.argv) != 5:
        sys.exit()

    datos = []
    ruta_fichero = sys.argv[1]
    t0 = eval(sys.argv[2])
    alpha = eval(sys.argv[3])
    ann_function = eval(sys.argv[4])

    with open(ruta_fichero) as fichero:
        for linea in fichero:
            datos.append([eval(dato) for dato in linea.split()])

    tiempo_acumulado = 0
    iteraciones = 100
    solucion = []
    caminos = []
    longitudes = []
    iteraciones_media = 0
    for _ in range(iteraciones):
        inicio = time.time()
        solucion, iteraciones_solucion = simAnnealing(datos, t0, alpha, ann_function)
        final = time.time()
        caminos.append(solucion[0])
        longitudes.append(solucion[1])
        tiempo_acumulado += (final - inicio)
        iteraciones_media += iteraciones_solucion

    print("--------------")
    print("Solucion final: ", caminos)
    print("Longitud de la ruta final: ", longitudes)
    print("Tiempo necesitado medio: ", (tiempo_acumulado/iteraciones) * 10**3,
          "ms")
    print("Iteraciones: ", iteraciones_media/iteraciones)

if __name__ == "__main__":
    main()
