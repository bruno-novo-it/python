
### Nesting ###

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

count = 0

print("Valores da Matriz: ", M)

print() # Pula Linha

for itens in M:
    print("Valores da Matriz: ",itens)

print()

for itens in M:
    print("Valor",count,"da Matriz: ",itens)
    count += 1

print()

print(M[1]) # Captura a linha 2
print()

print(M[1][2]) # Captura a linha 2 e mostra o 3 elemento
print()

### Comprehensions ###

# Coleta os itens na coluna 2
col2 = [row[1] for row in M]
print("Valores da Coluna 2: ",col2)
print()

# Coleta os itens na coluna 2 e soma 1 em cada um deles
col2_plus_1 = [row[1] + 1 for row in M]
print("Valores da Coluna 2 + 1:",col2_plus_1)
print()

# Coleta os itens na coluna 2 apenas se forem pares
col2_odd = [row[1] for row in M if row[1] % 2 ==0 ]
print("Valores da Coluna 2 Pares: ",col2_odd)
print()

# Coleta os itens na coluna 2 apenas se não forem pares
col2_no_odd = [row[1] for row in M if row[1] % 2 !=0 ]
print("Valores da Coluna 2 Ímpares: ",col2_no_odd)
print()

# Coleta a diagonal da Matriz
diag = [M[i][i] for i in [0,1,2]]
print("Diagonal da Matriz M: ",diag)
print()

# Repete os caracteres em uma String
doubles = [c * 2 for c in 'spam']
print("Duplica os caracteres em uma string: ",doubles)
print()

# Gera lista de 0..3
lista = list(range(4))
print("O tipo da lista é: ", list)
print("Lista(0..3): ",list(range(4)))
print("Lista(0..3): ",lista)
print()

# Gera lista de -6..6 de 2 em 2
lista2 = list(range(-6,7,2)) # Segundo elemento é o ultimo da lista + 1
print("Lista(-6..6): ",lista2)
print()

# Gera uma lista com multiplicação dos seus valores originais
lista3 = [[x ** 2, x ** 3] for x in range(4)]
print("Lista Multiplicada: ", lista3)
