
### JOGA DA FORCA ###
### PALAVRA A SER DESCOBERTA ###
def palavra():
    psc = input("Digite a palavra a ser descoberta: ").upper().strip()
    return psc
### LETRA A SER DESCOBERTA
def letra_teste():
    teste = False
    while teste == False:
        letra = input("Digite a Letra para testar o jogo: ").upper()
        if len(letra) == 1:
            teste = True
        else:
            print("Digite apenas uma letra!")
            continue
    return letra

def jogo_final():
    palavra_tamanho = palavra() # TAMANHO DA PALAVRA E A PROPRIA PALAVRA
    descoberto = [] # ( "-") QUE PRENCHE A PALAVRA
    ### PREENCHO A STRING DESCOBERTO COM O TAMANHO TOTAL DE CRS
    for i in range(0, len(palavra_tamanho)):
       descoberto.append("-")
       ## FIM DO PREENCHIMENTO
    tentativas = 0
    while tentativas <= 3:
        letra_format = letra_teste() # LETRA DA PALAVRA
        if letra_format in palavra_tamanho:
            for x in range(0, len(palavra_tamanho)):
                if letra_format == palavra_tamanho[x]:
                    descoberto.pop(x)
                    descoberto.insert(x, letra_format)
            if "-" in descoberto:
                print("AINDA NÃO DESCOBRIU A PALAVRA!!!")
                print("Sim sua palavra tem a letra : %s."%letra_format)
                print("Sua palavra esta assim: " , descoberto)
                continue
            else:
                print("PARABENS DESCOBRIU A PALAVRA","\033[1;31m" , descoberto)
                break
        else:
            print("Letra não existe!")
            faltante = (3 - tentativas)
            print("Voce tem ainda %i tentativas."%faltante)
            tentativas += 1
    return palavra_tamanho,letra_format,descoberto
print(jogo_final())