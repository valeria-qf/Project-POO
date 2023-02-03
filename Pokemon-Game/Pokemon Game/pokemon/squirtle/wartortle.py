from pokemon.squirtle.squirtle import Squirtle

class Wartortle(Squirtle):
    
    def __init__(self, pokemon: str = 'Wartortle', hp: int = 115, attack: int = 40, defense: int = 50, special_attack: int = 50, numero_vitorias: int = 1, numero_derrotas: int = 0, level: int = 2, evolucao_ant: str = 'Squirtle', evolucao_pos: str = 'Blastoise', tipo: str = 'Água') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)


    def evoluir(self):
        if self.get_numero_vitorias() == 2:
            self.set_pokemon('Blastoise')
            self.set_hp(130)
            self.set_attack(50)
            self.set_defense(60)
            self.set_special_attack(60)
            self.set_level(3)
            return super().evoluir()