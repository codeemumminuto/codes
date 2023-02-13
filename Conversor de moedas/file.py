import requests
import json

def converter(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")
    
    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None

print("=== Conversor de moedas ===")
print("Principais moedas disponíveis: USD, BRL, EUR, JPY, BTC, ETH, DOGE, ETC.\n")

valor = float(input("Valor: "))
de = input("Converter de (código): ")
para = input("Converter para (código): ")

cotacao = converter(valor, de, para)

if cotacao is not None:
    print(f"{valor} {de} é equivalente a {cotacao} {para}")
else:
    print("Erro: moeda inválida.")
