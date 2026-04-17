# Neste arquivo, você deve definir as classes para os tipos de livros que sua fábrica pode criar.
# Pense neles como os "produtos" concretos.

# 1. Crie uma classe base (ou uma interface) chamada `Livro`.
#    - Ela pode ter um método `obter_tipo()` que as subclasses irão implementar.

# 2. Crie classes concretas que herdam de `Livro`.
#    - Por exemplo, uma classe `Ebook`. O método `obter_tipo()` dela deve retornar "Ebook".
#    - Crie outra classe `LivroFisico`. O método `obter_tipo()` dela deve retornar "Livro Físico".
from enum import Enum, auto
from datetime import date
from abc import ABC, abstractmethod

class TipoDeLivro(Enum):
    EBOOK = auto()
    FISICO = auto()
    AUDIOLIVRO = auto()
    REVISTA = auto()
    MANGA = auto()

class Livro(ABC):
    def __init__(self, titulo: str, autor: str, data_publicacao: date, tamanho: str):
        self._titulo = titulo
        self._autor = autor
        self._data_publicacao = data_publicacao
        self._tamanho = tamanho

    def obter_detalhes(self):
        return f"{self._titulo} por {self._autor}, publicado em {self._data_publicacao}, tamanho: {self._tamanho}"

    @abstractmethod
    def obter_tipo(self):
        pass
    
class Ebook(Livro):
    def obter_tipo(self):
        return "Ebook"

class LivroFisico(Livro):
    def obter_tipo(self):
        return "Livro Físico"

class AudioLivro(Livro):
    def obter_tipo(self):
        return "Audiolivro"

class Revista(Livro):
    def obter_tipo(self):
        return "Revista"

class Manga(Livro):
    def obter_tipo(self):
        return "Mangá"
    
