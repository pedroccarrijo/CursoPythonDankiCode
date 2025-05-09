# Pedra, Papel ou Tesoura
from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def opcao_jogador():
    escolha = input("Escolha Pedra, Papel ou Tesoura: ")
    escolha.lower()
    if escolha == "pedra" or "papel" or "tesoura":
        return escolha
    else: 
        print("Opção invalida. Tente novamente")
        opcao_jogador() # chama a função dentro dela mesma para que possa ser repetida novamente


def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina

while True: 

    #recebendo as escolhas
    print("-"*30)
    esc_jogador = opcao_jogador() # chamando a função (opcao_jogador(): )e atribuindo o seu valor a variavel "esc_jogador"
    esc_maquina  = opcao_maquina()# chamando a função (opcao_maquina(): )e atribuindo o seu valor a variavel "esc_jogador"
    print("-"*30)

    #comparação das escolhas
    # "\" usada como quebra linha para continuação do código
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            # todas as alternativas que o jogador ganha
            print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}')
            print("Você ganhou!")
            jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        # empate
        print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}')
        print("Empate")
    
    else: 
        # todas as alternativas que a máquina vence
        print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}')
        print("Você perdeu")
        maq_vitorias += 1

    #mostrando a quantidade de vitórias
    print("-"*30)
    print(f'Vitórias do Jogador: {jogador_vitorias}')
    print(f'Vitórias da Máquina: {maq_vitorias}')
    print("-"*30)

    #escolha de jogar novamente ou encerrar 
    esc_jogador = input("Você quer jogar novamente? ")
    esc_jogador.lower()
    if esc_jogador == "sim":
        pass
    elif esc_jogador == "nao" or "não":
        print("Encerrando")
        break
    else: 
        print("Encerrando")
        break


