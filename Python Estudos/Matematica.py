#MODULO MATH
import math
x = 1
while x < 50:
      a = x
      raiz = math.sqrt(a)
      potencia = math.pow(a, 2)
      print("\033[092;1;5mA raiz de", x ,"é %.2f" %raiz)
      print("\033[91;1;5mA potencia de",x,"é %.1f" %potencia)
      print(13 * "••")
      x += 1