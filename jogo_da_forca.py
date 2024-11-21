#importando biblioteca como RANDOM(oderns aleatórias) e OS(sistema para limpar a tela
import time
import os
import random

animais = ('elefante', 'tigre', 'canguru', 'girafa', 'coala', 'lobo', 'porco')
comidas = ('pizza', 'hamburguer', 'sushi', 'feijoada', 'parmegiana', 'lasanha', 'strogonoff')
objetos = ('telefone', 'caneta', 'caderno', 'mochila', 'relogio', 'cadeira', 'estojo')
paises = ('japao', 'brasil', 'alemanha', 'canada', 'italia', 'egito', 'noruega')
carros = ('fusca', 'ferrari', 'camaro', 'gol', 'mustang', 'porsche', 'celta')

while True:
    print('-='*20)
    print('JOGO DA FORCA'.center(40))
    print('-='*20)
    print("""
    [ 1 ] Animais
    [ 2 ] Comidas
    [ 3 ] Objetos
    [ 4 ] Países
    [ 5 ] Carros
    """)
    escolha_de_tema = input('Qual tema você deseja jogar? ')

    if escolha_de_tema.isalpha():
        voltar = input("Erro: Apenas números são permitidos. Tecle Enter para tentar novamente ")
        if voltar == "":
            os.system('cls')
            continue
        else:
            pass
    

    if escolha_de_tema == "1":
        palavra_secreta = random.choice(animais)
        tema = 'ANIMAIS'
    elif escolha_de_tema == "2":
        palavra_secreta = random.choice(comidas)
        tema = 'COMIDAS'
    elif escolha_de_tema == "3":
        palavra_secreta = random.choice(objetos)
        tema = 'OBJETOS'
    elif escolha_de_tema == "4":
        palavra_secreta = random.choice(paises)
        tema = 'PAÍSES'
    elif escolha_de_tema == "5":
        palavra_secreta = random.choice(carros)
        tema = 'CARROS'
    else:
        print('Escolha inválida...')
        voltar = input("Erro: Apenas números menores ou iguais a 5. Tecle Enter para tentar novamente ")
        if voltar == "":
            os.system('cls')
            continue
        else:
            pass

    os.system('cls')
    letras_acertadas = ''
    num_tentativas = 0
    erros = 0
    letras_usadas = []

    print(f"""
        JOGO DA FORCA DOS {tema}
    ____      
    |  |
    |
    |
    |
    |""")

    while True:
        if erros == 6:
            quer_jogar = input('Quer jogar novamente? [S/N]: ').lower()
            if quer_jogar == 's':
                print('Reiniciando jogo...')
                time.sleep(1)
                break
            elif quer_jogar == 'n':
                print('Obrigado por jogar!!!\nVolte Sempre....')
                os.system('cls')
        else:
            

            letra_digitada = input('\nDigite uma letra: ')
            num_tentativas += 1

            if letra_digitada.isnumeric():
                print(f'{letra_digitada} não é uma letra, digite apenas letras')
                continue

            if letra_digitada not in palavra_secreta:

                if letras_usadas == '':
                    letras_usadas = letra_digitada

                if letra_digitada in letras_usadas:
                    num_tentativas -= 1
                    print(f'Você já usou a letra {letra_digitada}')
                    continue
                else:
                    if len(letra_digitada) == 2:
                        print('Digite apenas UMA letra')
                        continue
                    else:
                        letras_usadas.append(letra_digitada)

        

            if letra_digitada == palavra_secreta:
                print('Você acertou antes da hora...')
                time.sleep(1)

            if len(letra_digitada) > 3 and letra_digitada != palavra_secreta:
                print('Você esgotou suas chances...')
                print(f'A palavra era: {palavra_secreta}')
                print('Obrigado por jogar!!!\nVolte Sempre....')
                time.sleep(2)
                os.system('cls')
                

            if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

        #estamos usando o palavra formada vazio abaixo para preencher com as palavras certas que o usuário responder 
            palavra_formada = ''
            #para cada letra na palavra secreta, nos queremos que se a palavra digitada pelo usuario estiver certa, ela deve entrar na variável palavra formada
            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_acertadas:
                    '''letra_secreta.replace(letra_secreta, letras_acertadas)'''
                    palavra_formada += letra_secreta
                else:
                    #aqui é onde substituimos o caractere _ pela letra correta que o usuário digitar
                    palavra_formada += ' _'
            if letra_digitada not in palavra_secreta:
                erros += 1
            os.system('cls')

            if erros == 0:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |
            |
            |
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 1:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            |
            |
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 2:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            |  |
            |
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 3:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            |  |
            | / 
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 4:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            |  |
            | / \\
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 5:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            |  |\\
            | / \\
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')

            elif erros == 6:
                print(f"""
                JOGO DA FORCA DOS {tema}
            ____      
            |  |
            |  O
            | /|\\
            | / \\
            |""")
                print('Letras usadas:', ', '.join(letras_usadas))
                print(f'Palavra formada: {palavra_formada}')



            if erros >= 6:
                time.sleep(1)
                os.system('cls')
                print('Acabou as suas chances...')
                print(f'A palavra era: {palavra_secreta}')
                

            if palavra_formada == palavra_secreta:
                os.system('cls') 
                print('\nParabéns, você acertou!!')
                print(f'A palavra era: {palavra_secreta}')
                print(f'Você tentou: {num_tentativas} vezes')
                quer_jogar = input('Quer jogar novamente? [S/N]: ').lower()
                if quer_jogar == 's':
                    print('Reiniciando jogo...')
                    time.sleep(1)
                    os.system('cls') 
                    exit()
                else:
                    print('Obrigado por jogar!!!\nVolte Sempre....')
                    os.system('cls')
                    exit()
