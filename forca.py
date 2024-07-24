def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    
    #Definir qual a palavra secreta
    palavraSecreta = "feijao"

    letras_acertadas = ["_""_""_""_"]

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavraSecreta:
            if(chute.upper() == letra):
               letras_acertadas[index] = letra
            index += 1
            
        else:
            erros = erros + 1

            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

            print("Escolha outra letra!")

        if(acertou):
            print("Você acertou!")
        else:
            print("Você errou!")

        print("Fim de Jogo!")