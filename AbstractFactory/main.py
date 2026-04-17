"""
Arquivo principal para demonstrar o padrão Abstract Factory.

Cenário: Um cliente, João, quer comprar o livro "Design Patterns" em duas
versões: uma física (premium) para sua coleção e uma digital para ler no tablet.
"""
from datetime import date
from .editora import EditoraLivroFlexivel, EditoraPadrao, EditoraDigital, EditoraAudiolivro

def main():
    """Função principal que executa o cenário de compra."""

    # --- Cenário 1: João compra a versão física (Premium) ---
    print("--- João decide comprar a versão física (Premium) ---")
    
    # Para produtos físicos, usamos a fábrica de editoras premium.
    fabrica_premium = EditoraPadrao()
    
    # A fábrica cria a família de produtos relacionados: livro físico e capa dura.
    livro_fisico = fabrica_premium.criar_livro(
        titulo="A Língua de Fora", 
        autor="Juva Batella", 
        data_publicacao=date(2011, 10, 13), 
        tamanho="272 páginas"
    )
    capa_dura = fabrica_premium.criar_capa(cor="Azul", material="Couro")
    
    # Exibimos os produtos que João "recebeu"
    print(f"Produto: {livro_fisico.obter_detalhes()}")
    print(f"Acabamento: {capa_dura.obter_tipo()}")
    print("-" * 50)

    # --- Cenário 2: João compra a versão digital ---
    print("--- João agora compra a versão digital para seu tablet ---")
    
    # Para produtos digitais, usamos a fábrica de editoras digitais.
    fabrica_digital = EditoraDigital()
    
    # A fábrica cria a outra família de produtos: ebook e capa digital.
    ebook = fabrica_digital.criar_livro(
        titulo="Codigo Limpo", 
        autor="Robert C. Martin", 
        data_publicacao=date(2008, 8, 1), 
        tamanho="5 MB"
    )
    capa_digital = fabrica_digital.criar_capa(cor="Preta", material=".jpg")
    
    # Exibimos os produtos digitais
    print(f"Produto: {ebook.obter_detalhes()}")
    print(f"Acabamento: {capa_digital.obter_tipo()}")
    print("-" * 50)

    #--- Cenário 3: João compra de uma editora Flexível (capa flexível) ---
    print("--- João compra de uma editora Flexível (capa flexível) ---")

    fabrica_flexivel = EditoraLivroFlexivel()

    livro_flexivel = fabrica_flexivel.criar_livro(
        titulo="Design Patterns", 
        autor="GoF", 
        data_publicacao=date(1994, 10, 21), 
        tamanho="Médio"
    )
    capa_flexivel = fabrica_flexivel.criar_capa(cor="Verde", material="Plástico")

    print(f"Produto: {livro_flexivel.obter_detalhes()}")
    print(f"Acabamento: {capa_flexivel.obter_tipo()}")
    print("-" * 50)

#--- Cenário 4: João compra um audiolivro ---
    print("--- João compra por fim um audiolivro ---")

    fabrica_audiolivro = EditoraAudiolivro()

    livro_audiolivro = fabrica_audiolivro.criar_livro(
        titulo="Duna", 
        autor="Frank Herbert", 
        data_publicacao=date(1965, 8, 1), 
        tamanho="10 horas"
    )
    capa_audiolivro = fabrica_audiolivro.criar_capa(cor="Vermelha", material=".png")

    print(f"Produto: {livro_audiolivro.obter_detalhes()}")
    print(f"Acabamento: {capa_audiolivro.obter_tipo()}")
    print("-" * 50)

if __name__ == "__main__":
    main()

