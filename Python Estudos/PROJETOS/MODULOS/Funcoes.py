### Modulo de Funcoes###
import random, time

def Megasena():
    MegaS = []
    while len(MegaS) < 6:
        Sorteio = random.randint(1,60)
        if Sorteio in MegaS:
            continue
        else:
            MegaS.append(Sorteio)
    Mega = sorted(MegaS)
    return Mega
        
def Tempo():
    inicio = time.clock()
    input("DIGITE SEU NOME NO MENOR TEMPO POSSIVEL: ")
    fim = time.clock()
    Ttotal = round((fim - inicio),2)
    return Ttotal

print(Tempo())