# 📄 Documentação - Projeto Barbearia

## 🔹 Backend (Flask + Swagger + SQLAlchemy)

### Descrição
API RESTful para gerenciar barbeiros, serviços e agendamentos de uma barbearia.

### Estrutura

- `app.py` - Arquivo principal da API.
- `model/` - Contém modelos de dados (Barbeiro, Serviço, Agendamento).
- `schemas/` - Contém schemas de serialização (Marshmallow).
- `logger.py` - Logger de aplicação.
- `barbearia.db` - Banco de dados SQLite.

### Tecnologias

- Python 3
- Flask
- Flasgger (Swagger para documentação automática)
- Flask-CORS
- SQLAlchemy
- Marshmallow

### Endpoints Principais

- `POST /barbeiros` - Cria um novo barbeiro
- `POST /servicos` - Cria um novo serviço
- `POST /agendamentos` - Agenda um novo horário
- `GET /barbeiros` - Lista todos os barbeiros
- `GET /servicos` - Lista todos os serviços
- `GET /agendamentos` - Lista todos os agendamentos
- `DELETE /barbeiros` - Deleta o barbeiros
- `DELETE /servicos` - Deleta o serviços
- `DELETE /agendamentos` - Deleta o agendamentos

### Instalação

# Clone
git clone https://github.com/JoaoHenrique7/MVP-PUC-BACK.git

# Verificar versão do Python
python --version

# Criar o ambiente virutal com o nome "venv"
python -m venv venv

## se PowerShell
venv/Scripts/Activate.ps1

## se CMD
venv/Scripts/activate.bat

# Para sair do ambiente virtual
deactivate

# Para instalar as dependências:
pip install -r requirements.txt

# Para rodar:
python app.py
