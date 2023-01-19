import pandas as pd

pessoas = [
    {"Name": "Pessoa1", "Idade": 99, "Contato": "cont@cont.com"},
    {"Name": "Pessoa2", "Idade": 99, "Contato": "cont@cont.com"},
    {"Name": "Pessoa3", "Idade": 99, "Contato": "cont@cont.com"},
    {"Name": "Pessoa4", "Idade": 99, "Contato": "cont@cont.com"},]

df = pd.DataFrame(data=pessoas)

df.to_excel("pessoas.xlsx", index=False)
print("Conversão realizada com sucesso!")