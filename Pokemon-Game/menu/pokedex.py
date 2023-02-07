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
from rich import print
import time
import os
from tqdm import tqdm
class Pokedex:

    def __init__(self, pokemon_list: PokemonList) -> None:
        self.__pokemon_list = pokemon_list

    def start_game(self):
        print('[yellow][bold]\nPOKÉMON GAME\n')
        print('Bem vindo ao Pokémon game um mini jogo onde você iniciará sua jornada como treinador pokémon! \nPara iniciar o jogo, primeiro é selecionado o level da batalha e depois \ncada jogador deverá escolher seu pokémon de acordo com o level escolhido.\n\n[bold][white]Ex: level 1 [bold]\n\nBubasaur :seedling: \nCharmander :fire: \nSquirtle :droplet:\n')

        
        print('\n[bold]\nPressione [yellow]ENTER [white]para continuar!')

        input()
        os.system('cls')

    def select_pokemon_level(self):
        # O start_game dá print no texto inicial do jogo
        self.start_game()

        print('\n[green]Selecione o nível dos Pokémon que irão batalhar:[white]\n\n1 - Nível 1 \n2 - Nível 2 \n3 - Nível 3\n')
        pokemon_level = int(input())

        print('\n[green]Escolha um Pokémon abaixo:')

        pokemon_one: Pokemon
        pokemon_two: Pokemon

        # Verifica qual o level escolhido e mostra as opções de pokemon acordo com a escolha.Um input é dado para cada jogador. Após isso, o método create_pokemon é chamado e é passado como parâmetro o level escolhido e o pokemon escolhido. Esse método verifica qual o pokémon que vai ser criado e gera um retorno que é instanciado em pokemon_one e pokemon_two
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
            self.choose_pokemon_A()
            fist_pokemon = int(input())
            self.choose_pokemon_B()
            second_pokemon = int(input())
            pokemon_one = self.create_pokemon(pokemon_level, fist_pokemon)
            pokemon_two = self.create_pokemon(pokemon_level, second_pokemon)

        elif pokemon_level == 3:

            self.__pokemon_list.list_pokemon_level3()
            self.choose_pokemon_A()
            fist_pokemon = int(input())
            self.choose_pokemon_B()
            second_pokemon = int(input())
            pokemon_one = self.create_pokemon(pokemon_level, fist_pokemon)
            pokemon_two = self.create_pokemon(pokemon_level, second_pokemon)

        else:
            print('\nOpção inválida, tente novamente!\n')
        
        os.system('cls')

        print('[bold]\n-------------------------------\n[red]JOGADOR 1 [white]escolheu {} \n\n[blue]JOGADOR 2 [white]escolheu {}\n-------------------------------\n\n'.format(pokemon_one.get_pokemon(), pokemon_two.get_pokemon()))

        print('[yellow][bold]\n---------- CRIANDO ARENA ----------\n')
        for i in tqdm(range(0, 10)):
            time.sleep(0.2)
        
        print('\n[bold]Pressione [yellow]ENTER [white]para continuar!')
        input()
        os.system('cls')

        arena = Arena(A = pokemon_one, B = pokemon_two)
        # arena.batalhar retorna o pokemon vencedor da batalha
        pokemon_vencedor = arena.batalhar()

        # Se não houver vencedor, ou seja, empate, o hp dos pokemon será resetado, uma nova arena é instanciada e é chamada uma nova arena que também terá um vencedor como retorno. Essa conndição fica presa no while até existir um  retorno diferente de None
        if pokemon_vencedor == None:
                while pokemon_vencedor == None:
                    pokemon_one.reset_hp()
                    pokemon_two.reset_hp()
                    newArena = Arena(A = pokemon_one, B = pokemon_two)
                    pokemon_vencedor = newArena.batalhar(is_tie = True)

        if pokemon_vencedor != None:

            # Quando houver um pokemon vencedor, o replay recebe True, logo vai ficar preso no while e verificando o vencedor e iniciando uma nova batalha

            replay: bool = True
            while replay:

                pokemon_evolucao = pokemon_vencedor

                # Checa se o vencedor é instância de cada pokémon e instancia um novo com a classe de evolução. Ex: se pokemon é instancia de Charmander, o pokemon_evolucao é sobrescrevido com a instância do Charmeleon(evolução de Charmander)

                if isinstance(pokemon_evolucao, Charmander):
                    pokemon_evolucao = Charmeleon()
                
                elif isinstance(pokemon_evolucao, Charmeleon):
                    pokemon_evolucao = Charizard()

                elif isinstance(pokemon_evolucao,  Bubasaur):
                    pokemon_evolucao = Ivysaur()

                elif isinstance(pokemon_evolucao, Ivysaur):
                    pokemon_evolucao = Venusaur()

                elif isinstance(pokemon_evolucao, Squirtle):
                    pokemon_evolucao = Wartortle()

                elif isinstance(pokemon_evolucao, Wartortle):
                    pokemon_evolucao = Blastoise()

                # Se o número de vitórias for menor que 3 os jogadores tem a opção de continuar, senão, ao batalhar no último nível, o número de vitórias é igual a 3 e jogo chega ao fim
                if pokemon_evolucao.get_numero_vitorias() < 3:
            
                    print('[green]Deseja continuar? [bold][white]\n\n1 - SIM \n2 - NÃO\n')
                    acao = int(input())

                    # Se o jogador decidir continuar jogando, é verificado o level do pokemon vencedor para quando o novo oponente for escolher outro pokemon para batalhar, terá que ser um do mesmo level do vencedor

                    if acao == 1:
                        nivel_vencedor = pokemon_vencedor.get_level()

                        print('[green]Escolha um Pokémon abaixo:\n')

                        # o level 1 não é verificado, pois o vencedor sempre evolui após vencer a batalha, logo nunca será level 1

                        if nivel_vencedor == 2:
                            # Se o vencedor for level 2, vai ser exibido ao novo oponente a lista de pokemon do level 2. Um input é recebido com a escolha do pokémon e é passado o level e a escolha do jogador nos parâmetros do método create pokemon, para ser criado um novo pokemon para o jogador que perdeu

                            self.__pokemon_list.list_pokemon_level2()

                            other_pokemon = int(input())
                            new_oponent = self.create_pokemon(2, other_pokemon)


                        elif nivel_vencedor == 3:
                            self.__pokemon_list.list_pokemon_level3()
                            
                            other_pokemon = int(input())
                            new_oponent = self.create_pokemon(3, other_pokemon)
                        
                        # No fim da verificação, a nova arena é criada e é passado como parâmetro o pokemon vencedor(que evoluiu) e o novo oponente

                        new_arena = Arena(A = pokemon_evolucao, B = new_oponent)

                        #pokemon vencedor recebe new arena pois vai ser utilizado como retorno e renovar a variável pokemon evolução

                        pokemon_vencedor = new_arena.batalhar()

                        # Verifica se existiu empate após uma rodada de vitória
                        if (pokemon_vencedor == None):
                            while(pokemon_vencedor == None):
                                pokemon_evolucao.reset_hp()
                                new_oponent.reset_hp()
                                newArena = Arena(A = pokemon_evolucao, B = new_oponent)
                                pokemon_vencedor = newArena.batalhar(is_tie= True)
                        
                    # Se o jogador dacidir não continuar a gameplay, replay recebe False e o jogo acaba
                    elif acao == 2:
                        replay = False
                        print('[bold][green]F I M')

                # Número de batalhas maior que 2, os seja, já jogou a sua última batalha no level final, completando 3 vitórias
                else:
                    print('[bold][green]F I M')
                    break

    def create_pokemon(self, level: int, pokemon_option: int) -> Pokemon:
        
        # Se as escolhas estiverem fora do intervado de escolhas apresentadas, é retornado que a opção é inválida pedindo para tentar novamente
        if (level < 0 or level > 3) or (pokemon_option < 0 or pokemon_option > 3):
            return Exception('Opção inválida, tente novamente!\n')

        #Checa o level e o pokemon escolhidos que serão passados nos parâmetros quando o método for chamado e vai retornar o pokémon que condiz com as caracteristicas. O retorno é instaciado em uma variável quando o método é chamado
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
            