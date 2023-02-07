from implementation.pokemon import Pokemon

class Squirtle(Pokemon):
    def __init__(self, pokemon: str = 'Squirtle', hp: int = 100, attack: int = 20, defense: int = 25, special_attack: int = 30, numero_vitorias: int = 0, numero_derrotas: int = 0, level: int = 1, evolucao_ant: str = '-', evolucao_pos: str = 'Wartortle', tipo: str = 'Água') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)

    ''' Se o número de vitórias for igual a 1, o pokémon evolui a primeira vez e suas características são setadas'''
    def evoluir(self):
        if self.get_numero_vitorias() == 1:
            self.set_pokemon('Wartortle')
            self.set_hp(115)
            self.set_attack(25)
            self.set_defense(30)
            self.set_special_attack(40)
            self.set_level(2)
            self.set_evolucao_ant('Squirtle')
            self.set_evolucao_pos('Blastoise')
            return super().evoluir()
        