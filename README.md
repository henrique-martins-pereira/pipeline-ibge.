# 🇧🇷 Pipeline de Dados do IBGE | Python, API REST e SQLite

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um pipeline de dados utilizando Python para consumir informações da API de Localidades do IBGE, realizar a extração e organização dos municípios brasileiros e armazená-los em um banco de dados SQLite.

O objetivo é demonstrar conhecimentos práticos em consumo de APIs REST, manipulação de dados JSON, tratamento de requisições HTTP, organização de informações geográficas e armazenamento em bancos de dados relacionais.

## 🎯 Objetivos

- 🌎 Extrair informações dos estados e municípios brasileiros.
- 🏙️ Identificar os municípios e seus respectivos estados.
- 🗺️ Organizar os dados por região geográfica.
- 🔄 Automatizar a coleta de informações através de requisições HTTP.
- ⚠️ Implementar tratamento de erros e controle de tentativas.
- 🗄️ Armazenar os dados coletados em um banco SQLite.

## 🛠️ Tecnologias e ferramentas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento do pipeline |
| Requests | Consumo da API REST |
| SQLite3 | Armazenamento dos dados |
| JSON | Manipulação dos dados retornados |
| API IBGE | Fonte dos dados geográficos |

## 🔗 Fonte de dados

Os dados são obtidos através da API oficial de Localidades do IBGE.

- [API de Estados](https://servicodados.ibge.gov.br/api/v1/localidades/estados)
- [API de Municípios](https://servicodados.ibge.gov.br/api/v1/localidades/municipios)
- [Documentação oficial](https://servicodados.ibge.gov.br/api/docs/localidades)

## ⚙️ Funcionamento do pipeline

O processo de extração é dividido nas seguintes etapas:

1. **Extração dos estados:** consumo da API do IBGE para obter informações das unidades federativas brasileiras.
2. **Organização dos estados:** criação de um dicionário para relacionar os códigos identificadores aos respectivos estados.
3. **Extração dos municípios:** realização de requisições individuais para obter os municípios de cada estado.
4. **Transformação:** organização dos dados em dicionários contendo município, estado, sigla e região.
5. **Tratamento de erros:** implementação de tentativas de requisição, controle de tempo de espera e tratamento de respostas HTTP, incluindo o status 429.
6. **Armazenamento:** inserção dos registros coletados em um banco de dados SQLite.

## 🗄️ Estrutura do banco de dados

O projeto utiliza uma tabela chamada `municipios`, contendo as seguintes colunas:

| Coluna | Descrição |
|---|---|
| municipio | Nome do município |
| estado | Nome do estado |
| sigla | Sigla da unidade federativa |
| regiao | Região geográfica brasileira |

## 🚀 Como executar o projeto

**1. Clone o repositório**

```bash
git clone URL_DO_SEU_REPOSITORIO
```

**2. Entre na pasta do projeto**

```bash
cd pipeline_ibge
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Execute o pipeline**

```bash
python pipeline_ibge.py
```

Após a execução, o banco de dados `municipios_brasil.db` será criado no diretório do projeto e receberá os registros coletados.

## 📚 Conhecimentos desenvolvidos

- Consumo de APIs REST.
- Requisições HTTP com Python.
- Manipulação de estruturas JSON.
- Listas e dicionários.
- Tratamento de exceções.
- Controle de tentativas e tempo de espera.
- Integração entre Python e SQLite.
- Extração, transformação e armazenamento de dados (ETL).

## 👨‍💻 Autor

Desenvolvido como projeto prático de estudos em Python, APIs e engenharia de dados.

**Objetivo:** desenvolver habilidades práticas em coleta, organização e armazenamento de dados utilizando fontes oficiais.