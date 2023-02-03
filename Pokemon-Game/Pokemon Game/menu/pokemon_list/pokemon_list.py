from pokemon_enum.pokemon_level_one import PokemonLevelOne
from pokemon_enum.pokemon_level_two import PokemonLevelTwo
from pokemon_enum.pokemon_level_three import PokemonLevelThree

class PokemonList:

    def __init__(self) -> None:
        pass

    def list_pokemon_level1():
        PokemonLevelOne.print_values()

    def list_pokemon_level2():
        PokemonLevelTwo.print_values()

    def list_pokemon_level3():
        PokemonLevelThree.print_values()