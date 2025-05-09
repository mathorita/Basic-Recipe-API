# 🍽️ Recipe API

API para cadastro, busca e edição de receitas, com controle de proprietário.
API for create, search and edit food recipes, with owner control

## 🚀 Funcionalidades - Functions

- ✅ CRUD completo de receitas - CRUD complete of recipes
- ✅ Filtro por título e ingredientes - Title filter and ingredients filter
- ✅ Paginação de resultados - Pagination of results
- ✅ Permissão: qualquer pessoa pode ver, só o dono edita ou deleta - Permissions: views for any public, but only the owner can edit and delete
- ✅ Interface interativa via Swagger - Swagger interactive interface
- ✅ Campos formatados como lista (ingredientes e descrição) - List formated fields (ingredients and description)
- 🔒 Autenticação por sessão - Session Authentication 

## 🛠️ Tecnologias - Tecnologies

- Python 3.13
- Django 5
- Django REST Framework
- SQLite (dev)

## ▶️ Como rodar localmente - How to run

```bash
git clone https://github.com/seu-usuario/recipe-api.git
cd recipe-api
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
