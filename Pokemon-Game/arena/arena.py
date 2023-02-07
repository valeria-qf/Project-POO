from implementation.pokemon import Pokemon
from pokemon_enum.pokemon_options import PokemonOptions
from rich import print

import os
class Arena:


    def __init__(self, A: Pokemon, B: Pokemon) -> None:
        self.A = A
        self.B = B

    # O método batalhar possui o parâmetro is_tie(empate) que quando for empate vai ser atribuido True, e se não for inicializado ele automaticamente é False
    def batalhar(self, is_tie: bool = False) -> Pokemon:

        # Se for empate, não entra na condição para verificar o tipo do pokémon, já está verificado.
        # Caso não houvesse a verificação,  sempre que fosse empate iria verificar e incrementar novamente o ataque de acordo com o tipo de pokemón.

        if not is_tie: # Se for falso entra na condição

        # Verifica o tipo dos pokémon que estão batalhando
            self.pokemon_tipe()

        # Enquanto o hp de ambos os pokémon for maior que '0' a batalha continua
        while ((self.A.get_hp() > 0) and (self.B.get_hp() > 0)):

            # Quando o pokémon entiver com seu hp em um intervalo entre 1 e 50, a variável enable_special_attack vai receber um valor booleano. Quando for True, a opção do ataque especial é liberada
            enable_special_attack_pokemon_A = self.A.get_hp() >= 1 and self.A.get_hp() <= 50
            enable_special_attack_pokemon_B = self.B.get_hp() >= 1 and self.B.get_hp() <= 50


            print(self.A.list_options(enable_special_attack = enable_special_attack_pokemon_A))
            print('\n[bold][red]JOGADOR 1', 'é a sua vez!\n')
            acaoJogador1 = input()

            print(self.B.list_options(enable_special_attack = enable_special_attack_pokemon_B))
            print('[bold][blue]JOGADOR 2', 'é a sua vez!\n')
            acaoJogador2 = input()

            # Verificações de todas as combinações possíveis ao longo da batalha

            # BLOCO 1 (jogador 1 sempra ataca)
            if acaoJogador1 == '1' and acaoJogador2 == '1':
                self.action(PokemonOptions.atacar, PokemonOptions.atacar)

            elif acaoJogador1 == '1' and acaoJogador2 == '2':
                self.action(PokemonOptions.atacar, PokemonOptions.defender)

            elif acaoJogador1 == '1' and acaoJogador2 == '3':
                self.action(PokemonOptions.atacar, PokemonOptions.ataque_especial)

            # BLOCO 2 (jogador 1 sempre defende)
            elif acaoJogador1 == '2' and acaoJogador2 == '1':
                self.action(PokemonOptions.defender, PokemonOptions.atacar)

            elif acaoJogador1 == '2' and acaoJogador2 == '2':
                self.action(PokemonOptions.defender, PokemonOptions.defender)
        
            elif acaoJogador1 == '2' and acaoJogador2 == '3':
                self.action(PokemonOptions.defender, PokemonOptions.ataque_especial)

            # BLOCO 3 (jogador 1 sempre uma o ataque especial)
            elif acaoJogador1 == '3' and acaoJogador2 == '1':
                self.action(PokemonOptions.ataque_especial, PokemonOptions.atacar)

            elif acaoJogador1 == '3' and acaoJogador2 == '2':
                self.action(PokemonOptions.ataque_especial, PokemonOptions.defender)

            elif acaoJogador1 == '3' and acaoJogador2 == '3':
                self.action(PokemonOptions.ataque_especial, PokemonOptions.ataque_especial)

            else:
                print('\n[red][bold]Opção inválida, tente novamente!\n')

        # CHECA QUEM VENCEU E INCREMENTA NUMERO DE VITORIAS E DERROTAS

        if self.A.get_hp() == 0 and self.B.get_hp() == 0:
            print('--------------------\nEMPATE!\n--------------------')

            # Retorna None pois nenhum jogador venceu
            return None

        elif self.A.get_hp() == 0 and self.B.get_hp() != 0:

            os.system('cls')

            print('[bold]\n{} VENCEU! :trophy:\n'.format(self.B.get_pokemon()))
            self.A.set_numero_derrotas()
            self.B.set_numero_vitorias()

            if self.B.get_numero_vitorias() < 3:
                print('\n[yellow][bold]*** EVOLUÇÃO! *** \n[white]{}\n'.format(self.B))

            # Retorna B como vencedor
            return self.B

        elif self.B.get_hp() == 0 and self.A.get_hp() != 0:

            os.system('cls')
            
            print('[bold]\n{} VENCEU! :trophy:\n'.format(self.A.get_pokemon()))

            self.B.set_numero_derrotas()
            self.A.set_numero_vitorias()

            if self.A.get_numero_vitorias() < 3:
                print('\n[yellow][bold]*** EVOLUÇÃO! *** \n[white]{}\n'.format(self.A))

            # Retorna A como vencedor
            return self.A

            
    # Método action possui como parâmetro option1(jogador 1) e option2(jogador 2). Ambos são PokemonOptions(Enum que lista as opções de ataque de cada pokemon). Cada opção é verificada e chama os métodos de batalha de cada um. Exemplo: Se os 2 escolherem atacar, o método atacar de cada um é chamado.

    def action(self, option1: PokemonOptions, option2: PokemonOptions):

        '''print('\n-------------------------------\nJOGADOR 1{} \nJOGADOR 2{}\n-------------------------------'.format(option1.print_your_option(),option2.print_your_option()))'''

        # BLOCO 1.1
        if option1 == PokemonOptions.atacar and option2 == PokemonOptions.atacar:

            self.A.atacar(self.B)
            self.B.atacar(self.A)
        

        # BLOCO 1.2
        elif option1 == PokemonOptions.atacar and option2 == PokemonOptions.defender:
            
            self.B.defender(self.A)


        # BLOCO 1.3
        elif option1 == PokemonOptions.atacar and option2 == PokemonOptions.ataque_especial:

            self.A.atacar(self.B)
            self.B.ataque_especial(self.A)


        # BLOCO 2.1
        elif option1 == PokemonOptions.defender and option2 == PokemonOptions.atacar:

            self.A.defender(self.B)
            
        # BLOCO 2.2
         
        # Esse bloco ocorre quando os 2 pokémon escolhem a opção defesa, porém não é necessária sua implementação pois nada acontece quando ambos escolhem essa ação, o hp sempre continua igual.

        # BLOCO 2.3
        elif option1 == PokemonOptions.defender and option2 == PokemonOptions.ataque_especial:

            self.A.defender(self.B, is_special_attack = True) # Quando a defesa for de um ataque especial, a variavel is_special-attack recebe True e vai entrar em uma condição dentro do método defender que irá habilitar a defesa do ataque especial
            

        # BLOCO 3.1
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.atacar:
            
            self.A.ataque_especial(self.B)
            self.B.atacar(self.A)
        

        # BLOCO 3.2
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.defender:

            self.B.defender(self.A, is_special_attack = True) # Quando a defesa for de um ataque especial, a variavel is_special-attack recebe True e vai entrar em uma condição dentro do método defender que irá habilitar a defesa do ataque especial


        # BLOCO 3.3
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.ataque_especial:
            self.A.ataque_especial(self.B)
            self.B.ataque_especial(self.A)

        self.print_hp() # No fim da verificação o HP dos pokémon é exibido

    # Método que printa o Hp de ada pokémon
    def print_hp(self):

        print('[bold][white]\n------------------------\nHP de {} = {} \nHP de {} = {}\n------------------------\n'.format(self.A.get_pokemon(), self.A.get_hp(), self.B.get_pokemon(), self.B.get_hp()))


    # Método que verifica qual o tipo de pokémon é melhor contra o outro e incrementa no ataque e ataque especial.Exemplo: tipo Água é melhor que tipo fogo, então o pokemon do tipo água incrementa 5 no ataque basico e 15 no ataque especial
    def pokemon_tipe(self):
        basic_attack_increment = 5 # incremento do ataque básico para a maioria dos pokémon
        special_attack_increment = 15 # incremento do ataque especial para a maioria dos pokemon

        # Váriaveis criadas para deixar o código mais limpo e não precisar sempre repetir os métodos
        ataque_A = self.A.get_attack()
        special_attack_A = self.A.get_special_attack()

        ataque_B = self.B.get_attack()
        special_attack_B = self.B.get_special_attack()

        tipo_pokemon_A = self.A.get_tipo()
        tipo_pokemon_B = self.B.get_tipo()

        agua = 'Água'
        fogo = 'Fogo'
        planta = 'Planta'

        # BLOCO 1 ( A é água)

        if  tipo_pokemon_A == agua and tipo_pokemon_B == fogo:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        # O tipo planta tem um ataque melhor no tipo água e recebe um incremento de +10 no ataque básico para equilibrar a batalha
        elif tipo_pokemon_A == agua and tipo_pokemon_B == planta:
            self.B.set_attack(ataque_B + 10)
            self.B.set_special_attack(special_attack_A + special_attack_increment)

        # BLOCO 2 (A é fogo)

        elif tipo_pokemon_A == fogo and tipo_pokemon_B == agua:
            self.B.set_attack(ataque_B + basic_attack_increment)
            self.B.set_special_attack(special_attack_B + special_attack_increment)

        elif tipo_pokemon_A == fogo and tipo_pokemon_B == planta:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        # BLOCO 3 (A é planta)

        # O tipo planta tem um ataque melhor no tipo água e recebe um incremento de +10 no ataque básico para equilibrar a batalha
        elif tipo_pokemon_A == planta and tipo_pokemon_B == agua:
            self.A.set_attack(ataque_A + 10)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        elif tipo_pokemon_A == planta and tipo_pokemon_B == fogo:
            self.B.set_attack(ataque_B + basic_attack_increment)
            self.B.set_special_attack(special_attack_B + special_attack_increment)
