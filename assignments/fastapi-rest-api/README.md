# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para um catálogo de livros usando FastAPI. Você vai praticar rotas HTTP, validação de dados com Pydantic e respostas apropriadas para recursos encontrados ou inexistentes.

## 📝 Tasks

### 🛠️ Configure e explore a API

#### Descrição
Instale as dependências, complete a configuração básica do código inicial e execute o servidor FastAPI. Explore a documentação interativa gerada pelo framework.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI com o título `Book Catalog API`.
- Iniciar o servidor executando `python starter-code.py`.
- Permitir que a documentação interativa seja acessada em `http://127.0.0.1:8000/docs`.

### 🛠️ Consulte e adicione livros

#### Descrição
Implemente as rotas para listar livros, consultar um livro pelo ID e adicionar um livro ao catálogo. Use os modelos Pydantic fornecidos para validar os dados enviados.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros.
- Implementar `GET /books/{book_id}` para retornar um livro específico ou responder com HTTP 404 quando o ID não existir.
- Implementar `POST /books` para validar e adicionar um livro, atribuindo um ID e respondendo com HTTP 201.
- Manter os livros em memória; os dados podem voltar ao estado inicial quando o servidor reiniciar.

Exemplo de corpo para `POST /books`:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Atualize e remova livros

#### Descrição
Complete as operações de atualização e remoção. Teste tanto os casos de sucesso quanto os IDs inexistentes pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir o título e o autor de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com HTTP 204.
- Responder com HTTP 404 ao tentar atualizar ou remover um livro inexistente.
- Confirmar, usando `GET /books` e `GET /books/{book_id}`, que as operações alteraram o catálogo conforme esperado.