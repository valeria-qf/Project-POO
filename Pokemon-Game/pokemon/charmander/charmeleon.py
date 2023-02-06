from implementation.pokemon import Pokemon

class Charmeleon(Pokemon):
    
    def __init__(self, pokemon: str = 'Charmeleon', hp: int = 115, attack: int = 30, defense: int = 25, special_attack: int = 40, numero_vitorias: int = 1, numero_derrotas: int = 0, level: int = 2, evolucao_ant: str = 'Charmander', evolucao_pos: str = 'Charizard', tipo: str = 'Fogo') -> None:
        super().__init__(pokemon, hp, attack, defense, special_attack, numero_vitorias, numero_derrotas, level, evolucao_ant, evolucao_pos, tipo)
        
    def evoluir(self):
        if self.get_numero_vitorias() == 2:
            self.set_pokemon('Charizard')
            self.set_hp(130)
            self.set_attack(60)
            self.set_defense(50)
            self.set_special_attack(70)
            self.set_level(3)
            self.set_evolucao_ant('Charmeleon')
            self.set_evolucao_pos('-')
            return super().evoluir()