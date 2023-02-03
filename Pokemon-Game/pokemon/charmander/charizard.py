from pokemon.charmander.charmeleon import Charmeleon

class Charizard(Charmeleon):

    def __init__(self, pokemon: str = 'Charizard', hp: int = 130, attack: int = 60, defense: int = 50, special_attack: int = 60, numero_vitorias: int = 2, numero_derrotas: int = 0, level: int = 3, evolucao_ant: str = 'Charmeleon', evolucao_pos: str = '', tipo: str = 'Fogo') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)