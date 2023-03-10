from implementation.pokemon import Pokemon

class Wartortle(Pokemon):
    
    def __init__(self, pokemon: str = 'Wartortle', hp: int = 115, attack: int = 25, defense: int = 30, special_attack: int = 40, numero_vitorias: int = 1, numero_derrotas: int = 0, level: int = 2, evolucao_ant: str = 'Squirtle', evolucao_pos: str = 'Blastoise', tipo: str = 'Água') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)

    ''' Se o número de vitórias for igual a 2, o pokémon evolui a segunda vez e suas características são setadas'''
    def evoluir(self):
        if self.get_numero_vitorias() == 2:
            self.set_pokemon('Blastoise')
            self.set_hp(130)
            self.set_attack(30)
            self.set_defense(35)
            self.set_special_attack(50)
            self.set_level(3)
            self.set_evolucao_ant('Wartortle')
            self.set_evolucao_pos('-')
            return super().evoluir()