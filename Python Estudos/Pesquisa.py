### PROGRAMA DE PESQUISA ELEITORAL
import time, math, FuncPesquisa as F

Candidato_a = [0]
Candidato_b = [0]
Candidato_c = [0]
Candidato_d = [0]
Historico = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

while True:
   print(14 * "·■·■·")
   Escolha_Cand = input("""Digite ('a' - Bolsonaro') ou ('b' - Haddad) ou ('c' - Marina) ou ('d' - Ciro)
                        \n\33[31m···('P') Parcial.\n···('M') Busca Pesquisa Antiga por Mes. Ex: 02\n···('S') Sair.\n···('G') Guardar e Sair.\n··· Sua opção: \033[0m""").lower()
   print(14 * "·■·■·")
   if Escolha_Cand == 's':
      print("Pesquise Finalizada\n")
      print("\33[35mO candidato Jair Bolsonaro esta com",Candidato_a[0],"votos","\nO candidato Hadadd ficou com",Candidato_b[0],"votos!","\nA candidata Marina Silva ficou com",Candidato_c[0],"votos!"
            "\nO candidato Ciro Gomes ficou com",Candidato_d[0],"votos!")
      break
   elif Escolha_Cand == "a":
      Candidato_a[0] += 1
      print("\033[34mBolsonaro esta com",Candidato_a[0],"votos\033[0m!!!")
   elif Escolha_Cand == "b":
      Candidato_b[0] += 1
      print("\033[34mFernando Hadadd esta com",Candidato_b[0],"votos\033[0m!!!")
   elif Escolha_Cand == "c":
      Candidato_c[0] += 1
      print("\033[34mMarina Silva esta com",Candidato_c[0],"votos\033[0m!!!")
   elif Escolha_Cand == "d":
      Candidato_d[0] += 1
      print("\033[34mCiro Gomes esta com",Candidato_d[0],"votos\033[0m!!!")
   elif Escolha_Cand == "p":
      F.Parcial_P()
      
   elif Escolha_Cand == "g":
       ### Valida mes
       Valida_MesG = False
       while Valida_MesG == False:
           MesG = input("Digite o numero do mes da pesquisa para ser arquivada (Ex 01 -> Janeiro), ou Digite 13 para Sair: ")
           try:
              MesG = int(MesG)
              if MesG >= 1 and MesG <= 12:
                  F.Guarda_MesG()
              elif MesG == "13":
                  continue
              else:
                  print("Mes tem que estar entre 1 e 12.")
                  Valida_MesG = True
           except:
               print("Voce digitou algo errado , verifique e redigite.")
         ### fim do valida mes     
   elif Escolha_Cand == "m":
      Valida_BuscaG = False
      while Valida_BuscaG == False:
          BuscaG = input("Digite o numero do mes da pesquisa para ser desarquivada! (Ex 01 -> Janeiro), ou Digite 13 para Sair: ")
          try:
              BuscaG = int(BuscaG)
              if BuscaG >= 1 and BuscaG <= 12:
                  F.Busca_MesG()
              elif BuscaG == "13":
                  continue
              else:
                  print("Erro. Mes tem que estar entre 1 e 12.")
                  Valida_BuscaG = True
          except:
             ### Valida_BuscaG = False
              print("Voce digitou algo errado , verifique e redigite.")
