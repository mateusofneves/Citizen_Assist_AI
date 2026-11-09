from servico import Servico
from algoritmos import insertion_sort
from lista_encadeada import ListaEncadeada

# Criando lista encadeada
lista = ListaEncadeada()


# Criando serviços
servico1 = Servico(
    1,
    "Agendamento médico",
    "Saúde",
    "Agendamento de consultas",
    "Cartão SUS",
    "UBS"
)

servico2 = Servico(
    2,
    "Emissão de RG",
    "Documentação",
    "Solicitação de identidade",
    "Certidão de nascimento",
    "Poupatempo"
)


# Inserindo serviços
lista.inserir(servico1)
lista.inserir(servico2)


# Exibindo todos
lista.exibir_todos()


# Buscando pelo ID
resultado = lista.buscar_por_id(1)

if resultado is not None:
    print("\nServiço encontrado:")
    resultado.exibir_dados()


# Atualizando
lista.atualizar(1, "titulo", "Consulta médica atualizada")


# Removendo
lista.remover(2)


# Conferindo o resultado
print("\nLISTA FINAL:")
lista.exibir_todos()

print("\nQuantidade de serviços:", lista.tamanho)

print("\nANTES DA ORDENAÇÃO:")
lista.exibir_todos()

insertion_sort(lista, "id")

print("\nDEPOIS DA ORDENAÇÃO:")
lista.exibir_todos()
