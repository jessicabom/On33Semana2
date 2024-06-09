# Solicite ao usuário para digitar 2 números

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operações Aritméticas

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisaoInteira = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

# Exibir os resultados
print("\n Seguem os resultados das operações aritméticas: ")
print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("Divisão Inteira: ", divisaoInteira)
print("Módulo (resto da divisão): ", modulo)
print("Potência: ", potencia)

# Comparações com operadores
print("\nSeguem os resultados das operações de comparação")
print("Igualdade: ", num1 == num2)
print("Diferença: ", num1 != num2)
print("Maior: ", num1 > num2)
print("Maior ou igual: ", num1 >= num2)
print("Menor: ", num1 < num2)
print("Menor ou igual: ", num1 <= num2)

# Operadores de atribuição (Vai atribuir um novo valor às variáveis)
print("\nSeguem os resultados dos operadores de atribuição")
num1 += 5
print("O novo valor do primeiro número após atualização (num1 +=5) é: ", num1)
num2 /= 2
print("O novo valor do segundo número após atualização (num2 /= 2) é: ", num2)

# Verificar presença de elementos em uma lista
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in listaNumeros:
    print(f"\nO primeiro número {num1} está na lista de números")
else:
    print(f"\nO número {num1} não está na lista de números")

    #Comparar a identidade de objetos
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    print("\nSeguem os resultados das operações de identidade de objetos:")
    print("x é z: ", x is z)
    print("x é z: ", x is y )
    print("x is not y: ", x is not y)