from datetime import date
from Factory.fabrica import FabricaDeLivros
from Factory.livros import TipoDeLivro

def main():
    # Chamada direta via classe usando @classmethod
    # Note que agora passamos todos os argumentos que o construtor do Livro exige
    
    meu_ebook = FabricaDeLivros.criar_livro(
        tipo_livro=TipoDeLivro.EBOOK, 
        titulo="O Senhor dos Anéis", 
        autor="J.R.R. Tolkien", 
        data_publicacao=date(1954, 7, 29), 
        tamanho="500 páginas / 60 MB"
    )
    
    meu_livro_fisico = FabricaDeLivros.criar_livro(
        TipoDeLivro.FISICO,
        "O Cortiço",
        "Aluísio Azevedo",
        date(1890, 1, 1),
        "300 páginas"
    )

    meu_audiolivro = FabricaDeLivros.criar_livro(
        TipoDeLivro.AUDIOLIVRO,
        "Duna",
        "Frank Herbert",
        date(1965, 8, 1),
        "10 horas"
    )

    meu_manga = FabricaDeLivros.criar_livro(
        TipoDeLivro.MANGA,
        "One Piece",
        "Eiichiro Oda",
        date(1997, 7, 22),
        "Volume 1"
    )

    print("-" * 30)
    print(f"Tipo 1: {meu_ebook.obter_tipo()}")
    print(f"Detalhes 1: {meu_ebook.obter_detalhes()}")
    print("-" * 30)
    print(f"Tipo 2: {meu_livro_fisico.obter_tipo()}")
    print(f"Detalhes 2: {meu_livro_fisico.obter_detalhes()}")
    print("-" * 30)
    print(f"Tipo 3: {meu_audiolivro.obter_tipo()}")
    print(f"Detalhes 3: {meu_audiolivro.obter_detalhes()}")
    print("-" * 30)
    print(f"Tipo 3: {meu_manga.obter_tipo()}")
    print(f"Detalhes 3: {meu_manga.obter_detalhes()}")
    print("-" * 30)

if __name__ == "__main__":
    main()
