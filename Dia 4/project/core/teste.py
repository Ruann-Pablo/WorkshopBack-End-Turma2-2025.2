import requests
cep = '58356000'

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta_da_api = requests.get(url)
    if resposta_da_api.status_code == 200:
        dados_do_cep = resposta_da_api.json()
        return dados_do_cep
    else:
        return None
    
print(buscar_cep(cep))