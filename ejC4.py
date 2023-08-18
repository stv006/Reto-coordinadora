
N = int(input("Ingrese la cantidad de elementos a leer (1-15): "))

def leer_valor():
    while True:
        valor = int(input("Ingrese un numero entre 1 y 30: "))
        if 1 <= valor <= 30:
            return valor
        else:
            print("Valor invalido, Intente nuevamente con los numeros mencionados anteriormente")
vector1 = []
vector2 = []

print("Ingrese valores para el vector 1:")
for i in range(N):
     valor = leer_valor()
     
     vector1.append(valor)

print("Ingrese valores para el vector 2:")
for i in range(N):
    valor = leer_valor()
    vector2.append(valor)


vector1.sort()
vector2.sort()

print("Vector 1 ordenado:", vector1)
print("Vector 2 ordenado:", vector2)



suma_vectores = [vector1[i] + vector2[i] for i in range(N)]
print("Suma de vectores:", suma_vectores)
