lista = []
valida_loop = False
validasn = ("s","n")
while valida_loop == False:
   itemlista = input("Digite um item para adcionar a lista: ")
   valida_sn = False
### BLOCO PARA VALIDAR S OU N
   valida_sn = False
   while valida_sn == False:
      sn = input("Deseja continuar inserindo dados na lista? ('S' ou 'N'):").lower()
      if sn in validasn:
          if sn == "n":
              print("Programa Finalizado!")
              lista.append(itemlista)
              valida_sn = True
              valida_loop = True
          elif sn == "s":
              lista.append(itemlista)
              print("Sua lista é : ", lista)
              valida_sn = True
      elif sn not in validasn:
          print("As letras não são validas, digite (S ou N)" )
 ### FIM DO BLOCO DE VALIDACAO S OU N
print("Sua lista final é: ", lista )       
