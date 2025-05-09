"""
Exercícios - Python 

Observação: Todos os exercícios devem utilizar a função input, 
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo 
02 - área de um quadrado 
03 - Se o produto que você quer avaliar custa (??) reais, qual
será o valor do mesmo com desconto de (??)%
04 - área do círculo
05 - conversão de reais para dolar 
06 - conversão de dolar para real 

"""

#1)
base_retangulo = float(input("Qual o valor da base do retângulo?"))
altura_retangulo = float(input("Qual o valor da altura do retângulo?"))
area_retangulo = base_retangulo * altura_retangulo
print(area_retangulo)

#2)
lateral_quadrado = float(input("Qual o valor da lateral do quadrado?"))
area_quadrado = lateral_quadrado**2
print(area_quadrado)

#3)
valor = float(input("Qual o valor do produto?"))
desconto_porcentagem = float(input("Qual o valor do desconto em %?"))
desconto = valor / 100 * desconto_porcentagem
valor_desconto = valor - desconto
print(valor_desconto)

#4)
raio_circulo = float(input("Qual o raio do círculo?"))
area_circulo = 3.1415 * (raio_circulo**2)
print(area_circulo)

#5)
reais = float(input("Qual o valor em reais?"))
reaisParaDolar = reais / 6.09
print(reaisParaDolar)

#6)
dolar = float(input("Qual o valor em dolar?"))
dolarParaReal = dolar * 6.09
print(dolarParaReal)