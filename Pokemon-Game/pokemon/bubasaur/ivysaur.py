from implementation.pokemon import Pokemon

class Ivysaur(Pokemon):
    def __init__(self, pokemon: str = 'Ivysaur', hp: int = 115, attack: int = 25, defense: int = 25, special_attack: int = 45, numero_vitorias: int = 1, numero_derrotas: int = 0, level: int = 2, evolucao_ant: str = 'Bubasaur', evolucao_pos: str = 'Venusaur', tipo: str = 'Planta') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)

    ''' Se o número de vitórias for igual a 2, o pokémon evolui a segunda vez e suas características são setadas'''
    def evoluir(self):
        if self.get_numero_vitorias() == 2:
            self.set_pokemon('Venusaur')
            self.set_hp(130)
            self.set_attack(30)
            self.set_defense(30)
            self.set_special_attack(50)
            self.set_level(3)
            self.set_evolucao_ant('Ivysaur')
            self.set_evolucao_pos('-')
            return super().evoluir()

