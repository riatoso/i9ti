import time, Funcoes as ff, math

Atleta = []
Anos = []
Cm = []

ff.Func()

while True:
   print(10 * "-----")
   sn = ("s","n")
   Continua = input("CONTINUA (S,N):").lower()
   if Continua in sn and Continua == "s":
      ff.Func()
   elif Continua in sn and Continua == "n":
      break
   else:
      print("Voce digitou a tecla errada. Apenas 's' ou 'n'.")


print("Lista de Atletas: ",Atleta)
print("Lista de Idade: ",Anos)
print("Lista de Altura: ",Cm)

##### VALIDA OPCAO MEDIAS ##### 
print(10 * "-----")
#Valida_Medias = False
while True:
    mai = ("mi","ma","s")
    Escolha = input("\n\nEscolha uma opção!\n"+(6 * "----")+"\n\33[31;1m·Media Idade = MI\n·Media Altura = MA\n·Sair = S\n·OPÇÃO:").lower()
    if Escolha in mai and Escolha == "mi":
        ff.MediaIdade()
    elif Escolha in mai and Escolha == "ma":
        ff.MediaAltura()
    elif Escolha in mai and Escolha == "s":
        break
    else:
        print("Digite uma opção valida , conforme os exemplos!")
##### VALIDA OPCAO MEDIAS FIM #####
        
##### PROCURA POR ATLETA #####
BuscaA = ("s","n")
BuscaS = input("Deseja fazer uma procura por atleta no banco de dados ('S' ou 'N'): ").lower()
if BuscaS in BuscaA and BuscaS == 's':
    ff.BuscaAtleta()
elif BuscaS in BuscaA and BuscaS == 'n':
    print("Estamos finalizando o sistema.")
else:
    print("Voce digitou as opções erradas.")
    
print(10 * "■-■-■")
        
