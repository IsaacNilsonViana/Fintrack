# Fintrack

Sistema de gerenciamento financeiro


## Objetivo da aplicação

V1 de uma aplicação de finanças pessoais com backend.
Escopo atual:

* registrar usuários
* registrar contas
* registrar categorias
* registrar transações
* listar dados
* gerar relatórios simples

Sem frontend por enquanto.
Sem ML por enquanto.
Sem importação de extrato por enquanto.

---

## Stack principal

Backend:

* Python
* FastAPI

Banco:

* PostgreSQL

ORM e migrations:

* SQLAlchemy
* Alembic

Validação:

* Pydantic

Testes:

* pytest

Ambiente:

* virtualenv (`.venv`)

Infra futura:

* Docker
* Docker Compose

Frontend futuro:

* React
* Vite
* Axios

ML futuro:

* pandas
* scikit-learn
* numpy

---

## Estrutura de pastas recomendada

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   ├── category.py
│   │   └── transaction.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── account_schema.py
│   │   ├── category_schema.py
│   │   └── transaction_schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── account_service.py
│   │   ├── category_service.py
│   │   └── transaction_service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   ├── account_routes.py
│   │   ├── category_routes.py
│   │   └── transaction_routes.py
│   └── utils/
├── migrations/
├── tests/
│   ├── test_schema.py
│   ├── test_category_service.py
│   ├── test_account_service.py
│   └── test_transaction_service.py
└── alembic.ini
```

---

## Regras de import

Se estiver rodando comandos  **de dentro de `backend`** , os imports devem começar com:

```python
from app.schemas import ...
from app.models import ...
from app.services.category_service import ...
```

Se rodar da raiz do projeto, os imports mudam.
Para evitar confusão, a recomendação é:

* entrar em `backend`
* rodar tudo dali

---

## Entidades da V1

### User

Campos:

* id
* name
* email
* phone
* password_hash
* created_at

### Account

Campos:

* id
* user_id
* name
* type
* balance
* created_at
* updated_at

### Category

Campos:

* id
* user_id
* name
* type
* created_at

### Transaction

Campos:

* id
* user_id
* account_id
* category_id
* amount
* date
* description
* created_at
* updated_at

---

## Relacionamentos

* User tem muitas Accounts
* User tem muitas Categories
* User tem muitas Transactions
* Account pertence a User
* Category pertence a User
* Transaction pertence a User
* Transaction pertence a Account
* Transaction pertence a Category

---

## Etapas do desenvolvimento

### Etapa 1 — estrutura do projeto

Objetivo:

* criar a estrutura de pastas
* definir padrão de organização

### Etapa 2 — banco e conexão

Objetivo:

* configurar PostgreSQL
* configurar SQLAlchemy
* criar `database.py`

### Etapa 3 — models

Objetivo:

* criar models SQLAlchemy
* definir tabelas
* definir foreign keys
* definir relacionamentos

### Etapa 4 — migrations

Objetivo:

* configurar Alembic
* gerar migrations
* versionar banco

### Etapa 5 — schemas

Objetivo:

* criar schemas Pydantic
* separar Create / Update / Response

Padrão por entidade:

* `Base`
* `Create`
* `Update`
* `Response`

### Etapa 6 — services

Objetivo:

* criar lógica da aplicação
* separar regra de negócio das rotas

Arquivos:

* `user_service.py`
* `account_service.py`
* `category_service.py`
* `transaction_service.py`

CRUD esperado por service:

* create
* get_by_id
* list
* update
* delete

### Etapa 7 — routes

Objetivo:

* expor API REST com FastAPI

Rotas esperadas:

* `/users`
* `/accounts`
* `/categories`
* `/transactions`

### Etapa 8 — relatórios simples

Objetivo:

* saldo por conta
* gastos por categoria
* resumo mensal

### Etapa 9 — testes

Objetivo:

* validar schemas
* validar services
* validar endpoints depois

### Etapa 10 — frontend

Somente depois da API pronta.

### Etapa 11 — evolução futura

* importação CSV
* autenticação JWT
* frontend React
* ML para categorias
* previsão de gastos

---

## O que é schema

Schema é contrato da API.

Serve para:

* validar entrada
* padronizar saída
* separar API do banco

Tipos mais comuns:

* `Create`: entrada para criar
* `Update`: entrada para atualizar
* `Response`: saída da API

---

## O que é service

Service é a lógica da aplicação.

Serve para:

* criar
* buscar
* listar
* atualizar
* deletar
* aplicar regras de negócio

Fluxo:

```text
request
↓
route
↓
service
↓
model/database
↓
response
```

---

## O que ainda faltava no ponto em que você parou

Você ainda  **não tinha criado `category_service.py`** .
Por isso o teste falhou ao tentar importar `create_category`.

Antes de testar service, você precisa:

1. criar o arquivo do service
2. criar a função dentro dele
3. importar essa função no teste

---

## Ordem recomendada para aprender services

1. `category_service.py`
2. `account_service.py`
3. `user_service.py`
4. `transaction_service.py`

Motivo:

* category é o mais simples
* transaction é o mais complexo

---

## Primeiro exercício recomendado em services

Criar só esta função:

* `create_category`

Depois testar com pytest.

Depois fazer:

* `get_category_by_id`
* `list_categories_by_user`

---

## Como rodar testes

Entre em `backend` e rode:

```bash
python -m pytest tests/test_service_create_category.py
```

---

## Requisitos técnicos da V1

Funcionais:

* criar usuário
* criar conta
* criar categoria
* criar transação
* listar transações
* listar contas
* listar categorias
* ver saldo por conta
* ver gasto por categoria

Não funcionais:

* código organizado por camadas
* migrations versionadas
* validação com Pydantic
* testes básicos com pytest

---

## Próximos marcos

### Marco 1

* models prontos
* schemas prontos
* migrations funcionando

### Marco 2

* category service pronto
* account service pronto
* user service pronto
* transaction service pronto

### Marco 3

* rotas CRUD prontas

### Marco 4

* relatórios básicos

### Marco 5

* frontend

---

## O que evitar agora

* JWT antes da V1 básica
* Docker antes do CRUD funcionar
* React antes da API funcionar
* ML antes da V1 estabilizar
* importação CSV antes do CRUD existir

---

## Resumo do estado atual

Você já tinha avançado em:

* estrutura
* models
* schemas
* migrations

Você estava entrando em:

* services

O bloqueio atual não era conceitual.
Era só porque ainda não existia `category_service.py` com `create_category`.

---

## Prompt de continuidade para próxima conversa

Cole isso na próxima conversa:

```text
Estou construindo uma aplicação backend de finanças pessoais V1 com Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Pydantic e pytest.

Estrutura atual:
- backend/app/models
- backend/app/schemas
- backend/app/services
- backend/tests
- migrations funcionando

Já fiz:
- models
- schemas
- banco e migrations

Agora estou começando a camada de services.
Quero seguir passo a passo, aprendendo sozinho.
Quero ajuda apenas na etapa atual, sem receber o projeto inteiro de uma vez.

Minha próxima etapa é criar e entender o primeiro service, começando por category_service.py com create_category.
```

Se quiser, eu também posso transformar esse resumo em um `ROADMAP.md` pronto para você guardar no projeto.
