from pokemon_enum.pokemon_level_one import PokemonLevelOne
from pokemon_enum.pokemon_level_two import PokemonLevelTwo
from pokemon_enum.pokemon_level_three import PokemonLevelThree

'''criação da classe PokemonList'''
class PokemonList:

    def __init__(self) -> None:
        pass
    
    '''Método que quando chamado vai chamar a listagem de pokemon do level 1'''
    def list_pokemon_level1():
        PokemonLevelOne.print_values()

    '''Método que quando chamado vai chamar a listagem de pokemon do level 2'''
    def list_pokemon_level2():
        PokemonLevelTwo.print_values()

    '''Método que quando chamado vai chamar a listagem de pokemon do level 3'''
    def list_pokemon_level3():
        PokemonLevelThree.print_values()