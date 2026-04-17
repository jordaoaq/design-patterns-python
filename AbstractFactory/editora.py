from datetime import date
from abc import ABC, abstractmethod
from Factory import livros # Importa os tipos de livros definidos no pacote Factory
from . import capas

# Interface da Fábrica Abstrata
class FabricaEditora(ABC):
    @abstractmethod
    def criar_livro(self, titulo: str, autor: str, data_publicacao: date, tamanho: str) -> livros.Livro:
        pass
    
    @abstractmethod
    def criar_capa(self, cor: str, material: str) -> capas.Capa:
        pass

# Fábrica Concreta 1: Família Padrão (Livro Físico + Capa Dura)
class EditoraPadrao(FabricaEditora):
    def criar_livro(self, titulo: str, autor: str, data_publicacao: date, tamanho: str) -> livros.LivroFisico:
        return livros.LivroFisico(titulo, autor, data_publicacao, tamanho)
    
    def criar_capa(self, cor: str, material: str) -> capas.CapaDura:
        return capas.CapaDura(capas.TipoDeCapa.DURA, cor, material)

# Fábrica Concreta 2: Família Digital (Ebook + Capa Digital)
class EditoraDigital(FabricaEditora):
    def criar_livro(self, titulo: str, autor: str, data_publicacao: date, tamanho: str) -> livros.Ebook:
        return livros.Ebook(titulo, autor, data_publicacao, tamanho)
    
    def criar_capa(self, cor: str, material: str) -> capas.CapaDigital:
        return capas.CapaDigital(capas.TipoDeCapa.DIGITAL, cor, material)
    
# Fábrica Concreta 3: Variação da Padrao com Capa Flexível
class EditoraLivroFlexivel(EditoraPadrao): # Herda de EditoraPadrao
    # O método criar_livro é herdado e já retorna LivroFisico.
    # Apenas o método criar_capa precisa ser sobrescrito.
    def criar_capa(self, cor: str, material: str) -> capas.CapaFlexivel:
        # Retorna uma capa genérica, sem tipo específico
        return capas.CapaFlexivel(capas.TipoDeCapa.FLEXIVEL, cor, material) 
    
class EditoraAudiolivro(FabricaEditora): 
    def criar_livro(self, titulo: str, autor: str, data_publicacao: date, tamanho: str) -> livros.Livro:
        # Retorna um audiolivro.
        return livros.AudioLivro(titulo, autor, data_publicacao, tamanho)
    
    def criar_capa(self, cor: str, material: str) -> capas.Capa:
        # Audiolivros não têm capa física, mas podemos criar uma capa digital genérica.
        return capas.CapaDigital(capas.TipoDeCapa.DIGITAL, cor, material)

