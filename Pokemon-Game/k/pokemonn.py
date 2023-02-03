'''Importação da interface IPokemon'''
from k.pokemon_interface import IPokemon

'''Criação da classe concreta Pokemon que implementa a IPokemon'''
class Pokemon(IPokemon):

    def __init__(self, attack, defense, level, hp):
        self.__attack = attack
        self.__defense = defense
        self.__level = level
        self.__hp = hp
    

    def __str__(self):
        return '\nPokemon: {} \nAttack: {} \nDefense: {} \nLevel {} \nPrevious evolution: {} \nNext evolution: {}'.format(self.__class__.__name__, self.__attack, self.__defense, self.__level,self.__evolucao_ant, self.__evolucao_pos)

    def attack(self):
        self.__attack * self.__level
    
    def defense(self):
        self.__defense * self.__level
    
    def life_hp(self, rival_attack):
        self.__hp -= rival_attack

    def get_attack(self):
        return self.__attack

    def set_attack(self, attack):
        self.__attack = attack

    '''Getters e setters dos atributos'''
    
    def get_defense(self):
        return self.__defense
    def set_defense(self, defense):
        self.__defense = defense
    
    def get_level(self):
        return self.__level
    def set_level(self, level):
        self.__level = level
    
    def get_hp(self):
        return self.__hp
    def set_level(self, hp):
        self.__hp = hp

    def get_evolucao_ant(self):
        return self.__evolucao_ant
    def set_evolucao_ant(self, evolucao_ant):
        self.__evolucao_ant = evolucao_ant

    def get_evolucao_pos(self):
        return self.__evolucao_pos
    def set_evolucao_ant(self, evolucao_pos):
        self.__evolucao_pos = evolucao_pos

        

