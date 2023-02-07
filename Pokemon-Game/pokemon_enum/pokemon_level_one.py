from enum import Enum
'''classe Enum que lista as opções do pokemon no level 1'''
class PokemonLevelOne(Enum):
    bubasaur = 1
    charmander = 2
    squirtle = 3

    '''método que printa as opções de pokemon do level 1'''
    def print_values():
            print('\n1 - Bubasaur \n2 - Charmander \n3 - Squirtle')
