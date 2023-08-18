def calcular_puntuacion_matriz(lista_numeros):

    puntuacion_total = 0

    for numero in lista_numeros:
        if numero % 2 == 0:
             puntuacion_total += 1
        elif numero == 5:
            puntuacion_total += 5
        else:
            puntuacion_total += 3

    return puntuacion_total

matriz_ejemplo1 = [10, 15, 7, 8, 5]
matriz_ejemplo2 = [21, 4, 11, 2]

puntuacion_matriz1 = calcular_puntuacion_matriz(matriz_ejemplo1)
puntuacion_matriz2 = calcular_puntuacion_matriz(matriz_ejemplo2)

print("Puntuación Matriz 1:", puntuacion_matriz1) 
print("Puntuación Matriz 2:", puntuacion_matriz2)  

