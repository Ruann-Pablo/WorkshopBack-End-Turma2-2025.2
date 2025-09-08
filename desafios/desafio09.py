"""Exercício 3: Erro de Tipagem (TypeError)
O código abaixo tenta misturar tipos incompatíveis. Mas agora, o erro não é tão óbvio.

```
def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)
```
Tarefa:
1- Leia a stacktrace e identifique a causa do erro.
2- Corrija o código sem alterar a chamada da função (`somar(10, "5")`).
3- Dica: Use `try-except` para capturar e tratar o erro de forma inteligente."""

def somar(a, b) -> float:
    try:
        return a + b
    except TypeError as e:
        raise TypeError(f"error: {e}")



resultado = somar(10, "r")
print(resultado)

