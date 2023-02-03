from pokemon.bubasaur.ivysaur import Ivysaur

class Venusaur(Ivysaur):

    def __init__(self, pokemon: str = 'Venusaur', hp: int = 130, attack: int = 50, defense: int = 50, special_attack: int = 60, numero_vitorias: int = 3, numero_derrotas: int = 0, level: int = 3, evolucao_ant: str = 'Ivysaur', evolucao_pos: str = '', tipo: str = 'Planta') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)
