# Mini DropBox

Este projeto é uma aplicação web simples desenvolvida em **Flask** que permite **fazer upload, listar e baixar arquivos** armazenados em um bucket da **AWS S3**.  A interface é feita em **HTML + Bootstrap**, com integração direta via **JavaScript (Fetch API)**.

## 🛠️ Tecnologias utilizadas
- **Python 3.12+**
- **Flask** — servidor web
- **Boto3** — SDK da AWS para Python
- **HTML + CSS + Bootstrap**
- **JavaScript (Fetch API)**
- **dotenv** — para armazenar variáveis de ambiente (.env)

## ⚙️ Pré-requisitos
Antes de rodar o projeto localmente, é necessário ter instalado:

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- Uma conta AWS com acesso ao **S3**
- Credenciais de acesso da AWS (Access Key, Secret Key e Session Token)

## 📦 Instalação

1. **Clone este repositório**

```bash
git clone https://github.com/devellen/project-mini-dropbox.git
cd project-mini-dropbox
```
2. **Instale as dependências**

```bash
pip install flask boto3 python-dotenv
```

## 🔑 Configuração das Credenciais AWS
Crie um arquivo chamado **`.env`** na raiz do projeto com o seguinte conteúdo:
``` 
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=SEU_SECRET_KEY
AWS_SESSION_TOKEN=SEU_SESSION_TOKEN
AWS_REGION=SEU-REGION-NAME
S3_BUCKET=NOME-DO-SEU-BUCKET
```
⚠️ **Importante:** essas credenciais expiram após algumas horas se forem de um ambiente de laboratório, então você precisará atualizá-las quando for rodar novamente.

## 🧠 Estrutura do Projeto

```
📁 projeto/
├── app.py               # Código principal do Flask
├── .env                 # Credenciais e variáveis de ambiente
├── requirements.txt      # Lista de dependências (opcional)
└── templates/
     └── index.html        # Interface principal
```

## ▶️ Executando o Projeto

Com o ambiente configurado e o `.env` criado, execute:
```
py app.py
```

O servidor Flask será iniciado em:

`http://127.0.0.1:5000/` 

Abra esse endereço no navegador para acessar a aplicação.
