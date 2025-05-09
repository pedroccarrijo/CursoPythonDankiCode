# 1)

# def num_maior(x, y):
#     if x > y:
#         return x
#     elif x < y:
#         return y
#     else: return "Os dois valores são iguais"

# def media(x, y):
#     return ((x + y) / 2)

# x = int(input("Digite o valor de x: "))
# y = int(input("Digite o valor de y: "))

# escolha = int(input("Escolha uma das opções: \n1 - Maior dos números \n2 - Média aritmética \n"))
# if escolha == 1:
#     print(f'Resultado {num_maior(x, y)}')
# else:
#     print(f' Resultado {media(x, y)}')



# 2)

def potencia(base, expoente):
    if base == 0:
        return 1
    elif expoente == 0:
        return 1
    else: return base ** expoente

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

print(potencia(base, expoente))

# 3)
import math

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

def potencia(x, y):
    return x ** y

def raiz(x):
    return math.sqrt(x)

def porcentagem(x, y):
    return x % y

def operacoes(op):
    switch = {
    '+' : print(soma(x, y)),
    '-' : print(sub(x, y)),
    '*' : print(mult(x, y)),
    '/' : print(div(x, y)),
    '^' : print(potencia(x, y)),
    'sqrt' : print(raiz(x)),
    '%' : print(porcentagem(x, y))
}

x = float(input("Digite um valor: "))
y = float(input("Digite um valor: "))
op = input("Escolha uma operação:\n '+' - soma\n '-' - subtração\n '*' - multiplicação\n '/' - divisão\n '^' - potencia\n 'sqrt' - raiz quadrada ")


