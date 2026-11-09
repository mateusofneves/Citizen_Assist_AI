import servico as servico_
from lista_encadeada import ListaEncadeada
from algoritmos import busca_sequencial, insertion_sort
from indicadores import exibir_indicadores


# ==========================================
# FUNÇÕES DE VALIDAÇÃO
# ==========================================

def ler_texto(mensagem):

    while True:

        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Erro: este campo não pode ficar vazio.")


def ler_id(mensagem="Informe o ID: "):

    while True:

        try:

            valor = int(input(mensagem))

            if valor > 0:
                return valor

            print("Erro: o ID deve ser maior que zero.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")


def confirmar(mensagem):

    while True:

        resposta = input(mensagem + " (S/N): ").strip().lower()

        if resposta == "s":
            return True

        if resposta == "n":
            return False

        print("Digite S para sim ou N para não.")


# ==========================================
# 1. CADASTRAR SERVIÇO
# ==========================================

def cadastrar_servico(lista):

    print("\n========== CADASTRAR SERVIÇO ==========")

    id = ler_id()

    # Verifica se o identificador já existe
    if lista.buscar_por_id(id) is not None:

        print("Erro: já existe um serviço com esse ID.")
        return

    titulo = ler_texto("Título: ")
    categoria = ler_texto("Categoria: ")
    descricao = ler_texto("Descrição: ")
    requisitos = ler_texto("Requisitos: ")
    local = ler_texto("Local de atendimento: ")

    novo_servico = servico_.Servico(
        id,
        titulo,
        categoria,
        descricao,
        requisitos,
        local
    )

    if lista.inserir(novo_servico):
        print("Cadastro realizado com sucesso!")


# ==========================================
# 2. CONSULTAR SERVIÇO POR ID
# ==========================================

def consultar_servico(lista):

    print("\n========== CONSULTAR SERVIÇO ==========")

    id = ler_id()

    resultado = busca_sequencial(lista, id)

    if resultado is not None:

        print("\nServiço encontrado:")
        resultado.exibir_dados()

    else:

        print("Nenhum serviço encontrado com esse ID.")


# ==========================================
# 3. PESQUISAR POR TÍTULO OU CATEGORIA
# ==========================================

def pesquisar_servicos(lista):

    print("\n========== PESQUISAR SERVIÇOS ==========")

    print("1 - Pesquisar por título")
    print("2 - Pesquisar por categoria")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        atributo = "titulo"

    elif opcao == "2":
        atributo = "categoria"

    else:
        print("Opção inválida.")
        return

    termo = ler_texto("Digite o termo da pesquisa: ").casefold()

    atual = lista.inicio
    encontrados = 0

    while atual is not None:

        servico = atual.dado

        valor = getattr(servico, atributo)

        if termo in valor.casefold():

            servico.exibir_dados()
            encontrados += 1

        atual = atual.proximo

    if encontrados == 0:

        print("Nenhum serviço encontrado.")

    else:

        print(f"\nTotal de resultados: {encontrados}")


# ==========================================
# 4. ATUALIZAR SERVIÇO
# ==========================================

def atualizar_servico(lista):

    print("\n========== ATUALIZAR SERVIÇO ==========")

    id = ler_id()

    servico = lista.buscar_por_id(id)

    if servico is None:

        print("Serviço não encontrado.")
        return

    print("\nServiço selecionado:")
    servico.exibir_dados()

    print("\nQual informação deseja atualizar?")

    print("1 - Título")
    print("2 - Categoria")
    print("3 - Descrição")
    print("4 - Requisitos")
    print("5 - Local de atendimento")

    campos = {
        "1": "titulo",
        "2": "categoria",
        "3": "descricao",
        "4": "requisitos",
        "5": "local"
    }

    opcao = input("Escolha uma opção: ").strip()

    if opcao not in campos:

        print("Opção inválida.")
        return

    campo = campos[opcao]

    novo_valor = ler_texto("Digite o novo valor: ")

    if lista.atualizar(id, campo, novo_valor):

        print("Serviço atualizado com sucesso!")

    else:

        print("Não foi possível atualizar o serviço.")


# ==========================================
# 5. EXCLUIR SERVIÇO
# ==========================================

def excluir_servico(lista):

    print("\n========== EXCLUIR SERVIÇO ==========")

    id = ler_id()

    servico = lista.buscar_por_id(id)

    if servico is None:

        print("Serviço não encontrado.")
        return

    print("\nServiço selecionado:")
    servico.exibir_dados()

    if confirmar("Deseja realmente excluir este serviço?"):

        if lista.remover(id):

            print("Serviço excluído com sucesso!")

        else:

            print("Erro ao excluir o serviço.")

    else:

        print("Exclusão cancelada.")


# ==========================================
# 6. LISTAR TODOS OS SERVIÇOS
# ==========================================

def listar_servicos(lista):

    print("\n========== TODOS OS SERVIÇOS ==========")

    if lista.inicio is None:

        print("Nenhum serviço cadastrado.")
        return

    lista.exibir_todos()

    print(f"\nTotal de registros: {lista.tamanho}")


# ==========================================
# 7. ORDENAR SERVIÇOS
# ==========================================

def ordenar_servicos(lista):

    print("\n========== ORDENAR SERVIÇOS ==========")

    if lista.inicio is None:

        print("Não existem serviços para ordenar.")
        return

    print("1 - Ordenar por ID")
    print("2 - Ordenar por título")
    print("3 - Ordenar por categoria")

    opcao = input("Escolha uma opção: ").strip()

    criterios = {
        "1": "id",
        "2": "titulo",
        "3": "categoria"
    }

    if opcao not in criterios:

        print("Opção inválida.")
        return

    criterio = criterios[opcao]

    insertion_sort(lista, criterio)

    print("\nServiços ordenados com sucesso!")

    lista.exibir_todos()


# ==========================================
# 8. EXIBIR INDICADORES
# ==========================================

def mostrar_indicadores(lista):

    exibir_indicadores(lista)


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():

    # Inicializa a lista encadeada
    lista = ListaEncadeada()

    while True:

        print("""
================================================
              CITIZEN ASSIST AI
          SISTEMA DE SERVIÇOS PÚBLICOS
================================================

1 - Cadastrar serviço
2 - Consultar serviço por ID
3 - Pesquisar por título ou categoria
4 - Atualizar serviço
5 - Excluir serviço
6 - Listar todos os serviços
7 - Ordenar serviços
8 - Exibir indicadores

0 - Encerrar sistema

================================================
""")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":

            cadastrar_servico(lista)

        elif opcao == "2":

            consultar_servico(lista)

        elif opcao == "3":

            pesquisar_servicos(lista)

        elif opcao == "4":

            atualizar_servico(lista)

        elif opcao == "5":

            excluir_servico(lista)

        elif opcao == "6":

            listar_servicos(lista)

        elif opcao == "7":

            ordenar_servicos(lista)

        elif opcao == "8":

            mostrar_indicadores(lista)

        elif opcao == "0":

            print("\nEncerrando o Citizen Assist AI...")
            print("Obrigado por utilizar o sistema!")
            break

        else:

            print("\nOpção inválida! Tente novamente.")


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

if __name__ == "__main__":

    menu_principal()
