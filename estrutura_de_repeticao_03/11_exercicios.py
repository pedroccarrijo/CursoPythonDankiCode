#1)  Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o resultado.


# vet = []
# for i in range(5):
#     vet.append(int(input(f"Digite o valor do {i + 1}º valor: ")))
# menor = vet[0]
# maior = vet[1]
# for i in range(5):
#     if menor > vet[i]:
#         menor = vet[i]
#     if maior < vet[i]:
#         maior = vet[i]
# print(f'{maior} é o número maior')
# print(f'{menor} é o número menor')
    

# 2) Escreva um programa para calcular as somas:
#  S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
#  S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
#  S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)

#soma01
soma01 = 3/40
for i in range(4):
    if i == 3:
        soma01 += 340/1
    else:
        soma01 += (32 + i) / (39 - i)
print(f'Resultado da primeira somatoria: {soma01}')

#soma02
soma02 = 480/2
numerador02 = 480
for i in range(22, 41):
    numerador02 = numerador02 - 5
    print(f'{numerador02} / {i}')
    soma02 += numerador02 / i
    print(soma02)
print(f'Resultado da segunda somatoria: {soma02}')

#soma03 
soma03 = 1/2
numerador03 = 1
for i in range(23, 50, 2):
    numerador03 = numerador03 * 2 + 1
    print(f'{numerador03} / {i}')
    soma03 += numerador03 / i
    print(soma03)
print(f'Resultado da segunda somatoria: {soma03}')