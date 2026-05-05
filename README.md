# 📦 Sistema de Controle de Entregas

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![React](https://img.shields.io/badge/React-18.2+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-lightblue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production-brightgreen.svg)

> Sistema completo para gerenciamento de entregas de mercadorias com backend em FastAPI e frontend em React.

## ✨ Demonstração

<div align="center">
  <img src="https://via.placeholder.com/800x400?text=Sistema+de+Controle+de+Entregas" alt="Demonstração do Sistema" width="800">
</div>

## 📋 Sobre o Projeto

O **Sistema de Controle de Entregas** é uma aplicação web full-stack desenvolvida para gerenciar o fluxo de mercadorias, desde o recebimento até a entrega final. O sistema oferece uma interface intuitiva e responsiva, permitindo o controle completo de cada item com seus respectivos dados.

### 🎯 Problema que Resolve

- ✅ Controle manual de entregas perdido em planilhas
- ✅ Dificuldade em rastrear mercadorias por número de série
- ✅ Falta de histórico centralizado
- ✅ Processo lento de atualização de status
- ✅ Ausência de relatórios de itens pendentes

### 🚀 Funcionalidades Principais

#### CRUD Completo
| Operação | Descrição |
|----------|-----------|
| **Create** | Cadastro de novas mercadorias com todos os campos |
| **Read** | Listagem completa com visualização detalhada |
| **Update** | Edição de todos os campos de uma mercadoria |
| **Delete** | Remoção segura com confirmação |

#### Campos Gerenciados
- 🔢 **Nota Fiscal** - Identificador único da nota
- 🔖 **Número de Série** - Código único do produto (validação automática)
- 🏷️ **Modelo** - Especificação do produto
- 📝 **Descrição** - Informações detalhadas (opcional)
- ⚙️ **Configurado** - Status de configuração (Sim/Não)
- 🚚 **Entregue** - Status de entrega (Sim/Não)
- 👤 **Responsável** - Pessoa responsável pela mercadoria
- 📅 **Data de Entrada** - Registro automático da data de cadastro

#### Funcionalidades Especiais
- 🔍 **Validação automática** de número de série duplicado
- 📊 **Relatório** de mercadorias não entregues
- 🎨 **Interface responsiva** (Desktop/Tablet/Mobile)
- 📱 **Design profissional** com Bootstrap 5
- ⚡ **Feedback visual** de ações (sucesso/erro)

## 🛠️ Tecnologias Utilizadas

### Backend
```yaml
Framework: FastAPI 0.104.1
ORM: SQLAlchemy 2.0.23
Validação: Pydantic 2.5.0
Database: SQLite (com suporte a MySQL/PostgreSQL)
Server: Uvicorn 0.24.0
Documentação: Swagger/OpenAPI

### Frontend
Framework: React 18.2.0
UI Library: Bootstrap 5
HTTP Client: Axios
Icons: React Icons
State Management: React Hooks

### Ferramentas de Desenvolvimento
Version Control: Git
Environment: Python venv / Node.js
Code Style: PEP 8 (Python) / ESLint (JS)
API Testing: Postman / Swagger UI


### Estrutura do Banco de Dados
Tabela: mercadorias
├── id (INTEGER) - PK, Auto-incremento
├── nota_fiscal (VARCHAR) - Índice
├── numero_serie (VARCHAR) - Unique, Índice
├── modelo (VARCHAR)
├── descricao (TEXT) - Opcional
├── configurado (BOOLEAN) - Default: false
├── entregue (BOOLEAN) - Default: false
├── responsavel (VARCHAR)
└── data_entrada (DATETIME) - Default: now()

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina:

Python 3.8 ou superior

Node.js 14.0 ou superior

npm 6.0 ou superior (ou yarn)

Git (opcional, para clonar)

### Instalação e Execução
## 🐍 Backend (FastAPI)
``` bash
# 1. Acessar a pasta do backend
cd backend

# 2. Criar ambiente virtual
# Windows:
python -m venv venv
venv\Scripts\activate

# Linux/Mac:
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o servidor
python run.py

# O backend estará rodando em: http://localhost:8000

##⚛️ Frontend (React)
``` bash
# 1. Em um novo terminal, acessar a pasta do frontend
cd frontend

# 2. Instalar dependências
npm install

# 3. Executar o frontend
npm start

# O frontend estará disponível em: http://localhost:3000

### Script Automático (Opcional)
## Windows
´´´bash
# Execute o script de configuração automática
setup.bat

## Linux/Mac
´´´bash
# Dê permissão e execute
chmod +x setup.sh
./setup.sh

### Documentação da API
Após iniciar o backend, acesse a documentação interativa:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

|Endpoints Disponíveis|
|Método 	    Endpoint	                        Descrição	            Autenticação
|POST	    /api/mercadorias/	                Criar nova mercadoria	        ❌
|GET	    /api/mercadorias/	                Listar todas mercadorias	    ❌
|GET	    /api/mercadorias/{id}	            Buscar mercadoria por ID	    ❌
|PUT	    /api/mercadorias/{id}	            Atualizar mercadoria	        ❌
|DELETE	    /api/mercadorias/{id}	            Deletar mercadoria	            ❌
|GET	    /api/relatorios/nao-entregues/	    Listar não entregues	        ❌

### Exemplo de Requisição
´´´ json
POST /api/mercadorias/
Content-Type: application/json

{
  "nota_fiscal": "NF-12345",
  "numero_serie": "SN-001-2024",
  "modelo": "Dell XPS 15",
  "descricao": "Notebook Dell XPS 15, 32GB RAM, 1TB SSD",
  "configurado": false,
  "entregue": false,
  "responsavel": "João Silva"
}

### Exemplo de Resposta
´´´json
{
  "id": 1,
  "nota_fiscal": "NF-12345",
  "numero_serie": "SN-001-2024",
  "modelo": "Dell XPS 15",
  "descricao": "Notebook Dell XPS 15, 32GB RAM, 1TB SSD",
  "configurado": false,
  "entregue": false,
  "responsavel": "João Silva",
  "data_entrada": "2024-01-15T10:30:00"
}

###  Estrutura do Projeto
´´´text
sistema-controle-entregas/
│
├── backend/                    # Backend FastAPI
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Configuração principal
│   │   ├── database.py        # Configuração do BD
│   │   ├── models.py          # Modelos SQLAlchemy
│   │   ├── schemas.py         # Schemas Pydantic
│   │   ├── crud.py            # Operações CRUD
│   │   └── routes.py          # Rotas da API
│   ├── requirements.txt       # Dependências Python
│   ├── run.py                 # Script de execução
│   └── entregas.db            # Banco de dados SQLite
│
├── frontend/                   # Frontend React
│   ├── src/
│   │   ├── components/
│   │   │   ├── MercadoriaForm.js   # Formulário
│   │   │   └── MercadoriaList.js   # Listagem
│   │   ├── services/
│   │   │   └── api.js              # Configuração Axios
│   │   ├── App.js                  # Componente principal
│   │   ├── App.css                 # Estilos
│   │   └── index.js                # Ponto de entrada
│   ├── public/
│   │   └── index.html
│   ├── package.json           # Dependências Node
│   └── README.md
│
├── .gitignore                 # Arquivos ignorados
├── README.md                  # Documentação
├── setup.bat                  # Setup Windows
└── setup.sh                   # Setup Linux/Mac


### Interface do Usuário
## Responsividade
Desktop: Layout completo com tabela detalhada
Tablet: Colunas ajustadas para melhor visualização
Mobile: Cards responsivos para listagem

## Componentes
Navbar: Menu principal com navegação
Tabs: Abas para Listagem/Formulário
Formulário: Campos com validação em tempo real
Tabela: Dados organizados com ações
Modais: Confirmação para exclusão
Alerts: Feedback de ações (sucesso/erro)

### Fluxo de Trabalho
graph LR
    A[Login] --> B[Dashboard]
    B --> C[Cadastrar Mercadoria]
    B --> D[Listar Mercadorias]
    D --> E[Editar]
    D --> F[Excluir]
    D --> G[Visualizar]
    C --> H[Validar Dados]
    H --> I[Salvar no BD]
    I --> D

### Testando a Aplicação
## Teste Manuais Sugeridos
1. Cadastro:
    Criar mercadoria com todos campos
    Tentar criar com número de série duplicado
    Tentar criar sem campos obrigatórios

2. Listagem:
    Verificar ordenação
    Testar responsividade
    Confirmar formatação de datas

3. Edição:
    Alterar status de configurado/entregue
    Modificar responsável
    Atualizar descrição

4. Exclusão:
    Excluir e confirmar remoção
    Cancelar exclusão

### Proximas Melhorias
##Segurança
Autenticação JWT
Login de usuários
Controle de permissões por role
Log de ações dos usuários

##Relatórios
Exportação para Excel/CSV
Geração de PDFs
Dashboard com gráficos
Filtros avançados por período

##Interface
Tema dark/light
Animações suaves
Modo de impressão
Upload de imagens dos produtos

##Performance
Paginação na listagem
Busca com debounce
Cache com React Query
Lazy loading das rotas

##Mobile
PWA (Progressive Web App)
Notificações push
Scanner de código de barras
Versão mobile nativa (React Native)

###Contribuição
Contribuições são o que fazem a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será muito apreciada.
Como Contribuir
Faça um Fork do projeto
Crie sua Feature Branch (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'feat: Add some AmazingFeature')
Push para a Branch (git push origin feature/AmazingFeature)
Abra um Pull Request

## Padrões de Commit
´´´bash
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação de código
refactor: refatoração
test: testes
chore: manutenção

### Licença
Este projeto está sob a licença MIT.

### Autor
Alessandro Camargo
Github: @alessandrocamargo
Linkedin: Alessandro Camargo
Email: alessancamargo@gmail.com


### Agradecimentos
FastAPI - Framework backend incrível
React - Biblioteca frontend revolucionária
Bootstrap - Framework CSS
SQLAlchemy - ORM poderoso
Todos os contribuidores e usuários do projeto

