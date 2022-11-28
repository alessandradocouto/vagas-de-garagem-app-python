# App Vagas [em Atualização]

Inseri, altera, remove e mostra informações de quais apartamentos são os carros estacionados em cada vaga do condomínio.


# Tecnologias:

Python, Tkinter, MySQL, Unittest


# O que aprendi

- Entendimento de classes, métodos, atributos de classe e instância

- Testes Unitários de funções de validação de entrada do usuário

- Boas práticas ao utilizar banco de dados relacional(https://medium.com/@alexandre.malavasi/25-dicas-e-boas-pr%C3%A1ticas-de-banco-de-dados-para-desenvolvedores-7a60bfc28f1f),

- Instalar e configurar um banco de dados

- Criar e excluir banco de dados

- Consultas como criar, alterar e excluir tabelas, adicionar foreign key e 
primary key, quando usar DELETE CASCADE e DELETE NULL, utilizar expressões para recuperar informações do banco de dados.


# Pré-requisitos

Python v3.10, VS Code v1.73.1, Linux x64 5.15.0-53-generic


# Utilidade da Aplicação

Condomínio terá conhecimento de quais carros e de quais apartamentos estão usando
as vagas de garagem.


# Regras de Negócio

Cada vaga de garagem é destinado a um morador, pode acontecer de um apartamento 
ter mais de uma vaga, isso vai depender do que consta no contrato de cada imóvel
no ato da compra. 
Há carros na garagem que não pertecem aos moradores de um condomínio, pode ser de parentes ou amigos. É proibido usar vagas sem consentimento do dono, sujeito 
à multa a 3x o valor do salário mínimo.

Uma vaga de garagem é composta pelo nome do morador, o número do apartamento, 
o número da placa do carro, caso tenha um carro, além do telefone. Além disso,
uma placa de carro é formada por 3 letras e 4 caracteres, sendo o segundo uma 
letra de A até J, respectivamente.

# License
MIT
