class Servico:
    def __init__(self, id, titulo, categoria, descricao, requisitos, local):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.requisitos = requisitos
        self.local = local

    def exibir_dados(self):
        print("\n========== SERVIÇO ==========")
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Categoria: {self.categoria}")
        print(f"Descrição: {self.descricao}")
        print(f"Requisitos: {self.requisitos}")
        print(f"Local: {self.local}")
        print("=============================")
