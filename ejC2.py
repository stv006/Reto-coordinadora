def calcular_tribonacci_secuencia(secuencia_inicial):
    def es_secuencia_fibonacci(secuencia):
        if len(secuencia) < 3:
            return False
        for i in range(2, len(secuencia)):
            if secuencia[i] != secuencia[i-1] + secuencia[i-2]:
                return False 
        return True
    
    if not es_secuencia_fibonacci(secuencia_inicial):
        return "La secuencia  no corresponde a una secuencia fibonacci valida"   
    tribonacci = secuencia_inicial[:]
    
    while len(tribonacci) < 6:  
        siguiente_numero = sum(tribonacci[-3:])
        tribonacci.append(siguiente_numero)
    return tribonacci

secuencia_inicial1 = [1, 1, 2]
secuencia_inicial2 = [5, 8, 13]
secuencia_inicial3 = [2, 3, 5]

resultado1 = calcular_tribonacci_secuencia(secuencia_inicial1)
resultado2 = calcular_tribonacci_secuencia(secuencia_inicial2)
resultado3 = calcular_tribonacci_secuencia(secuencia_inicial3)

print("Resultado 1:", resultado1)  
print("Resultado 2:", resultado2) 
print("Resultado 3:", resultado3) 
