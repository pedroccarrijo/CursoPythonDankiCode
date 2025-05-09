"""Esse módulo tem como objetivo:
        retornar se um número é primo ou não
    
    Funções disponíveis:
        primo
"""
# modulo_09.primo_modulo.__doc__ (chamando no terminal - obrigatório colocar a pasta de origem (caso esteja em uma))
# __doc__ - mostra a documentação o que esta em """ aqui dentro """



""" descobrir números primos """


def primo(num):
    """ 
        Essa função tem como objetivo:
            retornar se um número é primo ou não
        Parâmetros (num):
            1 parâmetro obrigatório - do tipo numérico inteiro
    """ # modulo_09.primo_modulo.primo.__doc__ -> para mostrar a documentação dentro da função é preciso chamar o modulo mais o nome da função desejada
    #from modulo_09.primo_modulo import primo -> assim você importa apenas a função primo do modulo, então caso use .__doc__ já terá como resposta a documentação que esta dentro da função
    if num > 1:
        for i in range(2, num - 1):
            if num % i == 0:
                return f"O número {num} não é primo"
        else: return f'O número {num} é primo'
    else: return "Digite um valor positivo ou maior que 1"


# parte dunder

if __name__ == '__main__':
    print('ola mundo no módulo primo') 
    # essa função é executada apenas quando o código é rodado no arquivo de origem ( se for executado em outro módulo essa parte não é funcional )