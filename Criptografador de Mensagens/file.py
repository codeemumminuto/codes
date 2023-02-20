alfabeto = "abcdefghijklmnopqrstuvwxyz"
criptografia = "qwertyuiopasdfghjklzxcvbnm"
erro = "0"

def criptografar(mensagem):
    mensagem_criptografada = ""
    for letra in mensagem:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            mensagem_criptografada += criptografia[indice]
        else:
            mensagem_criptografada += erro # prédio
    
    return mensagem_criptografada

def descriptografar(mensagem):
    mensagem_normal = ""
    for letra in mensagem:
        if letra in criptografia:
            indice = criptografia.index(letra)
            mensagem_normal += alfabeto[indice]
        else:
            mensagem_normal += letra
    
    return mensagem_normal

print("O que deseja fazer?")
print("1. Criptografar mensagem")
print("2. Descriptografar mensagem")
op = int(input("Escolha: "))

if op == 1:
    criptografada = input("Mensagem para criptografar: ").lower()
    print(criptografar(criptografada))
elif op == 2:
    descriptografada = input("Mensagem para descriptografar: ").lower()
    print(descriptografar(descriptografada))
else:
    print("Opção inválida")