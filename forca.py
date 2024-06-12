def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    
    #Definir qual a palavra secreta
    palavraSecreta = "feijao"

    enforcou = False
    acertou = False

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavraSecreta:
            if(chute.upper() == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1