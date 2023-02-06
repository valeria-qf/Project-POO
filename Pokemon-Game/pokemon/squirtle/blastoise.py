from implementation.pokemon import Pokemon

class Blastoise(Pokemon):
    def __init__(self, pokemon: str = 'Blastoise', hp: int = 130, attack: int = 50, defense: int = 60, special_attack: int = 60, numero_vitorias: int = 3, numero_derrotas: int = 0, level: int = 3, tipo: str = 'Água', evolucao_ant = 'Wartortle', evolucao_pos = '-') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, tipo, evolucao_ant, evolucao_pos)
        