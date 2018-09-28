#FAZER UM PROGRAMA QUE DIGITE O NOME DO ALUNO
# E DIGITE A NOTA DOS 4 BIMESTRES. DEPOIS FACA 
# A MEDIA SE FOR MAIOR QUE 6 APROVADO , SE FOR 
# ENTRE  5 E 5.9 RECUPERAÇÃO, ABAIXO DE 5.0 O
# ALUNO REPROVOU..USAR LAÇO DE REPETIÇÃO E VALIDAR
# AS NOTAS
import math,time,sys
print("\033[31;1m### PROGRAMA DE BOLETIM ###\n")
## VALIDA O INPUT DO CONTINUE: APENAS AS TECLAS S.N VALERAM.. QUALQUER OUTRA O PROGRAMA ACUSA
continua_valida = False
while continua_valida == False:
    continua = input("\033[34mDIGITE 'S' PARA CONTINUAR OU 'N': ").lower()
    if continua == ('s'):
        print("\nOK , VAMOS AO PROGRAMA\n")
        continua_valida = True
    elif continua == ('n'):
        print("\nOBRIGADO , ESTAMOS TERMINANDO O PROGRAMA\n")
        time.sleep(3)
        exit()
    else:
       print("\033\31m\nVOCE NÃO ESCOLHEU A OPCAO CERTA -- FAVOR ESCOLHER ('S ou N')\n")
## FIM DO VALIDA CONTINUE
print("\033[32;1mPRIMEIRO PONTO DE VERIFICAÇÃO ESTA OK\n")
time.sleep(3)
## NOTAS PARA VALIDAR ENTRE 0 A 10.0 COMO FLOAT , QUALQUER OUTRA VOLTA AO PROGRAMA
valida_nota = False
Nlista = []
while valida_nota == False:
   nota1 = input("DIGITE A NOTA DO 1o. BIMESTRE: ")
   nota2 = input("DIGITE A NOTA DO 2o. BIMESTRE: ")
   nota3 = input("DIGITE A NOTA DO 3o. BIMESTRE: ")
   nota4 = input("DIGITE A NOTA DO 4o. BIMESTRE: ")
   try:
      nota1 = float(nota1)
      nota2 = float(nota2)
      nota3 = float(nota3)
      nota4 = float(nota4)
      if (nota1 > 10) or (nota2 > 10) or (nota3 > 10) or (nota4 > 10):
          print("AS NOTAS DIGITADAS TEM QUE SER ENTRE 0 E 10")
      elif (nota1 < 0) or (nota2 < 0) or (nota3 < 0) or (nota4 < 0):
          print("VERIFIQUE AS NOTAS, TEM QUE SER ENTRE 0 E 10")
      else:
          valida_nota = True
   except:
      print("SUA DIGITAÇÃO DE NOTA ESTA ERRADA, DIGITE SÓ NUMEROS COM '.'.")
## FIM DA VALIDAÇÃO DAS NOTAS
Nlista.append(nota1)
Nlista.append(nota2)
Nlista.append(nota3)
Nlista.append(nota4)
Nsoma = sum(Nlista)
Nmedia = Nsoma / 4
if Nmedia >= 6:
    print("Voce foi aprovado com a media de %.2f" %Nmedia)
    print("PARABENS!")
elif (Nmedia >= 5) and (Nmedia < 6):
    print("Voce ficou de recuperação com a media de %.2f" %Nmedia)
else:
    print("FOI FOI MUITO MAL NAS NOTAS , BOMBOU COM MEDIA DE %.2f" %Nmedia)
            