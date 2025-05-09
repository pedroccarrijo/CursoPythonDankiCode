""" como achar o fatorial de um número """

num = int(input("Insira um número: "))
result = 1
if num < 0:
    print("Não existe fatorial de números negativos")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    for i in range(1, num):
        result += result * (num - i)
    print(f'O fatorial de {num} é {result}')