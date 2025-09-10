"""Exercício 5: Tratando Múltiplos Erros ao Mesmo Tempo

O código abaixo pode gerar vários tipos de erro dependendo da entrada do usuário.

```
def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")
```

Tarefa:
1️⃣ Identifique quais erros esse código pode gerar.
2️⃣ Implemente `try-except` para capturar diferentes erros e mostrar mensagens adequadas.
3️⃣ Pesquise possíveis abordagens para tornar o código mais robusto.

💡Dica:
- O usuário pode inserir um texto em vez de um número (`ValueError`).
- O segundo número pode ser zero, gerando um `ZeroDivisionError`."""

def dividir(num1:str, num2:str) -> float:
    try:
        num_1 = float(num1)
        num_2 = float(num2)
        return num_1 / num_2
    except ValueError:
        print("Erro: você deve digitar números válidos (ex.: 10, 3.5).")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except TypeError:
        print("Erro: tipos inválidos recebidos.")


num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(num1, num2)
print(f"Resultado: {resultado}")