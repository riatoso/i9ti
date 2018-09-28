#VALIDACAO
##################
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