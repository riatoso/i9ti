#EXERCICIOS DE FUNÇÃO

#1) Escreva um algoritmo que contenha uma função de nome estudo() e que quando executada imprima na saída padrão a frase "Estamos estudando as funções":
"""def estudo():
    print("ESTAMOS ESTUDANDO AS FUNÇOES")

estudo()
print(20 * "---")
#2) Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber um número como argumento. Chame este argumento de x. No corpo da função imprima a seguinte frase na tela: "Função invocada com sucesso. O valor passado pelo argumento x é: <valor de x>"
def valox(x):
    return x
y = valox(45)
print("Estamos passando um valor de x que sera:", y)
print(20 * "---")
#3) Escreva um algoritmo que receba dois números através da declaração de dois parâmetros cujos nomes serão: x e y. No bloco de instrução faça a soma de ambos valores e imprima o resultado no monitor:
def soma(x,y):
    somas = (x + y)
    return somas
z = soma(23,45)
print("A soma de x e y é igual:", z)"""
print(20 * "---")
#4) Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:
def arit(x,y,t):
    lista = [x,y,t]
    lista.sort()
    media = round((x+y+t)/(len(lista)),2)
    """print("Sua lista em ordem crescente é:",lista)
    print("A media aritimetica é:",media)"""
    return ("Lista",lista),("media",media)

print(arit(2,6,3))
print(20 * "---")
#5) Escreva uma função que contenha dois parâmetros. O primeiro deve ser obrigatório e o segundo facultativo:

#6) Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos. Invoque a primeira função de ``func1()`` e a segunda de ``func2()``. Em seguida, invoque os parâmetros da segunda função de x e y. Some x e y e retorne o resultado. Em func1(), ao receber o resultado, retorne-o também como valor de retorno da função. Por fim, imprima na tela o valor que foi calculado por func2(), retornado para func1() e retornado a quem invocou a função inicialmente:

#7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. Em seguida, imprima os parâmetros recebidos na tela:

#8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:

#9) Considere o trecho de código a seguir.

#def func(a, b, c, d)
#    print(a+b+c+d)
#lista = 1,2,3,4
#Invoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:

#10) Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.

#11) Escreva um função que some todos os números contidos numa lista.
#Lista: (1, 2, 3, 4, 5)
#Soma: 15

#12) Escreva uma função que multiplique todos os números de uma lista.
#Lista: (1, 2, 3, 4, 5)
#Multiplicação: 120

def multiplica(a,b,c,d,e):
    xin = (a*b*c*d*e)
    return xin
print(multiplica(1,2,3,4,5))
print(20 * "---")
    


#13) Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. Não utilize a função interna do Python que faz inverção, crie o algoritmo que faça a inversão.
#Lista: "1234abcd"
#Saída: "dcba4321"

#14) Escreva uma função que calcule o fatorial de um número (um inteiro não negativo). Envie o valor do número que será calcula como argumento da função.

#15) Escreva uma função que verifique se um número está num intervalo determinado.

#16) Escreva uma função que aceite Strings e calcule a quantidade de letras em mauisculas e minúsculas que a String possui.

#17) Escreva uma função que receba como argumento uma lista que poderá ter valores duplicados e retorne uma nova lista sem que haja valores iguais.
#Lista: [1,2,3,3,3,3,4,5]
#Retorno: [1, 2, 3, 4, 5]

#18) Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e imprima na telas os números primos contidos nessa lista.

#19) Escreva uma função que imprima somente os números pares
#Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Saída: [2, 4, 6, 8]

lista_impares = []
def pares(*lista):
    lista_num = [1,2,3,4,5,6,7,8,9,10]
    global lista_impares    
    lista_pares = []
    for x in lista_num:
        if x % 2 == 0:
            lista_pares.append(x)
        else:
            lista_impares.append(x)
    return lista_pares

listani = lista_impares
listanp = pares()
print("Sua lista de numeros pares é :", listanp)
print("Sua lista de numeros impares é:", listani)
print(20 * "---")

#20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

def palin(*pd):
    lpd = []
    pld = input("DIGITE UMA PALAVRA: ")
    if pld == pld[::-1]:
        lpd.append(pld)
    else:
        pass
    return lpd

xin = palin()
if xin == []:
    print("NÃO É PALINDROMO.")
else:
    print(xin[0],"É PALINDROMO.")
print(20 * "---")
#21) Escreva uma função que tenha definida uma função em seu escopo. Invoque a função aninhada, retorne algum valor, imprima esse valor na tela e finalize a aplicação.
