from enum import Enum
from rich import print
'''classe enum que lista as opções de ação de um pokemon em uma batalha'''
class PokemonOptions(Enum):
    atacar = 1
    defender = 2
    ataque_especial = 3

    ''' Método que printa o menu de batalha
        Se o enable_special_atack for True, o menu com o ataque especial é liberado
        Senão, o menu é exibido sem essa opção'''
    def print_values(enable_special_attack):
        if enable_special_attack:
                return '\n[white]1 - Atacar \n2 - Defender \n3 - Ataque especial\n\n'
        else:
                return '\n[white]1 - Atacar \n2 - Defender \n\n'