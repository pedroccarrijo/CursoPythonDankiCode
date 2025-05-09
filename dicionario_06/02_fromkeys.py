"""
Função Fromkeys -> transforma outros tipos de variáveis em dicionários

"""
#index     0         1        2
tupla = ("item1", "item2", "item3")
dicionario = dict.fromkeys(tupla)
print(dicionario)
#trnsforma uma tupla (ou outro tipo de variável em dicionário)
#os valores anteriormente da tupla passam a ser as chaves do dicionario

tupla = ("item1", "item2", "item3")
x = 0
dicionario = dict.fromkeys(tupla, x)
print(dicionario)
#o segundo parametro passa a ser o valor das chaves 

dicio = {
    "dicio1": {
        "nome": "Pedro",
        "idade": 19
    },
    "dicio2": {
        "nome": "Ana",
        "idade": 20
    }
}
print(dicio)
#é possivel criar dicionários um dentro do outro 