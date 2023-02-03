from pokemon.squirtle.wartortle import Wartortle

class Blastoise(Wartortle):
    def __init__(self, pokemon: str = 'Blastoise', hp: int = 130, attack: int = 50, defense: int = 60, special_attack: int = 60, numero_vitorias: int = 3, numero_derrotas: int = 0, level: int = 3, tipo: str = 'Água') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, tipo)
        