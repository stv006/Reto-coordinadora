def procesar_arreglo(arreglo):
    tipo = arreglo['tipo']
    numeros = arreglo['numeros']

    if tipo == 1:
        valores_unicos = list(set(numeros))
        valores_1_3 = [num for num in numeros if num in [1, 3]]
        valores_ordenados = sorted(numeros + valores_unicos)

        return {
            'valores_unicos': valores_unicos,
            'valores_1_3': valores_1_3,
            'valores_ordenados': valores_ordenados
        }
    else:
        
         return "valor no valido, debe ser 1, 2 o 3."

arreglo_input = {
    'tipo': 1,
    'numeros': [2, 3, 1, 1]
}

resultado = procesar_arreglo(arreglo_input)
print(resultado)
