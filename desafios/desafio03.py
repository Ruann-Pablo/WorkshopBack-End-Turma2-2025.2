import math

class FiguraGeometrica:
    @staticmethod
    def circulo(raio: float):
        area = math.pi * math.pow(raio, 2)
        return area
    
    @staticmethod
    def triangulo(base: float, altura: float):
        return (base * altura) / 2
    
    @staticmethod
    def hipotenusa(cateto1: float, cateto2: float):
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
    

def menu():
    while True:
        print("\nEscolha o cálculo que deseja realizar:")
        print("1 - Área do Círculo")
        print("2 - Área do Triângulo")
        print("3 - Hipotenusa de Triângulo Retângulo")
        print("0 - Sair")
        
        escolha = input("Digite a opção: ")
        
        if escolha == "1":
            raio = float(input("Digite o raio do círculo: "))
            area = FiguraGeometrica.circulo(raio)
            print(f"A área do círculo é: {area:.2f}")
            
        elif escolha == "2":
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = FiguraGeometrica.triangulo(base, altura)
            print(f"A área do triângulo é: {area:.2f}")
            
        elif escolha == "3":
            cateto1 = float(input("Digite o primeiro cateto: "))
            cateto2 = float(input("Digite o segundo cateto: "))
            hip = FiguraGeometrica.hipotenusa(cateto1, cateto2)
            print(f"A hipotenusa do triângulo retângulo é: {hip:.2f}")
            
        elif escolha == "0":
            print("Encerrando o programa.")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


menu()