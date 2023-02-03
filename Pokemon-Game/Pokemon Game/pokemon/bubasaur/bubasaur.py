from implementation.pokemon import Pokemon

class Bubasaur(Pokemon):
    def __init__(self, pokemon: str = 'Bubasaur', hp: int = 100, attack: int = 30, defense: int = 30, special_attack: int = 40, numero_vitorias: int = 0, numero_derrotas: int = 0, level: int = 1, evolucao_ant: str = '', evolucao_pos: str = 'Ivysaur', tipo: str = 'Planta') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias,  numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)

    def evoluir(self):
        if self.get_numero_vitorias() == 1:
            self.set_pokemon('Ivysaur')
            self.set_hp(115)
            self.set_attack(40)
            self.set_defense(40)
            self.set_special_attack(50)
            self.set_level(2)
            return super().evoluir()
