from enum import Enum
'''classe Enum que lista as opções do pokemon no level 2'''
class PokemonLevelTwo(Enum):
    ivysaur = 1
    charmeleon = 2
    wartortle = 3

    '''método que printa as opções de pokemon do level 2'''
    def print_values():
            print('\n1 - Ivysaur \n2 - Charmeleon \n3 - Wartortle')