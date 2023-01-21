import requests
from bs4 import BeautifulSoup

# Realizando requisição ao Google
pesquisar = "Como programar em python"
quant_resultados = "4"

url = f"https://www.google.com/search?q={pesquisar}&num={quant_resultados}"
response = requests.get(url)

# Analisar o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Puxar todas as DIVs de resultados
titulos = soup.find_all('h3')

# Imprimir os resultados
for titulo in titulos:
    print(titulo.text)