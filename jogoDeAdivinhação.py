import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = random.randrange(1,101)
#print(numeroSecreto)

#Definindo o número de tentativas
numeroTentativas = 10
rodada = 1

print('Qual o nível de dificuldade?')
print('(1)- Fácil, (2)- Médio, (3)- Difícil, (4)- Hardcore')

nivel = int(input("Defina um nível:"))

while(rodada <= numeroTentativas):
    print('Você tem somente algumas chances -->' ,numeroTentativas,', Não desperdice, verme insolente!!')
    print('Tentativa', rodada, 'de' , numeroTentativas)
    
#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')

    #numeroTentativas = numeroTentativas-1
    rodada = rodada +1
#Aula Elif 26.02.24
