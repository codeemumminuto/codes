from time import sleep

def temporizador(tempo):
    while tempo >= 0:
        print(tempo)
        sleep(1)
        tempo -= 1
    print("O tempo acabou!!!")

tempo = int(input("Tempo em segundos: "))
temporizador(tempo)