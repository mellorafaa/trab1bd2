# Sistema de Gerenciamento de Adoção de Pets com MongoDB

### Trabalho: Modelagem Não-Relacional – Parte 01
### Turma: 31  
### Integrantes do Grupo: Helena Pacheco e Rafaela Mello

## Descrição do Projeto

Este projeto tem como objetivo o desenvolvimento de uma aplicação para gerenciamento de um sistema de adoção de pets, utilizando a linguagem Python e o banco de dados NoSQL MongoDB.

A proposta contempla o armazenamento e controle de informações relacionadas aos pets disponíveis para adoção, seus tutores, os adotantes interessados, além do histórico de rastreabilidade e acompanhamento dos animais após a adoção.

## Estrutura do Banco de Dados

O banco de dados utilizado chama-se `pet_adocao`, estruturado em três coleções principais:

- Tutores: contém informações dos responsáveis pelos pets antes da adoção (ex.: nome e contato);
- Pets: armazena dados dos animais, como nome, espécie, raça, porte, idade, status de adoção, saúde, comportamento, rastreabilidade e acompanhamento pós-adoção;
- Adotantes: guarda informações dos interessados, incluindo preferências de adoção e pets já adotados.

## Funcionalidades da Aplicação

- Cadastro de tutores, adotantes e pets.
- Atualização automática do status do pet após a adoção.
- Registro completo do histórico de rastreabilidade (locais por onde o pet passou).
- Acompanhamento pós-adoção, com eventos e datas registradas.
- Consulta de compatibilidade entre pets e adotantes com base em:
  - Porte
  - Espécie
  - Sexo
  - Doenças crônicas
  - Aceitação de necessidades especiais
  - Tempo disponível do adotante
  - Comportamento do pet
- Listagem de pets disponíveis para adoção.
- Consulta de pets adotados por um determinado usuário.

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org)
- [MongoDB](https://www.mongodb.com/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)

## Instalação e Execução

1. Certifique-se de ter o Python 3.10 ou superior instalado.
2. Instale o MongoDB e inicie o servidor local.
3. Instale as dependências do Python com:
    pip install pymongo
4. Execute o script principal do projeto:
    python inicializa_bd.py
5. Os relatórios serão apresentados no terminal da IDE utilizada para execução do script, e o banco será populado por conta do script