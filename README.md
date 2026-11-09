# Citizen Assist AI

**Sistema de gerenciamento e consulta de serviços públicos desenvolvido em Python.**

Projeto acadêmico desenvolvido para a Global Solution 2026.2 da FIAP, na disciplina de Data Structures and Algorithms (DSA).

O Citizen Assist AI tem como objetivo organizar informações sobre serviços públicos, permitindo cadastrar, consultar, pesquisar, atualizar, excluir e ordenar registros por meio de uma estrutura de dados implementada manualmente.

## Objetivo do projeto

Desenvolver um protótipo que aplique conceitos de estruturas de dados e algoritmos na organização de informações sobre serviços públicos, demonstrando na prática o funcionamento de uma lista encadeada e de algoritmos de busca e ordenação.

## Funcionalidades

- **Cadastro:** registro de novos serviços públicos.
- **Consulta:** localização de serviços por identificador (ID).
- **Pesquisa:** busca por título ou categoria.
- **Atualização:** alteração das informações dos serviços cadastrados.
- **Exclusão:** remoção de registros da estrutura.
- **Listagem:** exibição de todos os serviços cadastrados.
- **Ordenação:** organização dos registros por ID, título ou categoria.
- **Indicadores:** apresentação da quantidade total de serviços e distribuição por categoria.

## Tecnologias utilizadas

- Python
- Estruturas de Dados
- Lista Encadeada
- Busca Sequencial
- Insertion Sort
- Análise de Complexidade (Big-O)

## Estrutura do projeto

```text
CITIZEN_ASSIST_AI/
│
├── main.py
├── servico.py
├── no.py
├── lista_encadeada.py
├── algoritmos.py
├── indicadores.py
├── README.md
└── .gitignore
```

### Organização dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Menu principal e integração das funcionalidades. |
| `servico.py` | Classe responsável pela representação dos serviços públicos. |
| `no.py` | Implementação dos nós da lista encadeada. |
| `lista_encadeada.py` | Implementação manual das operações da lista encadeada. |
| `algoritmos.py` | Implementação dos algoritmos de busca e ordenação. |
| `indicadores.py` | Cálculo e apresentação dos indicadores. |
| `teste.py` | Testes das funcionalidades iniciais do projeto. |

## Estruturas de dados e algoritmos

### Lista Encadeada

A estrutura principal do sistema é uma lista simplesmente encadeada, implementada manualmente utilizando classes e referências entre nós.

Cada nó armazena:
- Um objeto contendo os dados do serviço.
- Uma referência para o próximo nó da estrutura.

A lista mantém referências para o primeiro e o último elemento, além de um contador de registros.

### Algoritmos implementados

**Busca Sequencial**

Percorre os nós da lista encadeada até encontrar o identificador solicitado ou atingir o final da estrutura.

**Insertion Sort**

Algoritmo de ordenação implementado manualmente, responsável por reorganizar os próprios nós da lista encadeada de acordo com o critério selecionado.

Critérios disponíveis:
- ID;
- Título;
- Categoria.

## Análise de complexidade — Big-O

Considerando `n` como a quantidade de serviços cadastrados:

| Operação | Complexidade |
|---|---|
| Inserção com validação de ID | O(n) |
| Busca por ID | O(n) |
| Pesquisa por título ou categoria | O(n) |
| Atualização | O(n) |
| Remoção | O(n) |
| Listagem | O(n) |
| Insertion Sort | O(n²) no pior caso |
| Indicadores | O(n + k), em média, sendo k o número de categorias distintas |

A inserção no final da lista, isoladamente, possui complexidade O(1), pois a estrutura mantém uma referência para o último nó. Entretanto, a validação de identificadores duplicados torna a operação completa O(n).

O Insertion Sort reorganiza os nós diretamente, utilizando espaço auxiliar O(1).

## Como executar o projeto

### Pré-requisitos

- Python instalado.
- Visual Studio Code ou outro editor de código.
- Terminal para execução.

Não é necessário instalar bibliotecas externas.

### Executando

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Acesse a pasta:

```bash
cd CITIZEN_ASSIST_AI
```

3. Execute o sistema:

```bash
python main.py
```

O menu principal será apresentado no terminal, permitindo acessar todas as funcionalidades.

## Armazenamento dos dados

Nesta versão, os serviços são armazenados em memória por meio da lista encadeada.

Isso significa que os registros são mantidos somente durante a execução do programa e não são preservados após seu encerramento.

## Contexto acadêmico

### Responsáveis envolvidos

**Mateus de Oliveira Fernandes Neves         RM: 572431**
**Nathan Hiroshi Watanabe                    RM: 572806**


**Instituição:** FIAP — Faculdade de Informática e Administração Paulista

**Projeto:** Global Solution 2026.2 — Citizen Assist AI

**Disciplina:** Data Structures and Algorithms (DSA)

---

*Projeto desenvolvido para fins acadêmicos e demonstração prática de estruturas de dados e algoritmos em Python.*