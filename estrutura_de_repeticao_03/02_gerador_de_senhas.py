#maiúsculas e minúsculas 
#símbolos e espaços 

"""
security = chave
5ecurt1ty = senha

hex
1 = 1
até 
9 = 9 
11 = A
12 = B
13 = C 
14 = D
15 = E

"""
chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    else:
        senha = senha + letra
print(senha)

#exemplo de resposta:
# Digite a base da sua senha: pedrocarvalho
# p1413#o1210#v10lho