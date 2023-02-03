from pokemon.bubasaur.bubasaur import Bubasaur

class Ivysaur(Bubasaur):
    def __init__(self, pokemon: str = 'Ivysaur', hp: int = 115, attack: int = 40, defense: int = 40, special_attack: int = 50, numero_vitorias: int = 1, numero_derrotas: int = 0, level: int = 2, evolucao_ant: str = 'Bubasaur', evolucao_pos: str = 'Venusaur', tipo: str = 'Planta') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)

    def evoluir(self):
        if self.get_numero_vitorias() == 2:
            self.set_pokemon('Venusaur')
            self.set_hp(130)
            self.set_attack(50)
            self.set_defense(50)
            self.set_special_attack(60)
            self.set_level(3)
            return super().evoluir()

