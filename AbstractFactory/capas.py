from enum import Enum
from abc import ABC, abstractmethod

class TipoDeCapa(Enum):
    DURA = "Capa Dura"
    FLEXIVEL = "Capa Flexível"
    DIGITAL = "Capa Digital"

class Capa(ABC):
    def __init__(self, tipo: TipoDeCapa, cor: str, material: str):
        self._tipo = tipo
        self.cor = cor
        self.material = material

    @abstractmethod
    def obter_tipo(self):
        pass

class CapaDura(Capa):
    def obter_tipo(self):
        return f"{self._tipo.value} {self.cor} (Material: {self.material})"
    
class CapaFlexivel(Capa):
    def obter_tipo(self):
        return f"{self._tipo.value} {self.cor} (Material: {self.material})"
    
class CapaDigital(Capa):
    def obter_tipo(self):
        return f"{self._tipo.value} {self.cor} (Material: {self.material})"
