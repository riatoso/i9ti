#Programa MegaSena
import random, time
mg = 0
laposta = []
while mg < 6:
   aposta = int(input("Digite um número de 1 a 60: "))
   laposta.append(aposta)
   mg += 1
   
print("\nSua oposta:",  laposta[0],"-",laposta[1],"-",laposta[2],"-",laposta[3],"-",laposta[4],"-",laposta[5],"\n")

print("\033[34;4;1mSORTEIO COMEÇANDO EM 5 SEGUNDOS\n\033[0m")
time.sleep(5)

resulista = []
sorteio = 0
while sorteio < 6:
   numsort = random.randint(1,60)
   if numsort not in resulista:
      resulista.append(numsort)
      sorteio += 1
      
print("\n\033[092;1mSORTEIO:",  resulista[0],"-",resulista[1],"-",resulista[2],"-",resulista[3],"-",resulista[4],"-",resulista[5],"\n")

print("\033[34;4;1mCHECANDO RESULTADO EM 5 SEGUNDOS\n\033[0m")
time.sleep(5)

acertos = []
if laposta[0] in resulista:
   acertos.append(laposta[0])
elif laposta[1] in resulista:
   acertos.append(laposta[1])
elif laposta[2] in resulista:
   acertos.append(laposta[2])
elif laposta[3] in resulista:
   acertos.append(laposta[3])
elif laposta[4] in resulista:
   acertos.append(laposta[4])
elif laposta[5] in resulista:
   acertos.append(laposta[5])
else:
   print("NENHUM ACERTO")
   

print("\033[92;1mACERTOU OS NÚMEROS:", acertos)
