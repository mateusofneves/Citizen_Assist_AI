# INSERTION SORT
def busca_sequencial(lista_encadeada, id):

    atual = lista_encadeada.inicio

    while atual is not None:

        if atual.dado.id == id:
            return atual.dado

        atual = atual.proximo

    return None


def insertion_sort(lista_encadeada, criterio="titulo"):

    # Critérios permitidos para ordenação
    criterios = ("id", "titulo", "categoria")

    if criterio not in criterios:
        raise ValueError("Critério de ordenação inválido.")

    # Se tiver zero ou um elemento, já está ordenada
    if lista_encadeada.inicio is None:
        return

    if lista_encadeada.inicio.proximo is None:
        return

    ordenada = None
    atual = lista_encadeada.inicio

    while atual is not None:

        proximo = atual.proximo

        # Obtém o valor utilizado na comparação
        if criterio == "id":
            chave = atual.dado.id
        else:
            chave = getattr(atual.dado, criterio).casefold()

        # Insere o primeiro elemento da lista ordenada
        if ordenada is None:

            atual.proximo = None
            ordenada = atual

        else:

            if criterio == "id":
                chave_inicio = ordenada.dado.id
            else:
                chave_inicio = getattr(
                    ordenada.dado, criterio
                ).casefold()

            # Insere no início quando necessário
            if chave < chave_inicio:

                atual.proximo = ordenada
                ordenada = atual

            else:

                anterior = ordenada

                while anterior.proximo is not None:

                    if criterio == "id":
                        chave_proximo = anterior.proximo.dado.id
                    else:
                        chave_proximo = getattr(
                            anterior.proximo.dado, criterio
                        ).casefold()

                    if chave_proximo > chave:
                        break

                    anterior = anterior.proximo

                atual.proximo = anterior.proximo
                anterior.proximo = atual

        atual = proximo

    # Atualiza o início da lista
    lista_encadeada.inicio = ordenada

    # Recalcula o último nó
    atual = lista_encadeada.inicio

    while atual.proximo is not None:
        atual = atual.proximo

    lista_encadeada.fim = atual
