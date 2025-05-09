"""
Python - Comandos de controle condicional 

if, else e elif (else if)

"""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if y > x:
    print("y é maior que x")
    print("Código dentro do bloco condicional if (y > x)")

elif y < x:
    print("y é menor que x")
    print("Código dentro do bloco condicional elif (else if) (y < x)")

else:
    print("y e x possuem o mesmo valor")
    print("Código dentro do bloco condicional else (!= y > x and y < x)")