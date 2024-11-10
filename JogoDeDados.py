import random

def rolar_dado(lad=20):
    return random.randint(1, lad)

def calcular_dano(valor_dado):
    if valor_dado >= 18:
        return 20  
    elif valor_dado >= 14:
        return 10  
    elif valor_dado >= 8:
        return 5
    else:
        return 3  

def calcular_defesa():
    return random.randint(0, 5)

def jogo():
    vida_jogador = 60
    vida_inimigo = 55
    rodada = 1
    print(f"Sua Vida Inicial: {vida_jogador} \nVida Inicial do Inimigo: {vida_inimigo} ")   
    while vida_jogador > 0 and vida_inimigo > 0:
        print(f"\nRodada {rodada}:")

        input("\nPressione Enter para rolar o dado para o seu ataque...")
        valor_dado_jogador = rolar_dado()
        dano_jogador = calcular_dano(valor_dado_jogador)

        defesa_inimigo = calcular_defesa()
        dano_final_jogador = max(0, dano_jogador - defesa_inimigo)  #Em alguns casos sem o max o jogador ganhava vida quando a defesa era maior que o ataque
        vida_inimigo = vida_inimigo - dano_final_jogador

        print(f"\nVocê rolou um dado e caiu {valor_dado_jogador} e causou {dano_jogador} de dano e o inimigo defendeu {defesa_inimigo}")
        print(f"Dano no inimigo: {dano_final_jogador}")
        print(f"Vida do inimigo restante: {vida_inimigo}")

        if vida_inimigo <= 0:
            print("\nParabéns seu inimigo foi de arrasta")
            break

        input("\nPressione Enter para rolar o dado para o ataque do inimigo...")
        valor_dado_inimigo = rolar_dado()
        dano_inimigo = calcular_dano(valor_dado_inimigo)

        defesa_jogador = calcular_defesa()
        dano_final_inimigo = max(0, dano_inimigo - defesa_jogador) 
        vida_jogador = vida_jogador - dano_final_inimigo

        print(f"\nO inimigo rolou um dado e caiu {valor_dado_inimigo} causou {dano_inimigo} de dano e você defendeu {defesa_jogador}")
        print(f"Dano em você: {dano_final_inimigo}")
        print(f"Sua vida restante: {vida_jogador}")

        if vida_jogador <= 0:
            print("\nVocê foi de comes e bebes meu parceirinho")
            break
        
        rodada = rodada + 1

jogo()
