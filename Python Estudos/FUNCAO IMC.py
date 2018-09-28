# FUNÇOES PARA CALCULAR IMC

##### FUNCAO DE CORES #####
def cores(cor):
    vermelho = "\033[31m"
    verde = '\033[32m'
    azul = '\033[34m'
    ciano = '\033[36m'
    magenta = '\033[35m'
    amarelo = '\033[33m'
    return cor


print(cores(amarelo)+"TESTE DE CORE")
##### FIM DA FUNCA DE CORES #####

##### VALIDA SEXO #####
Valida_sexo = False
while Valida_sexo == False:
   Sexosn = ("m","f")
   Sexo = input("DIGITE SEU SEXO (M OU F): ").lower()
   if (Sexo in Sexosn) and Sexo == "f":
      print("Voce é Mulher")
      Valida_sexo = True
   elif (Sexo in Sexosn) and Sexo == "m":
      print("Voce é Homem")
      Valida_sexo = True
   else:
      print("VOCE DIGITOU ALGO ERRADO")
#### FIM VALIDA SEXO #####
      
##### VALIDA PESO #####
Valida_peso = False
while Valida_peso == False:
    Peso = input("DIGITE SEU PESO: ")
    try:
        Peso = float(Peso)
        if Peso <= 0:
            print("SEU PESO DEVE SER MAIOR QUE ZERO")
        else:
            Valida_peso = True
    except:
        print("VOCE DIGITOU SEU PESO ERRADO, O DECIMAL É '.'.")
##### FIM DO VALIDA PESO #####

##### VALIDA ALTURA #####
Valida_alt = False
while Valida_alt == False:
    Altura = input("DIGITE SEU ALTURA: ")
    try:
        Altura = float(Altura)
        if Altura <= 0 or Altura >= 2.60:
            print("SUA ALTURA DEVE SER MAIOR QUE ZERO E MENOR QUE '2,60'")
        else:
            Valida_alt = True
    except:
        print("VOCE DIGITOU SEU ALTURA ERRADA, O DECIMAL É '.'.")
##### FIM DO VALIDA ALTURA #####                
print(Sexo,Peso,Altura)

##### FUNCAO PARA CALCULAR IMC #####
def imc(Sexo,Peso,Altura):
   imc_calc = (Peso / (Altura  * Altura))
   ### se for homem ###
   if Sexo == "m":
      if imc_calc >= 31.1:
         return("VOCE É HOMEM E ESTA OBESO")
      elif imc_calc >= 20.7 and imc_calc <= 26.4:
         return("VOCE É HOMEM E ESTA NO SEU PESO NORMAL")
      elif imc_calc >= 27.7 and imc_calc <= 31:
          return("VOCE ESTA ACIMA DO PESO")
      else:
          return("ERRO INESPERADO")
   ### se for mulher ###
   if Sexo == "f":
      if imc_calc >= 31.1:
         return("VOCE É MULHER E ESTA OBESA")
      elif imc_calc >= 20.7 and imc_calc <= 26.4:
         return("VOCE É MULHER E ESTA NO SEU PESO NORMAL")
      elif imc_calc >= 27.7 and imc_calc <= 31:
          return("VOCE É MULHER E ESTA ACIMA DO PESO")
      else:
          return("ERRO INESPERADO")
##### FUNCAO IMC FINALIZADO #####

imcalc = imc(Sexo,Peso,Altura)
print(imcalc)