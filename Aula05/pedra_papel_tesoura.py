# Jogo do Pedra Papel e tesoura interativo
import random

def escolhaHumano(playerchoice):
    print(" ")
    humano = "Você escolheu "
    if playerchoice == 1:
        print(humano + "Pedra.")
    elif playerchoice == 2:
        print(humano + "Papel.")
    else:
        print(humano + "Tesoura.")
        
def escolhaMaquina(computerchoice):
    maquina = "Python escolheu "
    if computerchoice == 1:
        print(maquina + "Pedra.")
    elif computerchoice == 2:
        print(maquina + "Papel.")
    else:
        print(maquina + "Tesoura.")
    print(" ")
    
def resultado(playerchoice, computerchoice, playerscore, computerscore):
    vitoriaMaquina = False;
    
    if playerchoice == computerchoice:
        print("😮 Empate")
        return playerscore, computerscore
    elif playerchoice == 1 and computerchoice == 2:
        vitoriaMaquina = True;
            
    elif playerchoice == 2 and computerchoice == 3:
        vitoriaMaquina = True;
    
    elif computerchoice == 1:
        vitoriaMaquina = True;
    
    if vitoriaMaquina:
        computerscore += 1
        print("🐍 Python ganhou!!!")
    else :
        playerscore += 1
        print("😁 Você ganhou!!!")
        
    return playerscore, computerscore
    
def pontuacao(playerscore, computerscore):
    print("Pontuação".center(31, "-"))
    print("Você:\t", playerscore)
    print("Python:\t", computerscore)
    print(" ")
        
print("PedraPapelTesoura".center(31, "="))
print(" ")
playerscore = 0
computerscore = 0

while 1:
    pontuacao(playerscore,computerscore)
    playerchoice = int(input("Insira:\n1 para Pedra,\n2 para Papel,\n3 para Tesoura ou\n4 para sair do programa:\n\n"))
    computerchoice = int(random.choice("123"))

    if playerchoice == 4:
        exit()
    elif (playerchoice < 1 or playerchoice > 3):
        print("Comando inválido, insira 1, 2 ou 3.")
        continue

    escolhaHumano(playerchoice)
    escolhaMaquina(computerchoice)
   
    playerscore, computerscore = resultado(playerchoice, computerchoice, playerscore, computerscore)