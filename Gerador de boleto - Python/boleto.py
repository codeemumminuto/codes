from pagseguro import PagSeguro

# Configuração do PagSeguro
pagseguro = PagSeguro(email="SEU_EMAIL", token="SEU_TOKEN")

# Dados do boleto
dados = {
    'valor': '100.00',
    'data_vencimento': '2022-12-31',
    'nome': 'João da Silva',
    'cpf': '12345678999',
    'telefone': '1112345678',
    'email': 'cliente@email.com',
    'endereco': {
        'cep': '12345678',
        'rua': 'Rua teste',
        'numero': '123',
        'bairro': 'Bairro teste',
        'cidade': 'São Paulo',
        'estado': 'SP'
    }
}

# Criação do boleto
boleto = pagseguro.boleto(**dados)

# Verificação do status do pagamento
status = boleto["status"]

# Notificação do cliente ou atualização do status do boleto
if status == "Aprovado":
    print("Pagamento aprovado")
else:
    print("Pagamento não aprovado")
