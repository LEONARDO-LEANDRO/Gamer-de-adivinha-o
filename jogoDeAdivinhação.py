import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = random.randrange(1,101)
#print(numeroSecreto)

#Definindo o número de tentativas
numeroTentativas = 0
rodada = 1
pontuação = 1000

print('Qual o nível de dificuldade?')
print('(1)- Fácil, (2)- Médio, (3)- Difícil, (4)- Hardcore')

nivel = int(input("Defina um nível:"))

#Vamos mudar o número de tentativas  conforme a dificuldade

if(nivel == 1):
    numeroTentativas = 20

elif(nivel == 2):
    numeroTentativas = 15

elif(nivel == 3):
    numeroTentativas = 10
elif(nivel == 4):
    numeroTentativas = 5

else:
    numeroTentativas = 2
    print('Incompleto')

while(rodada <= numeroTentativas):
    print('Você tem somente algumas chances -->' ,numeroTentativas,', Não desperdice, verme insolente!!')
    
    
#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou! E sua pontuação foi: ', pontuação)
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
    pontos_perdidos = abs(numeroSecreto - chute)
    pontuação = pontuação - pontos_perdidos
    numeroTentativas -= 1
    #numeroTentativas = numeroTentativas-1
    rodada = rodada +1

#Aula Elif 26.02.24
