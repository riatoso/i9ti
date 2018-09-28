# FATURA CARTÃO
import time, math
prodic = {}
while True:
   adicionar = input("Quer acrescentar um produto 's' ou 'n': ").lower()
   if adicionar == ("n"):
      print("PROGRAMA FINALIZADO")
      total = 0
      prod = prodic.keys()
      valor = prodic.values()
      
      for item in prodic:
         total = sum(valor)
         print("SUAS COMPRAS: ",item, "R$",prodic[item])
      print("GEROU UM TOTAL DE: ",total,"R$")
      break
   else:
      produto = str(input("Produto: "))
      preco = float(input("Preço: "))
      prodic.update({produto:preco})
      print("SUBTOTAL: ",prodic)

   
