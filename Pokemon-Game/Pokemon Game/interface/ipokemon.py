'''importação do módulo abc'''
from abc import ABC, abstractmethod

'''Criação da Interface Pokemon atravez da implemantação de metodos abstratos e módulo abc'''
class IPokemon(ABC):

    @abstractmethod
    def atacar(self):
       pass

    @abstractmethod
    def ataque_especial(self):
        pass
    
    @abstractmethod
    def defender(self):
        pass

    @abstractmethod
    def evoluir(self):
        pass
