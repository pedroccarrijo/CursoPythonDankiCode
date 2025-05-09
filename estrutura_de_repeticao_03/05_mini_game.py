"""
do while 

código para adivinhar um número

"""

palpite = 0
num = 9

while palpite != num: 
    print("Qual o número correto? ")
    palpite = int(input())
    print("Você errou, tente novamente")

print("Parabéns você certou ")


""" Utilizando a função boolean """

# Função bool() -> boolean 0 = false, 1 = true
print(bool(palpite))

""" Bool """
# if bool is true it enters while (true = 1) (false = 0)
while bool(palpite) is True:
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == num:
        print("Parabéns você certou ")
        break;
    else:
        print("Você errou, tente novamente")
# Caso o numero "0" seja digitado o código é encerrado


""" Função que se assemelha a o do while (verifica após a execução)"""
""" do while* """
# sempre entra como verdadeira
while True:
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == num:
        print("Parabéns você certou ")
        break;
    else:
        print("Você errou, tente novamente")
else:
    print("Erro na aplicação")
    print(bool(palpite))