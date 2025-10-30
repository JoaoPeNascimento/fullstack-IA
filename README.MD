# Aplicação full-stack desenvolvida com **FastAPI (Python)** no back-end e **React + Vite** no front-end, com integração de **IA para resumo de texto**.

---

## 📋 Visão Geral

A aplicação permite ao usuário digitar um texto e obter um **Resumo**.  
O fluxo completo é o seguinte:

1. O **usuário** insere o texto na interface web.
2. O **front-end** envia o texto ao **back-end** via requisição HTTP (`POST /api/v1/analyze`).
3. O **back-end (FastAPI)** processa o texto — utilizando modelo local.
4. O resultado é retornado em formato JSON e exibido de forma amigável na interface.

---

## ⚙️ Tecnologias Utilizadas

### **Backend**

- 🐍 Python 3.12
- ⚡ FastAPI
- 🧩 Uvicorn
- 🌐 Requests / Transformers (para integração IA)
- 🧱 Estrutura modular (rotas → serviços → clientes externos)
- 🔒 Suporte a variáveis de ambiente e CORS habilitado

### **Frontend**

- ⚛️ React + Vite
- 🎨 CSS / Tailwind
- 🔄 Axios para requisições HTTP
- ⏳ Estados de Loading e tratamento de erros

### **Infraestrutura**

- 🐳 Docker & Docker Compose

---

## 🏗️ Arquitetura do Projeto

```
/backend
│── app/
│ ├── main.py
│ ├── routes/
│ │ ├── healthz.py
│ │ └── analyze.py
│ ├── services/
│ │ └── ai_service.py
│ ├── models/
│ │ └── schemas.py
│ └── utils/
│ └── logger.py
│── requirements.txt
│── Dockerfile

/frontend
│── src/
│ ├── components/
│ │ ├── TextInput.jsx
│ │ ├── SummaryOutput.jsx
│ │ └── Loader.jsx
│ ├── services/
│ │ └── api.js
│ ├── App.jsx
│ ├── App.css
│ ├── index.css
│ └── main.jsx
│── .env
│── Dockerfile

/docker-compose.yml
/README.md
```

---

## 🚀 Como Executar o Projeto

> É necessário ter **Docker** e **Docker Compose** instalados.

### 🧩 Passo 1 — Clonar o Repositório

```
git clone https://github.com/JoaoPeNascimento/fullstack-IA.git
cd nome-do-projeto
```

### 🧩 Passo 2 — Criar arquivo .env

📁 frontend/.env
VITE_API_URL=http://localhost:8000/api/v1

### 🧩 Passo 3 — Subir os containers

docker compose up --build

### 🧩 Passo 4 — Acessar no navegador

Front-end: http://localhost:5173

Back-end (docs): http://localhost:8000/docs

Health check: http://localhost:8000/api/v1/healthz

---

### 🧠 Tarefa de IA Escolhida

🗣️ Resumo de textos

O sistema analisa o texto fornecido e retorna um resumo conciso.

---

### 🧰 Comandos Úteis

Recriar containers:

- docker compose up --build

Parar containers:

- docker compose down

Ver logs:

- docker compose logs -f backend
- docker compose logs -f frontend

## 🧑‍💻 Autor

João Nascimento

Desenvolvedor Full-Stack em formação
