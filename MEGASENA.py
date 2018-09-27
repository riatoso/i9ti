import time , random

### CORES
vermelho = '\033[31m'
verde = '\033[32m'
fim = '\033[0;0m'

def sorteio():
    mega = []
    num1 = random.randint(1,60)
    mega.append(num1)
    print(10*"*****")
    print("Bola numero 1 -> Numero:",num1)
    print(10*"*****")
    
    ### SORTEIO BOLA 2 - VERIFICA ###
    print("\nSORTEIOOOO BOLAAAAAA 2.... AGUARDE.")
    time.sleep(2)
    verifica_num2 = False
    while verifica_num2 == False:
        num2 = random.randint(1,60)
        if num2 in mega:
            continue
        else:
            mega.append(num2)
            verifica_num2 = True
    print("Bola numero 2 -> Numero:",num2)
    print(10*"*****")

    ### SORTEIO BOLA 3 - VERIFICA ###
    print("\nSORTEIOOOO BOLAAAAAA 3.... AGUARDE.")
    time.sleep(2)
    verifica_num3 = False
    while verifica_num3 == False:
        num3 = random.randint(1,60)
        if num3 in mega:
            continue
        else:
            mega.append(num3)
            verifica_num3 = True
    print("Bola numero 3 -> Numero:",num3)
    print(10*"*****")

    ### SORTEIO BOLA 4 - VERIFICA ###
    print("\nSORTEIOOOO BOLAAAAAA 4.... AGUARDE.")
    time.sleep(2)
    verifica_num4 = False
    while verifica_num4 == False:
        num4 = random.randint(1,60)
        if num4 in mega:
            continue
        else:
            mega.append(num4)
            verifica_num4 = True
    print("Bola numero 4 -> Numero:",num4)
    print(10*"*****")

    ### SORTEIO BOLA 5 - VERIFICA ###
    print("\nSORTEIOOOO BOLAAAAAA 5.... AGUARDE.")
    time.sleep(2)
    verifica_num5 = False
    while verifica_num5 == False:
        num5 = random.randint(1,60)
        if num5 in mega:
            continue
        else:
            mega.append(num5)
            verifica_num5 = True
    print("Bola numero 5 -> Numero:",num5)
    print(10*"*****")

    ### SORTEIO BOLA 6 - VERIFICA ###
    print("\nSORTEIOOOO BOLAAAAAA 6.... AGUARDE.")
    time.sleep(2)
    verifica_num6 = False
    while verifica_num6 == False:
        num6 = random.randint(1,60)
        if num6 in mega:
            continue
        else:
            mega.append(num6)
            verifica_num6 = True
    print("Bola numero 6 -> Numero:",num6)
    print(10*"*****")

    
    mega.sort()
    return mega

sorteado = sorteio()

print(verde+"\nA MEGASENA SORTEOU:",sorteado,fim)
