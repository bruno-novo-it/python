# Funções para cálculo da fórmula de Bhaskara

import math
import sys

# Exemplo de valores entrada
# Equação = 1xˆ2+12x-13
# a = 1
# b = 12
# c = -13
# delta = 196
# x1 = 1
# x2 = -13

# Equação = 3xˆ2+4x-20
# a = 3
# b = 4
# c = -20
# delta = 256
# x1 = 2
# x2 = -(10/3) = 3.3333....

def get_parameter_a():
    a=input ("Digite o A: ")
    return float(a)

def get_parameter_b():
    b=input ("Digite o B: ")
    return float(b)

def get_parameter_c():
    c=input ("Digite o C: ")
    return float(c)

def calc_delta(a,b,c):
    return float(b**2 - 4*a*c)

def calc_raizes(D):
    if D < 0:
        print ("Valor de delta negativo, raiz impossivel de ser extraida com numeros reais")
        sys.exit()
    else:
        print("Delta é igual à: %f" % D)

    M = math.sqrt(D)

    X1=(-B+M)/(2*A)

    X2=(-B-M)/(2*A)

    print("Raiz aproximada de X1 = %f" % X1)
    print("Raiz aproximada de X2 = %f" % X2)

print ("---Programa para calcular Bhaskara---")
A = get_parameter_a()
B = get_parameter_b()
C = get_parameter_c()

D = calc_delta(A,B,C)

calc_raizes(D)
