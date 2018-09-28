#-*-coding:utf8;-*-
#qpy:3
#qpy:console
cores = {"azul":"blue", "vermelho":"red", 
         "amarelo":"yellow", "roxo":"purple",
         "verde":"green"}
while True:
   cor1 = input("Digite o nome da cor em PT/BR: ")
   traduz = cores.get(cor1)
   if traduz == None:
      print("nao tem no dicionário")
   else:
      print(traduz)
      break
nova = input("Digite a cor em PT/BR: ")
new = input ("Digite a cor ingles: ")
cores.update({nova:new})
print("\nSua cores sao: --")
for x in cores:
   print("\33[33mAs cores no dic sao:", x)
while True:
   apagar = input("Digite a cor que deseja apagar, ou s para sair: ")
   if apagar == ("s"):
      print("Finalizado")
      break
   else:
      del cores[apagar]
      print("Suas cores agora: ", cores)