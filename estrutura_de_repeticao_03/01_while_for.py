"""
Estrutura de repetição - loops

while 
for 
do while*

"""

""" while """
print("while")
a = 0
# print(a)
# a = a + 1
# print(a)

while a <= 5:
    print(a)
    a = a + 1
print(f"O valor final de (a) é: {a}")


#Break

b = 0
print("\nBreak\n")
while b <= 5:
    print(b)
    if b == 3:
        break
    b = b + 1
print(f"O valor final de (b) é: {b}")


#Else

c = 0
print("\nElse\n")
while c <= 5:
    print(c)
    c = c + 1
else: 
    print(f"(c) não é menor ou igual a 5. \nValor de c: {c}")
print("\n")

""" for """
print("for")

s = "franca"
for i in s:
    print(i)
print("\n")

for i in range(5):
    print(i)
# range(x) singnifica que começamos do 0 até termos 5 dígitos 
print("\n")

for i in range(1, 3):
    print(i)
# range recebe o valor do inicio da contagem e o valor final da repetição (valor final -1)
print("\n")

for i in range(2, 10, 5):
    print(i)
# range com mais de 1 parametro
# 1 - valor inicial da contagem 
# 2 - valor final da repetição (x - 1)
# 3 - valor somado a (i) a cada repetição
print("\n")

for i in range(5):
    print(i)
else: print("Chegamos ao fim da repetição")