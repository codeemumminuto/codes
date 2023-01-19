import bitly_api
 
TOKEN_ACESSO_BITLY ="SEU TOKEN DE ACESSO AQUI"
conexao = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

encurtado = conexao.shorten("https://tiktok.com")
print(f"Link encurtado: {encurtado}")