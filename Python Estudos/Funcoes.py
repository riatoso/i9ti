##### MODULO DE FUNCOES DO PROJETO
import time, ProjetoTotal as main



def Func():
   ##### FUNÇÃO DE PREENCHER LISTA DE ATLETAS #####
   ### VALIDA DOS LAÇOS WHILE
   Valida_idade = False   ### VALIDA IDADE WHILE
   Valida_altura = False  ### VALIDA ALTURA WHILE
   ##############################
   print(10 * "-----")
   ### NOME VALIDAÇÃO
   NomeVal = str(input("NOME: "))
   Nome = NomeVal.title()
   main.Atleta.append(Nome)
   print(10 * "-----")
   ### IDADE VALIDAÇÃO ###
   while Valida_idade == False:
       Idade = input("IDADE: ")
       try:
          Idade = float(Idade)
          if Idade > 100 or Idade <= 0:
              print("Sua idade não pode ser menor ou igual a '0' ou maior que '100'.")
          else:
              main.Anos.append(Idade)
              Valida_idade = True
       except:
            print("Voce precisa digitar a idade com separação por '.' Ex: 32.2.")
   ### FIM DO VALIDA IDADE ###
   print(10 * "-----")
   ### VALIDA ALTURA WHILE
   while Valida_altura == False:
       Altura = input("ALTURA: ")
       try:
           Altura = float(Altura)
           if Altura <= 0.60 or Altura > 2.80:
               print("Voce não pode ser maior que '2.80 Cm' ou menor que '0.60 Cm'.")
           else:
               main.Cm.append(Altura)  
               Valida_altura = True
       except:
           print("Voce digitou sua altura errado. 'Ex: 1.98' sempre separado por '.'")
    ##### FIM DA FUNÇÃO DE PREENCHER #####

def MediaIdade():
    ##### FAZER A MEDIA DE IDADE DO TIME #####
    print(10 * "-----")
    time.sleep(3)
    print(10 * "-----")
    print("\n\033[43ricard;1mCALCULANDO MEDIA DE IDADE DO TIME >>>>")
    Tamanho = len(main.Anos)
    Soma = sum(main.Anos)
    MediaIdade = round((Soma/Tamanho),2)
    print("Seu time tem media de idade de:",MediaIdade,"anos.")
    print(10 * "-----")
    ##### FIM DO CALCULO DE MEDIA DE IDADE #####
    
def MediaAltura():
    ##### FAZER A MEDIA DE ALTURA DO TIME #####
    print(10 * "-----")
    time.sleep(3)
    print(10 * "-----")
    print("\n\033[42;1mCALCULANDO MEDIA DE ALTURA DO TIME >>>>")
    TamanhoAlt = len(main.Cm)
    SomaAlt = sum(main.Cm)
    MediaAlt = round((SomaAlt/TamanhoAlt),2)
    print("Seu time tem media de Altura de:",MediaAlt,"metros.")
    print(10 * "-----")
    ##### FIM DO CALCULO DE MEDIA DE IDADE #####
    
def BuscaAtleta():
    ##### VALIDA BUSCA DO ATLETA #####
    print(10 * "-----")
    Valida_busca = False
    while Valida_busca == False:
        Busca_Atleta1 = input("\33[34;1mDigite o nome do atleta para fazer a busca: ")
        Busca_Atleta = Busca_Atleta1.title()
        if Busca_Atleta in main.Atleta:
            indice = main.Atleta.index(Busca_Atleta)
            print(10 * "-----")
            print("O nome do atleta: ",main.Atleta[indice])
            print("Idade do atleta: ",main.Anos[indice])
            print("Altura do atleta: ",main.Cm[indice])
            print(10 * "-----")
            Valida_busca = True
        elif Busca_Atleta not in main.Atleta():
            print("Este atleta não esta cadastrado , ou foi digitado nome errado.")
        else:
            print("Ocorreu um erro desconhecido, tente novamente.")
    ##### FIM DO VALIDA BUSCA ATLETA #####



