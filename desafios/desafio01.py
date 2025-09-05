import math

def raiz_quadrada(num: float):
    if num <= 0:
        return ("Número inválido")
    return math.sqrt(num)

condicao = "sim"

while condicao:
    num = int(input("Informe o número: "))
    resultado = raiz_quadrada(num)
    print(round(resultado))

    condicao = str(input("Deseja continuar? (sim ou nao) "))

    if condicao == "nao":
        break


