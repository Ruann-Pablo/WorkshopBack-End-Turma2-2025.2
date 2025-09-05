import math

def arredondando(num: float):
    return {
        'piso': math.floor(num),
        'teto': math.ceil(num),
        'inteiro': math.trunc(num)
    }

num = 3.14159

resultado = arredondando(num)

print(f"Piso: {resultado['piso']}")
print(f"Teto: {resultado['teto']}")
print(f"Parte inteira: {resultado['inteiro']}")
