from menu.pokemon_list.pokemon_list import PokemonList
from arena.arena import Arena
from implementation.pokemon import Pokemon
from pokemon.bubasaur.bubasaur import Bubasaur
from pokemon.bubasaur.ivysaur import Ivysaur
from pokemon.bubasaur.venusaur import Venusaur
from pokemon.charmander.charmander import Charmander
from pokemon.charmander.charmeleon import Charmeleon
from pokemon.charmander.charizard import Charizard
from pokemon.squirtle.squirtle import Squirtle
from pokemon.squirtle.wartortle import Wartortle
from pokemon.squirtle.blastoise import Blastoise
from tqdm import tqdm
from rich import print
import time
import os
class Pokedex:

    def __init__(self, pokemon_list: PokemonList) -> None:
        self.__pokemon_list = pokemon_list

    def start_game(self):
        print('[yellow][bold]\nPOKÉMON GAME\n')
        print('Bem vindo ao Pokémon game um mini jogo onde você iniciará sua jornada como treinador pokémon! \nPara iniciar o jogo, primeiro é selecionado o level da batalha e depois \ncada jogador deverá escolher seu pokémon de acordo com o level escolhido.\n\n[bold][white]Ex: level 1 [bold]\n\nBubasaur :seedling: \nCharmander :fire: \nSquirtle :droplet:\n')

        
        print('\n[bold]\nPressione [yellow]ENTER [white]para continuar!')

        input()
        os.system('clear')

    def select_pokemon_level(self):
        self.start_game()

        print('\n[green]Selecione o nível dos Pokémon que irão batalhar:[white]\n\n1 - Nível 1 \n2 - Nível 2 \n3 - Nível 3\n')
        pokemon_level = int(input())

        print('\n[green]Escolha um Pokémon abaixo:')

        pokemon_one: Pokemon
        pokemon_two: Pokemon
    
        if pokemon_level == 1:
            self.__pokemon_list.list_pokemon_level1()
            self.choose_pokemon_A()
            fist_pokemon = int(input())
            self.choose_pokemon_B()
            second_pokemon = int(input())
            pokemon_one = self.create_pokemon(pokemon_level, fist_pokemon)
            pokemon_two = self.create_pokemon(pokemon_level, second_pokemon)

        elif pokemon_level == 2:
            self.__pokemon_list.list_pokemon_level2()
            fist_pokemon = int(input())
            second_pokemon = int(input())
            pokemon_one = self.create_pokemon(pokemon_level, fist_pokemon)
            pokemon_two = self.create_pokemon(pokemon_level, second_pokemon)

        elif pokemon_level == 3:

            self.__pokemon_list.list_pokemon_level3()
            fist_pokemon = int(input())
            second_pokemon = int(input())
            pokemon_one = self.create_pokemon(pokemon_level, fist_pokemon)
            pokemon_two = self.create_pokemon(pokemon_level, second_pokemon)

        else:
            print('\nOpção inválida, tente novamente!\n')
        
        os.system('clear')

        print('[bold]\n-------------------------------\n[red]JOGADOR 1 [white]escolheu {} \n\n[blue]JOGADOR 2 [white]escolheu {}\n-------------------------------\n\n'.format(pokemon_one.get_pokemon(), pokemon_two.get_pokemon()))

        print('[yellow][bold]\n---------- CRIANDO ARENA ----------\n')
        for i in tqdm(range(10)):
            time.sleep(0.2)
        
        print('\n[bold]Pressione [yellow]ENTER [white]para continuar!')
        input()
        os.system('clear')

        arena = Arena(A = pokemon_one, B = pokemon_two)
        # arena.batalhar retorna o pokemon vencedor da batalha
        pokemon_vencedor = arena.batalhar()


        if pokemon_vencedor != None:

            pokemon_evolucao = pokemon_vencedor

            if isinstance(pokemon_evolucao, Charmander):
                pokemon_evolucao = Charmeleon()
            
            elif isinstance(pokemon_vencedor, Charmeleon):
                pokemon_evolucao = Charizard()

            elif isinstance(pokemon_vencedor,  Bubasaur):
                pokemon_evolucao = Ivysaur()

            elif isinstance(pokemon_vencedor, Ivysaur):
                pokemon_evolucao = Venusaur()

            elif isinstance(pokemon_vencedor, Squirtle):
                pokemon_evolucao = Wartortle()

            elif isinstance(pokemon_vencedor, Wartortle):
                pokemon_evolucao = Blastoise()

            replay: bool = True

            while replay:

                print('[green]Deseja continuar? [bold][white]\n\n1 - SIM \n2 - NÃO\n')
                acao = int(input())

                if acao == 1:
                    nivel_vencedor = pokemon_vencedor.get_level()

                    print('[green]Escolha um Pokémon abaixo:\n')
                    
                    '''if nivel_vencedor == 1:
                        self.__pokemon_list.list_pokemon_level1()

                        second_pokemon = int(input())
                        new_oponent = self.create_pokemon(1, other_pokemon)
                    '''

                    if nivel_vencedor == 2:
                        self.__pokemon_list.list_pokemon_level2()

                        other_pokemon = int(input())
                        new_oponent = self.create_pokemon(2, other_pokemon)


                    elif nivel_vencedor == 3:
                        self.__pokemon_list.list_pokemon_level3()
                        
                        other_pokemon = int(input())
                        new_oponent = self.create_pokemon(3, other_pokemon)
                        
                    new_arena = Arena(A = pokemon_evolucao, B = new_oponent)
                    pokemon_vencedor = new_arena.batalhar()
                    
                elif acao == 2:
                    replay = False

    def create_pokemon(self, level: int, pokemon_option: int) -> Pokemon:
        
        if (level < 0 or level > 3) or (pokemon_option < 0 or pokemon_option > 3):
            return Exception('Opção inválida, tente novamente!\n')

        elif level == 1:
            if pokemon_option == 1:
                return Bubasaur()

            elif pokemon_option == 2:
                return Charmander()

            elif pokemon_option == 3:
                return Squirtle()

        elif level == 2:
            if pokemon_option == 1:
                return Ivysaur()
            
            elif pokemon_option == 2:
                return Charmeleon()

            elif pokemon_option == 3:
                return Wartortle()

        elif level == 3:
            if pokemon_option ==1:
                return Venusaur()

            elif pokemon_option == 2:
                return Charizard()

            elif pokemon_option == 3:
                return Blastoise()

    def get_pokemon_list(self):
        return self.__pokemon_list

    def choose_pokemon_A(self):
            print('\n[bold][red]JOGADOR 1' , '[bold]escolha o seu Pokémon!')

    def choose_pokemon_B(self):
            print('\n[bold][blue]JOGADOR 2' , '[bold]escolha o seu Pokémon!')
            