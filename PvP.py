import random as rd
import time as tm


class Entidade :
    def __init__(self , vida:float = 100 , mana:float = 100 , defesa:float = 5 , dano_fisico:float = 20 , classe:str = "" , pontos_Acao:float = 1):
        self.vida = vida
        self.mana = mana 
        self.defesa = defesa
        self.dano_fisico = dano_fisico
        self.classe = classe
        self.pontos_Acao = pontos_Acao

    def receber_dado(self , Dano_recebido):
        self.vida -= Dano_recebido
        return

    def ataque_Magico(self , alvo:'Entidade'):
        d20_Jogador = rd.randint(1,20) 
        d20_Inimigo = rd.randint(1,20)
        d20_Jogador *= self.pontos_Acao
        d20_Inimigo *= alvo.pontos_Acao 
        tm.sleep(2)
        print(f'o seu dado foi {d20_Jogador:.2f}')
        tm.sleep(2)

        print()
        print(f'O dado do Oponente foi {d20_Inimigo:.2f}')
        tm.sleep(2)
        if d20_Inimigo < d20_Jogador:
            d6 = rd.randint(1,6)
            dano_ataque  = self.mana * d6 / alvo.defesa
            print(f"seu dano Foi de {dano_ataque}")
            tm.sleep(2)
            return dano_ataque
        else:
            print("O Ataque Falhou")
            tm.sleep(2)
            return 0

    def ataque_fisico(self , alvo:'Entidade'):
        d20_Jogador = rd.randint(1,20) 
        d20_Inimigo = rd.randint(1,20)
        d20_Jogador *= self.pontos_Acao
        d20_Inimigo *= alvo.pontos_Acao 
        print()
        print(f'o seu dado foi {d20_Jogador}')
        tm.sleep(2)
        print()
        print(f'O dado do Oponente foi {d20_Inimigo}')
        tm.sleep(2)
        if d20_Inimigo < d20_Jogador:
            d6 = rd.randint(1,6)
            dano_ataque  = self.dano_fisico * d6 / alvo.defesa
            print(f"seu dano Foi de {dano_ataque}")
            tm.sleep(2)
            return dano_ataque
        else:
            print("O Ataque Falhou")
            tm.sleep(2)
            return 1
    
    def restaurar_vida(self):
        print()
        d6_vida = rd.randint(1,6)
        d20= rd.randint(1,20) 
        d20_mestre = rd.randint(1,20) 
        tm.sleep(2)
        print(f"Seu dado: {d20}")
        tm.sleep(2)
        print(f"o dado do meste e: {d20_mestre}")
        Valor_Teste = d20 * (self.pontos_Acao * 1.5)
        tm.sleep(2)     

        print()
        print(f"Seu Valor de Proficiencia foi {Valor_Teste}")
        if Valor_Teste > d20_mestre:
            print("Voce venceu")
            self.vida += d6_vida
            print(f"Curou {d6_vida}")
            return
        else:
            print("Voce falhou")
            print("passou a vez")
            return



    def mostrar_status(self):

        print(f"({self.classe})")
        print(f"Vida: {self.vida:.2f}")
        print(f"Mana: {self.mana:.2f}")
        print(f"Defesa: {self.defesa:.2f}")
        print(f"Dano: {self.dano_fisico:.2f}")
        print(f"Ação: {self.pontos_Acao:.2f}")

        

class Cavaleiro(Entidade): 
     
    def __init__(self ):
        
        super().__init__()
    
        self.vida *= 1.5
        self.mana *= 0.5 
        self.defesa *= 2
        self.dano_fisico *= 1.1
        self.classe = "Cavaleiro" 
        self.pontos_Acao *= 1.0 

class Mago(Entidade): 

    def __init__(self):

        super().__init__()
        self.vida *= 0.6
        self.mana *= 3.0
        self.defesa *= 0.2
        self.dano_fisico*= 0.3
        self.classe = "Mago" 
        self.pontos_Acao *= 0.7 

class arqueiro(Entidade): 

    def __init__(self):

        super().__init__()
        self.vida *= 0.9
        self.mana *= 2.0
        self.defesa *= 0.2
        self.dano_fisico *= 1.0
        self.classe = "arqueiro" 
        self.pontos_Acao *= 3.0 

class berserker(Entidade):
    
    def __init__(self):

        super().__init__()
        self.vida *= 3.0
        self.mana *= 0.001
        self.defesa *= 0.2
        self.dano_fisico *= 4.0
        self.classe = "Berserker" 
        self.pontos_Acao *= 2.0 

class Monge(Entidade):
    
    def __init__(self):

        super().__init__()
        self.vida *= 1
        self.mana *= 2
        self.defesa *= 1.7
        self.dano_fisico *= 2.07
        self.classe = "Monge" 
        self.pontos_Acao *= 3.5 



def turno_do_jogador(jogador: Entidade, alvo: Entidade):

    while True:
        print("Escolha sua ação:")
        print("1: Ataque Físico ")
        print("2: Ataque Mágico ")
        print("3: Recuperar Vida")
        escolha = input("Digite o número da sua escolha (1, 2 ou 3): ")

        if escolha == '1':
            alvo.receber_dado(jogador.ataque_fisico(alvo))
            
            break
        elif escolha == '2':
                alvo.receber_dado(jogador.ataque_Magico(alvo))
                break
            
        elif escolha == '3':
            jogador.restaurar_vida()
            break
        else:
            print("Escolha inválida. Tente novamente.")

def definir_classe(numero_escolha):
    
    if numero_escolha == 1:
        personagem = berserker()
    if numero_escolha == 2: 
        personagem = Cavaleiro()
    if numero_escolha == 3:
        personagem = Mago()
    if numero_escolha == 4:
        personagem = arqueiro()
    if numero_escolha == 5:
        personagem = Monge()
    

    return personagem

    
print("__________________")
print("escola sua Classe")
print("__________________")
print("Baserker 1 ")

print("__________________")
print("Cavaleiro 2" )

print("__________________")
print("Mago 3")

print("__________________")
print("Arqueiro")

print("__________________")
Escola1 = int(input("Jogador1: "))
Escola2 = int(input("Jogador2: "))
jogador1 = definir_classe(Escola1)
jogador2 = definir_classe(Escola2)
rodada = 1

while True:
    
    print(f"rodada {rodada}")
    print()
    print("__________________")
    print(jogador1.mostrar_status())
    print("__________________")
    print()
    print("__________________")
    print(jogador2.mostrar_status())
    print("__________________")



    print("Vez do jogador 1")
    turno_do_jogador(jogador1 , jogador2)
    print()
    print("__________________")
    print(jogador1.mostrar_status())
    print("__________________")
    print()
    print("__________________")
    print(jogador2.mostrar_status())
    print("__________________")
    if jogador2.vida <= 0:
        print("o Jogador 2 morreu , Jogador 1 e o ganhador")
        break
    
    print("Vez do jogador 2")
    turno_do_jogador(jogador2 , jogador1)
    print()
    print("__________________")
    print(jogador1.mostrar_status())
    print("__________________")
    print()
    print("__________________")
    print(jogador2.mostrar_status())
    print("__________________")
    if jogador1.vida <= 0:
        break