import time , random

### CORES
vermelho = '\033[31m'
verde = '\033[32m'
fim = '\033[0;0m'

### JOGO FEITO PELO USUARIOS
nums_externo = []
### FIM

def jogo():
    jogo_ativo = []
    ### VALIDA A DEZENA 1 ###
    print(10*"*****")
    valida_ap1 = False
    while valida_ap1 == False:
        num1 = int(input("DIGITE A 1ª DEZENA DO JOGO: "))
        try:
            num1 = int(num1)
            if num1 > 60 or num1 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            else:
                print("Dezena 1 , Boa sorte.")
                jogo_ativo.append(num1)
                valida_ap1 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 1
    
    ### VALIDA A DEZENA 2 ###
    print(10*"*****")
    valida_ap2 = False
    while valida_ap2 == False:
        num2 = int(input("DIGITE A 2ª DEZENA DO JOGO: "))
        try:
            num2 = int(num2)
            if num2 > 60 or num2 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            elif num2 in jogo_ativo:
                    print("Esta Dezena ja esta marcada, marque outra!")       
            else:
                print("Dezena 2 , Boa sorte.")
                jogo_ativo.append(num2)
                valida_ap2 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 2
    
    ### VALIDA A DEZENA 3 ###
    print(10*"*****")
    valida_ap3 = False
    while valida_ap3 == False:
        num3 = int(input("DIGITE A 3ª DEZENA DO JOGO: "))
        try:
            num3 = int(num3)
            if num3 > 60 or num3 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            elif num3 in jogo_ativo:
                print("Esta Dezena ja esta marcada, marque outra!") 
            else:
                print("Dezena 3 , Boa sorte.")
                jogo_ativo.append(num3)
                valida_ap3 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 3

    ### VALIDA A DEZENA 4 ###
    print(10*"*****")
    valida_ap4 = False
    while valida_ap4 == False:
        num4 = int(input("DIGITE A 4ª DEZENA DO JOGO: "))
        try:
            num4 = int(num4)
            if num4 > 60 or num4 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            elif num4 in jogo_ativo:
                print("Esta Dezena ja esta marcada, marque outra!") 
            else:
                print("Dezena 4 , Boa sorte.")
                jogo_ativo.append(num4)
                valida_ap4 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 4

    ### VALIDA A DEZENA 5 ###
    print(10*"*****")
    valida_ap5 = False
    while valida_ap5 == False:
        num5 = int(input("DIGITE A 5ª DEZENA DO JOGO: "))
        try:
            num5 = int(num5)
            if num5 > 60 or num5 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            elif num5 in jogo_ativo:
                print("Esta Dezena ja esta marcada, marque outra!") 
            else:
                print("Dezena 5 , Boa sorte.")
                jogo_ativo.append(num5)
                valida_ap5 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 5

    ### VALIDA A DEZENA 6 ###
    print(10*"*****")
    valida_ap6 = False
    while valida_ap6 == False:
        num6 = int(input("DIGITE A 6ª DEZENA DO JOGO: "))
        try:
            num6 = int(num6)
            if num6 > 60 or num6 < 1:
                print("A Dezena não pode ser menor que 1 , ou maior que 60!")
            elif num6 in jogo_ativo:
                print("Esta Dezena ja esta marcada, marque outra!") 
            else:
                print("Dezena 6 , Boa sorte.")
                jogo_ativo.append(num6)
                valida_ap6 = True
        except:
            print("Voce digitou algo errado!")
    print(10*"*****")
    ### FIM DO VALIDA DEZENA 3

    global nums_externo
    nums_externo = jogo_ativo
    
    return jogo_ativo
    
    
######################################### SEPARA FUNCOES #####


### NUMEROS SORTEADOS NA MEGASENA
mega_externo = []
### FIM

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
    global mega_externo
    mega_externo = mega
    
    return mega

############################################# RODA OS SCRIPTS
aposta = jogo()
sorteado = sorteio()
print(aposta)
print(verde+"\nA MEGASENA SORTEOU:",sorteado,fim)
### FIM

############################################# COMPARA JOGOS

def confere():
    
    global mega_externo, nums_externo
    acertos = []
    for numero in nums_externo:
        if numero in mega_externo:
            acertos.append(numero)
        else:
            continue
    return acertos

print(10*"*****")
print("CALCULANDO ACERTOS!!!")
time.sleep(5)
total_a = confere()
print("Voce acertou os seguinte numeros: ",total_a)
