import random

# Crei essa função porque este jogo faz parte de um conjunto de jogos que são ativados e importados por um "HUB" :)
def jogar():
    print("***************************************")
    print("Bem vindo ao nosso jogo de Adivinhação!")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 3
    tentativa = 1
    pontos = 1000

    print("Qual o nível de dificuldade que deseja jogar?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha:"))

    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    elif(nivel == 3):
        numero_de_tentativas = 5


    for tentativa in range(1, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, numero_de_tentativas))

        chute_str = input("Digite o seu numero entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 0 or chute > 100):
            print("Digite apenas numeros positivos entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        print("você digitou ", chute)

        if (acertou):
            print("Você acertou")
            print("Parabens, você fez {} pontos com {}º tentativas".format(pontos, tentativa))
            break
        else:
            if(maior):
                print("voce errou, seu chute foi maior que o numero secreto")
            elif(menor):
                print("voce errou, seu chute foi menor que o numero secreto")

        tentativa = tentativa + 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()