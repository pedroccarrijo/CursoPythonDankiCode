
# Contagem SEM recursão 
def reduzirNumero(numeroInt):
    while numeroInt  > 0:
        print(numeroInt)
        numeroInt -= 1

reduzirNumero(10)
# contagem regressiva de numeros inteiros - (10 a 1)

print('----' * 10)
"""
1 - checar se o nosso número não é igual a zero
2 - caso não for igual a zero - reduzir 1 unidade

5 (n - 1)
    4 (5 - 1)
        3 (4 - 1)
            2 (3 - 1)
                1 (2 - 1)
                    0 (1 - 1)
"""

# Contagem COM recursão
def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        # n - 1
        reduzirNumero(numeroInt - 1)

reduzirNumero(5)
print('----' * 10)


# Fatorial SEM recursão 
def fatorialSr(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for i in range(1, numero + 1):
            fatorial *= i 
        return fatorial 

print(fatorialSr(5))
print('----' * 10)


# Fatorial COM recursão
def fatorialCr(numero):
    if numero == 0:
        return 1
    else: 
        return numero * fatorialCr(numero - 1)

print(fatorialCr(4))