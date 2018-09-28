##### FUNCOES PESQUISA ELEITORAL #####
import time, math, Pesquisa as P

def Guarda_MesG():      
      Totalv = (P.Candidato_a[0] + P.Candidato_b[0] + P.Candidato_c[0] + P.Candidato_d[0])
      ParcialP = float(Totalv/100)
      PorcenA = float(P.Candidato_a[0]/ParcialP)
      PorcenB = float(P.Candidato_b[0]/ParcialP)
      PorcenC = float(P.Candidato_c[0]/ParcialP)
      PorcenD = float(P.Candidato_d[0]/ParcialP)
      print("O Candidato Bolsonaro esta com",round((PorcenA),2),"% dos votos.")
      print("O Candidato Hadadd esta com",round((PorcenB),2),"% dos votos.")
      print("A Candidata Marina esta com",round((PorcenC),2),"% dos votos.")
      print("O Candidato Ciro Gomes esta com",round((PorcenD),2),"% dos votos.")
      print("Finalizada a pesquisa com",Totalv,"votos!")
      if P.MesG in P.Historico:
          del P.Historico[P.MesG]
          P.Historico.update({P.MesG:[PorcenA,PorcenB,PorcenC,PorcenD]})
          print(P.Historico)
      else:
          ("Ocorreu um erro inesperado , contate o Administrador do seu sistema!")

def Parcial_P():
      Totalv = (P.Candidato_a[0] + P.Candidato_b[0] + P.Candidato_c[0] + P.Candidato_d[0])
      ParcialP = float(Totalv/100)
      PorcenA = float(P.Candidato_a[0]/ParcialP)
      PorcenB = float(P.Candidato_b[0]/ParcialP)
      PorcenC = float(P.Candidato_c[0]/ParcialP)
      PorcenD = float(P.Candidato_d[0]/ParcialP)
      print("O Candidato Bolsonaro esta com",round((PorcenA),2),"% dos votos.")
      print("O Candidato Hadadd esta com",round((PorcenB),2),"% dos votos.")
      print("A Candidata Marina esta com",round((PorcenC),2),"% dos votos.")
      print("O Candidato Ciro Gomes esta com",round((PorcenD),2),"% dos votos.")
      print("Parcial total de",Totalv,"votos!")
      
def Busca_MesG():
      Pesquisa_M = P.Historico[P.BuscaG]
      print("O Candidato Bolsonaro esta com",round((Pesquisa_M[0]),2),"% dos votos.")
      print("O Candidato Hadadd esta com",round((Pesquisa_M[1]),2),"% dos votos.")
      print("A Candidata Marina esta com",round((Pesquisa_M[2]),2),"% dos votos.")
      print("O Candidato Ciro Gomes esta com",round((Pesquisa_M[3]),2),"% dos votos.")