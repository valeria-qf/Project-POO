from enum import Enum
from rich import print

class PokemonOptions(Enum):
    atacar = 1
    defender = 2
    ataque_especial = 3

    def print_your_option(option) -> str:
            return ' escolheu {}'.format(option.name)

    def print_values(enable_special_attack: bool):
        if enable_special_attack:
                return '\n[white]1 - Atacar \n2 - Defender \n3 - Ataque especial\n\n'
        else:
                return '\n[white]1 - Atacar \n2 - Defender \n\n'