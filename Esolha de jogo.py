import Adivinhação
import Forca

print("***************************************")
print("**********O que deseja jogar?**********")
print("***************************************")

print("(1) Jogo de Advinhação (2) Jogo da Forca")
jogo = int(input("Escolha:"))

if(jogo == 1):
    print("Jogando Adivinhação")
    Adivinhação.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    Forca.jogar()
else:
    print("Escolha o jogo pelo seu determinado numeral")


