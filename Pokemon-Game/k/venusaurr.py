from k.ivysaurr import Ivysaur

class Venusaur(Ivysaur):
    def __init__(self, attack, defense, level, evolucao_ant = 'Ivysaur', evolucao_pos = 'None', hp = 50):
        super().__init__(attack, defense, level, hp)

    def Atacar(self):
        return self.get_attack() * self.get_level()

    def Defender(self):
        return self.get_defense() * self.get_level()

    def life_hp(self, rival_attack):
        return super().life_hp(rival_attack)

    def __str__(self):
        return super().__str__()

bb = Venusaur(40, 40, 2)
print(bb)