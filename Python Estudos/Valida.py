#VALIDACAO
print("\033[92;1m####### VALIDA FLOAT #########\033[0m\n")
valida_num = False
while valida_num == False:
   flut = input("Digite um número P. Flutuante: ")
   try: 
      flut = float(flut)
      if flut <= 0:
         print("DIGITE UM NÚMERO MAIOR QUE ZERO")
      else:
         valida_num = True
   except:
       print("DIGITE COM '.' E NAO ',' E APENAS NÚMEROS")
print(flut)

print("\n\033[92;1m####### VALIDA FLOAT #########\033[0m\n")
valida_nota = False

while valida_nota == False:
   nota = input("DIGITE SUA NOTA: ")
   try:
      nota = int(nota)
      if nota < 0 or nota > 100:
         print("SUA NOTA TEM QUE SER ENTRE 0 E 100")
      else:
         valida_nota = True
   except:
      print("DIGITE APENAS NÚMEROS ,SEM PONTO")
      
print("SUA NOTA FOI:",nota)
###############TRECHO TODO DE VALIDAÇÃO ################# 