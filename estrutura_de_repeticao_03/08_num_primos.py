""" descobrir números primos """

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num - 1):
        if num % i == 0:
            print(f"O número {num} não é primo")
            break
    else: print(f'O número {num} é primo')
else: print("Digite um valor positivo ou maior que 1")