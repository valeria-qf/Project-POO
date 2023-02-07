from enum import Enum
'''classe Enum que lista as opções do pokemon no level 3'''
class PokemonLevelThree(Enum):
    venusaur = 1
    charizard = 2
    blastoise = 3

    '''método que printa as opções de pokemon do level 3'''
    def print_values():
            print('\n1 - Venusaur \n2 - Charizard \n3 - Blastoise')
