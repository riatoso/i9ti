### FUNCOES DE APLITATIVO DE TEMPO DE DIGITAÇÃO
import time

##### FUNCAO DE TEMPO 5 DIGITAÇÕES
def tempo():
    total = []
    while len(total) < 5:
        iniciot = time.clock()
        Valida_palavra = False
        while Valida_palavra == False:
           palavra = input("DIGITE A PALAVRA 'TEMPO' NO MENOR TEMPO POSSIVEL: ").lower()
           if palavra != ("tempo"):
              print("VOCE DIGITOU A PALAVRA ERRADA , TENTE NOVAMENTE")
              continue
           else:
               Valida_palavra = True
        fimt = time.clock()
        ttempo = round((fimt - iniciot),2)
        if ttempo >= 10.00:
            print("Seu tempo foi superior ou igual a '10s'")
            continue
        else:
            total.append(ttempo)
    return total
##### FIM DA FUNCAO DE TEMPO