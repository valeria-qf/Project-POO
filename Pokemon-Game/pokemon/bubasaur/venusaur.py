from implementation.pokemon import Pokemon

class Venusaur(Pokemon):

    def __init__(self, pokemon: str = 'Venusaur', hp: int = 130, attack: int = 30, defense: int = 30, special_attack: int = 50, numero_vitorias: int = 2, numero_derrotas: int = 0, level: int = 3, evolucao_ant: str = 'Ivysaur', evolucao_pos: str = '-', tipo: str = 'Planta') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)
