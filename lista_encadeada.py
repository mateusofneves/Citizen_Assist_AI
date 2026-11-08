from no import No

class ListaEncadeada:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # INSERIR SERVIÇO
    def inserir(self, servico):

        # Verifica se o ID já existe
        if self.buscar_por_id(servico.id) is not None:
            print("Erro: já existe um serviço com esse ID.")
            return False

        novo_no = No(servico)

        # Caso a lista esteja vazia
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no

        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

        self.tamanho += 1

        print("Serviço cadastrado com sucesso!")
        return True

    # BUSCAR POR ID
    def buscar_por_id(self, id):

        atual = self.inicio

        while atual is not None:

            if atual.dado.id == id:
                return atual.dado

            atual = atual.proximo

        return None

    # PESQUISAR POR TÍTULO OU CATEGORIA
    def pesquisar(self, atributo, valor):

        atributos_permitidos = ("titulo", "categoria")

        if atributo not in atributos_permitidos:
            return None

        atual = self.inicio

        while atual is not None:

            dado = getattr(atual.dado, atributo)

            if valor.lower() in dado.lower():
                return atual.dado

            atual = atual.proximo

        return None

    # ATUALIZAR SERVIÇO
    def atualizar(self, id, campo, novo_valor):

        campos_permitidos = (
            "titulo",
            "categoria",
            "descricao",
            "requisitos",
            "local"
        )

        if campo not in campos_permitidos:
            return False

        servico = self.buscar_por_id(id)

        if servico is None:
            return False

        setattr(servico, campo, novo_valor)

        return True

    # REMOVER SERVIÇO
    def remover(self, id):

        atual = self.inicio
        anterior = None

        while atual is not None:

            if atual.dado.id == id:

                # Remoção do primeiro nó
                if anterior is None:
                    self.inicio = atual.proximo

                else:
                    anterior.proximo = atual.proximo

                # Atualiza o último nó
                if atual == self.fim:
                    self.fim = anterior

                self.tamanho -= 1

                # Se a lista ficou vazia
                if self.inicio is None:
                    self.fim = None

                return True

            anterior = atual
            atual = atual.proximo

        return False

    # EXIBIR TODOS OS SERVIÇOS
    def exibir_todos(self):

        if self.inicio is None:
            print("Nenhum serviço cadastrado.")
            return

        atual = self.inicio

        while atual is not None:

            atual.dado.exibir_dados()

            atual = atual.proximo
