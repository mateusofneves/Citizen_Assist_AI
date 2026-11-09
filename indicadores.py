def exibir_indicadores(lista_encadeada):

    total = lista_encadeada.tamanho

    categorias = {}

    atual = lista_encadeada.inicio

    while atual is not None:

        categoria = atual.dado.categoria

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

        atual = atual.proximo

    print("\n========== INDICADORES ==========")

    print(f"Total de serviços: {total}")

    print("\nServiços por categoria:")

    if not categorias:
        print("Nenhum serviço cadastrado.")

    else:
        for categoria, quantidade in categorias.items():
            print(f"{categoria}: {quantidade}")

    print("=================================")
