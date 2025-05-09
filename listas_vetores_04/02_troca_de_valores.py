""" troca de valores das variaveis sem utilizar auxiliar """

x = 10
y = 20
print(f"Valor atual de x: {x}")
print(f"Valor atual de y: {y}")
x, y = y, x
#valor de x passa para y e de y para x
print("\ntroca (x, y = y,x) \n")
print(f"Valor atual de x: {x}")
print(f"Valor atual de y: {y}")