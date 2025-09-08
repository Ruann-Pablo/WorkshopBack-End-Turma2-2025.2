"""Exercício 6: Erro ao Trabalhar com Dicionários

O código abaixo tenta acessar uma chave que não existe no dicionário e ainda pede uma entrada do usuário.

```
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")
```

Tarefa:
1️⃣ Teste com diferentes entradas e veja quais causam erro.
2️⃣ Implemente `try-except` para capturar `KeyError` e mostrar uma mensagem amigável.
3️⃣ Pesquise sobre o método `get()` e utilize-o para evitar erros ao acessar o dicionário.

💡 Dica: `dados.get("endereco", "Endereço não encontrado")` evita o erro."""

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

try:
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    valor = dados.get(chave, f"Chave: '{chave}' não existe. Chaves existentes {list(dados.keys())}")
    print(valor)