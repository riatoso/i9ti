##### CORPO DE EXECUÇÃO DO PROGRAMA TEMPO 5X
import time, Modulo as tt, matplotlib.pyplot as mtlib
Digitados = [1,2,3,4,5]
lista = (tt.tempo())
#grafico = mtlib.plot(Digitados,tt.tempo())
print("Seus melhores 5 tempos foram: ", lista)

## GERA GRAFICO
print("\n\033[34mGERANDO O GRAFICO\n")
time.sleep(4)
leg = ['1 Dig','2 Dig','3 Dig','4 Dig','5 dig']
mtlib.xticks(Digitados,leg)
mtlib.plot(legenda,lista)
