"""Exercício 4: Corrigindo um Erro de Índice (IndexError)
O código abaixo tenta acessar um índice fora dos limites de uma lista, mas agora há mais de um problema.

```
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])
```
Tarefa:
1- Teste diferentes entradas do usuário e veja o que acontece.
2- Corrija o código para que ele não permita índices inválidos.
3- Adicione `try-except` para evitar que o programa quebre."""

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: "))

try: 
    if indice > len(numeros):
        raise ValueError("não é possível acessar este índice.")
        
    print(numeros[indice])
except ValueError as e:
    print(f"error: {e}")