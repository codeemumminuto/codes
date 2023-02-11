from random import randint

continua = True
wins = 0
loss = 0

print("=== ADIVINHE O NÚMERO === ")

while continua:
    aleatorio = randint(1,5)
    tentativas = 3
    while tentativas > 0:
        escolha = int(input("Digite um número: "))
        if escolha == aleatorio:
            wins += 1
            print("Parabéns! Você acertou!")
            x = input("Deseja continuar para o próximo número? S/N: ")
            continua = True if x.upper() == "S" else False
            break
        else:
            tentativas -= 1
            if tentativas == 0:
                loss += 1
                x = input("Acabaram as tentativas, deseja continuar? S/N: ")
                continua = True if x.upper() == "S" else False
            else:
                print(f"Você errou :(. {tentativas} tentativas restantes")
    print(f"PLACAR = WINS: {wins} X LOSSES: {loss}")
        