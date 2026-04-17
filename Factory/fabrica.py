from . import livros

class FabricaDeLivros:
    # Atributo de classe (compartilhado por todas as instâncias, mas acessado via cls)
    _TIPOS_DE_LIVRO = {
        livros.TipoDeLivro.EBOOK: livros.Ebook,
        livros.TipoDeLivro.FISICO: livros.LivroFisico,
        livros.TipoDeLivro.AUDIOLIVRO: livros.AudioLivro,
        livros.TipoDeLivro.REVISTA: livros.Revista,
        livros.TipoDeLivro.MANGA: livros.Manga
    }

    @classmethod
    def criar_livro(cls, tipo_livro, titulo, autor, data_publicacao, tamanho):
        """
        Método de classe que cria um livro sem precisar instanciar a fábrica.
        Os parâmetros são explícitos para garantir a padronização (segurança).
        """
        classe_livro = cls._TIPOS_DE_LIVRO.get(tipo_livro)
        
        if classe_livro:
            return classe_livro(titulo, autor, data_publicacao, tamanho)
        else:
            raise ValueError(f"Tipo de livro '{tipo_livro}' não reconhecido.")
