def fat(n):
    if(n ==0):
        return 1
    return n * fat(n - 1)

def pot(base, exp):
    if(exp == 0):
        return 1
    return base * pot(base, exp - 1)

# Calcular a Área de um Quadrado
def are_quadrado(lado):
    return lado * lado
