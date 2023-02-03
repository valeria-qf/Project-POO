from k.pokemonn import Pokemon

class Bubassaur(Pokemon):

    def __init__(self, attack, defense, level, hp = 30):
        super().__init__(attack, defense, level, hp)

    def Atacar(self):
        return self.get_attack()

    def Defender(self):
        return self.get_defense()

    def life_hp(self, rival_attack):
        return super().life_hp(rival_attack)

    def __str__(self):
        return super().__str__()
    