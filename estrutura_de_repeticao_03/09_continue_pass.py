""" break """
print("break")
for i in range(10):
    if i == 5:
        break
    print(i)
# break -> finaliza o programa naquele ponto ( caso entre na condição do if )
print(50 * "-")

""" continue """
print("\ncontinue")
for i in range(10):
    if i == 5:
        continue 
    print(i)
# continue -> cancela o laço atual e pula para o proximo ( se i é 5 ele pula para o 6 é a ação do 5 é canselada)
print(50 * "-")

""" pass """
print("\npass")
for i in range(10):
    if i == 5:
        pass 
    print(i)
if i == 3:
    #essa condição vai gerar um ERRO 
    pass
    #pass ignora o erro e continua o código
print("Ola mundo")