'''Importação da interface IPokemon'''
from interface.ipokemon import IPokemon
from pokemon_enum.pokemon_options import PokemonOptions
'''Criação da classe concreta Pokemon que implementa a IPokemon'''
class Pokemon(IPokemon):

    def __init__(self, pokemon: str, hp: int, attack: int, defense: int, special_attack: int, numero_vitorias: int, numero_derrotas: int, level: int, evolucao_ant: str, evolucao_pos: str, tipo: str) -> None: 
        self.__pokemon = pokemon
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__special_attack = special_attack
        self.__numero_vitorias = numero_vitorias
        self.__numero_derrotas = numero_derrotas
        self.__level = level
        self.__evolucao_ant = evolucao_ant
        self.__evolucao_pos = evolucao_pos
        self.__tipo = tipo

    def __str__(self) -> str:
        return '\n---------------------------\nPokémon: {} \nTipo: {} \nHp: {} \nAttack: {} \nDefense: {} \nSpecial attack: {} \nLevel: {}\nVictories: {} \nDefeats: {} \nPrevious evolution: {} \nNext evolution: {}\n---------------------------'.format(self.__pokemon, self.__tipo, self.__hp, self.__attack, self.__defense, self.__special_attack, self.__level, self.__numero_vitorias, self.__numero_derrotas, self.__evolucao_ant, self.__evolucao_pos)

    def atacar(self, rival) -> int:
        if rival.__hp < self.__attack:
            rival.__hp = 0
        else:
            rival.__hp -= self.__attack

    def ataque_especial(self, rival):
        if rival.__hp < self.__special_attack:
            rival.__hp = 0
        else:
            rival.__hp -= self.__special_attack

    def defender(self, rival, is_special_attack: bool = False) -> int:
            
            if is_special_attack:
                if self.__defense > rival.__special_attack:
                    dano = 0
                else:
                    dano  = rival.__special_attack - self.__defense

            else:

                if self.__defense > rival.__attack:
                    dano = 0
                else:
                    dano  = rival.__attack - self.__defense
            
            
            if self.__hp < dano:
                self.__hp = 0
            
            else:
                self.__hp -= dano


    def evoluir(self):
        return 

    def list_options(self, enable_special_attack: bool):
        return PokemonOptions.print_values(enable_special_attack)
        
    '''GETTERS'''

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense
    
    def get_hp(self):
        return self.__hp

    def get_special_attack(self):
        return self.__special_attack
    
    def get_pokemon(self):
        return self.__pokemon

    def get_numero_vitorias(self):
        return self.__numero_vitorias

    def get_numero_derrotas(self):
        return self.__numero_derrotas
    
    def get_level(self) -> int:
        return self.__level

    def get_evolucao_ant(self):
        return self.__evolucao_ant

    def get_evolucao_pos(self):
        return self.__evolucao_pos

    def get_tipo(self):
        return self.__tipo
        
    '''SETTERS'''

    def set_attack(self, attack: int):
        self.__attack = attack
    
    def set_defense(self, defense: int):
        self.__defense = defense
    
    def set_hp(self, hp: int):
        self.__hp = hp
    
    def set_special_attack(self, special_attack: int):
        self.__special_attack = special_attack

    def set_pokemon(self, pokemon: str):
        self.__pokemon = pokemon

    def set_numero_vitorias(self):
        self.__numero_vitorias += 1
        self.evoluir()

    def set_numero_derrotas(self):
        self.__numero_derrotas += 1
    
    def set_level(self, level: int):
        self.__level = level

    def set_evolucao_ant(self, other: str):
        self.__evolucao_ant = other

    def set_evolucao_pos(self, other: str):
        self.__evolucao_pos = other

    def set_tipo(self, other: str):
        self.__tipo = other
    
        

