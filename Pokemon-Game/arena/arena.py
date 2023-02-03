from implementation.pokemon import Pokemon
from pokemon_enum.pokemon_options import PokemonOptions
from rich import print
import os
class Arena:


    def __init__(self, A: Pokemon, B: Pokemon) -> None:
        self.A = A
        self.B = B

    def batalhar(self) -> Pokemon:

        # Verifica o tipo dos pokémon que estão batalhando
        self.pokemon_tipe()

        while ((self.A.get_hp() > 0) and (self.B.get_hp() > 0)):

            enable_special_attack_pokemon_A = self.A.get_hp() > 1 and self.A.get_hp() <= 30
            enable_special_attack_pokemon_B = self.B.get_hp() > 1 and self.B.get_hp() <= 30


            print(self.A.list_options(enable_special_attack = enable_special_attack_pokemon_A))
            print('\n[bold][red]JOGADOR 1', 'é a sua vez!\n')
            acaoJogador1 = input()

            print(self.B.list_options(enable_special_attack = enable_special_attack_pokemon_B))
            print('[bold][blue]JOGADOR 2', 'é a sua vez!\n')
            acaoJogador2 = input()

            # BLOCO 1
            if acaoJogador1 == '1' and acaoJogador2 == '1':
                self.action(PokemonOptions.atacar, PokemonOptions.atacar)

            elif acaoJogador1 == '1' and acaoJogador2 == '2':
                self.action(PokemonOptions.atacar, PokemonOptions.defender)

            elif acaoJogador1 == '1' and acaoJogador2 == '3':
                self.action(PokemonOptions.atacar, PokemonOptions.ataque_especial)

            # BLOCO 2
            elif acaoJogador1 == '2' and acaoJogador2 == '1':
                self.action(PokemonOptions.defender, PokemonOptions.atacar)

            elif acaoJogador1 == '2' and acaoJogador2 == '2':
                self.action(PokemonOptions.defender, PokemonOptions.defender)
        
            elif acaoJogador1 == '2' and acaoJogador2 == '3':
                self.action(PokemonOptions.defender, PokemonOptions.ataque_especial)

            # BLOCO 3
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
            return None
            

        elif self.A.get_hp() == 0 and self.B.get_hp() != 0:

            os.system('clear')

            print('[bold]\n{} VENCEU! :trophy:\n'.format(self.B.get_pokemon()))
            self.A.set_numero_derrotas()
            self.B.set_numero_vitorias()

            
            print('\n[yellow][bold]*** EVOLUÇÃO! *** \n[white]{}\n'.format(self.B))


            return self.B

        elif self.B.get_hp() == 0 and self.A.get_hp() != 0:

            os.system('clear')
            
            print('[bold]\n{} VENCEU! :trophy:\n'.format(self.A.get_pokemon()))

            self.B.set_numero_derrotas()
            self.A.set_numero_vitorias()

            print('\n[yellow][bold]*** EVOLUÇÃO! *** \n[white]{}\n'.format(self.A))
            

            return self.A

            
    # método action utilizando Enum
    def action(self, option1: PokemonOptions, option2: PokemonOptions):

        '''print('\n-------------------------------\nJOGADOR 1{} \nJOGADOR 2{}\n-------------------------------'.format(option1.print_your_option(),option2.print_your_option()))'''

        # BLOCO 1.1
        if option1 == PokemonOptions.atacar and option2 == PokemonOptions.atacar:

            self.A.atacar(self.B)
            self.B.atacar(self.A)
        
            self.print_hp()

        # BLOCO 1.2
        elif option1 == PokemonOptions.atacar and option2 == PokemonOptions.defender:
            
            self.B.defender(self.A)

            self.print_hp()

        # BLOCO 1.3
        elif option1 == PokemonOptions.atacar and option2 == PokemonOptions.ataque_especial:

            self.A.atacar(self.B)
            self.B.ataque_especial(self.A)

            self.print_hp()

        # BLOCO 2.1
        elif option1 == PokemonOptions.defender and option2 == PokemonOptions.atacar:

            self.A.defender(self.B)
            
            self.print_hp()

        # BLOCO 2.2
        elif option1 == PokemonOptions.defender and option2 == PokemonOptions.defender:

            self.print_hp()

        # BLOCO 2.3
        elif option1 == PokemonOptions.defender and option2 == PokemonOptions.ataque_especial:

            self.A.defender(self.B, is_special_attack = True)

            self.print_hp()

        # BLOCO 3.1
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.atacar:
            
            self.A.ataque_especial(self.B)
            self.B.atacar(self.A)
        
            self.print_hp()

        # BLOCO 3.2
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.defender:

            self.B.defender(self.A, is_special_attack = True)

            self.print_hp()

        # BLOCO 3.3
        elif option1 == PokemonOptions.ataque_especial and option2 == PokemonOptions.ataque_especial:
            self.A.ataque_especial(self.B)
            self.B.ataque_especial(self.A)

            self.print_hp()

    def print_hp(self):

        print('[bold][white]\n------------------------\nHP de {} = {} \nHP de {} = {}\n------------------------\n'.format(self.A.get_pokemon(), self.A.get_hp(), self.B.get_pokemon(), self.B.get_hp()))

    def pokemon_tipe(self):
        basic_attack_increment = 5
        special_attack_increment = 15

        ataque_A = self.A.get_attack()
        special_attack_A = self.A.get_special_attack()

        ataque_B = self.B.get_attack()
        special_attack_B = self.B.get_special_attack()

        agua = 'Água'
        fogo = 'Fogo'
        planta = 'Planta'

        # BLOCO 1
        if ataque_A == agua and ataque_B == fogo:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        elif ataque_A == agua and ataque_B == planta:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        # BLOCO 2 
        elif ataque_A == fogo and ataque_B == agua:
            self.B.set_attack(ataque_B + basic_attack_increment)
            self.B.set_special_attack(special_attack_B + special_attack_increment)

        elif ataque_A == fogo and ataque_B == planta:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        # BLOCO 3
        elif ataque_A == planta and ataque_B == agua:
            self.A.set_attack(ataque_A + basic_attack_increment)
            self.A.set_special_attack(special_attack_A + special_attack_increment)

        elif ataque_A == planta and ataque_B == fogo:
            self.B.set_attack(ataque_B + basic_attack_increment)
            self.B.set_special_attack(special_attack_B + special_attack_increment)
