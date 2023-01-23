#função para encontrar id a partir do nome
def encontrar_id(nome_escola, dicionario):
    for id, escola in dicionario.items():
        if escola['nome'] == nome_escola:
            return id

#dicionário com as escolas
escolas = {
    1:{'nome': 'Jesus de Nazaré', 'vagas': 3},
    2:{'nome': 'Mario Compagner', 'vagas': 4},
    3:{'nome': 'Helena Vaz', 'vagas': 2},
    4:{'nome': 'Cassiano Ricardo', 'vagas': 3},
    5:{'nome': 'Zenaide Vilalva', 'vagas': 1},
    6:{'nome': 'Benedito Carvalho', 'vagas': 2},
}

#dicionário com os cadastros
cadastros = {
    1:{'nome': 'Ana', 'classificacao': 75, 'opcao1': escolas[1]['nome'], 'opcao2': escolas[5]['nome'], 'opcao3': escolas[3]['nome']},
    2:{'nome': 'Gabriel', 'classificacao': 140, 'opcao1': escolas[1]['nome'], 'opcao2': escolas[2]['nome'], 'opcao3': escolas[3]['nome']},
    3:{'nome': 'Sarah', 'classificacao': 55, 'opcao1': escolas[4]['nome'], 'opcao2': escolas[6]['nome'], 'opcao3': escolas[2]['nome']},
    4:{'nome': 'Giovanna', 'classificacao': 215, 'opcao1': escolas[3]['nome'], 'opcao2': escolas[4]['nome'], 'opcao3': escolas[5]['nome']},
    5:{'nome': 'Eduardo', 'classificacao': 259, 'opcao1': escolas[5]['nome'], 'opcao2': escolas[3]['nome'], 'opcao3': escolas[1]['nome']},
    6:{'nome': 'Davi', 'classificacao': 80, 'opcao1': escolas[5]['nome'], 'opcao2': escolas[4]['nome'], 'opcao3': escolas[3]['nome']},
    7:{'nome': 'Maria', 'classificacao': 201, 'opcao1': escolas[4]['nome'], 'opcao2': escolas[6]['nome'], 'opcao3': escolas[1]['nome']},
    8:{'nome': 'Nicole', 'classificacao': 100, 'opcao1': escolas[6]['nome'], 'opcao2': escolas[3]['nome'], 'opcao3': escolas[1]['nome']},
    9:{'nome': 'Natalie', 'classificacao': 189, 'opcao1': escolas[4]['nome'], 'opcao2': escolas[2]['nome'], 'opcao3': escolas[6]['nome']}
}

#imprime as escolas cadastradas e vagas
print("Escolas cadastradas: ")
for id_escola, escola in escolas.items():
    print(f"{escola['nome']} | Vagas: {escola['vagas']}")

#organiza os cadastros do maior para o menor
cadastros_ordenado = sorted(cadastros.items(), key=lambda x: x[1]['classificacao'],reverse=True)

#lista vazia para incluir os resultados no final
resultados = list()

#laço que realiza o trabalho
for id_cadastro, cadastro in cadastros_ordenado:
    for opcao in ['opcao1', 'opcao2', 'opcao3']:
        nome_escola = cadastro[opcao]
        id = encontrar_id(nome_escola, escolas)

        if escolas[id]['vagas'] > 0:
            escolas[id]['vagas'] -= 1
            resultados.append(f"Concursado: {cadastro['nome']} - Escola: {nome_escola}")
            break

#impressão dos resultados
for resultado in resultados:
    print(resultado)
