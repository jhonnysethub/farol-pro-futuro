# Projeto Farol pro Futuro

## Visão Geral

O "Farol pro Futuro" é uma aplicação web desenvolvida em Flask e SQLAlchemy para auxiliar estudantes que se sentem perdidos e ansiosos em relação à escolha de carreira. A plataforma oferece um espaço de acolhimento anônimo, uma ferramenta de descoberta de cursos e uma curadoria de recursos de apoio.

---

## Como Executar o Projeto

**Pré-requisitos:**
* Python 3.10+

**Passos para a instalação e execução:**

1.  **Crie e ative um ambiente virtual:**
    ```bash
    # Crie o ambiente (ex: no Windows)
    python -m venv .venv
    # Ative o ambiente (ex: no Windows PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```

2.  **Instale as dependências:**
    Com o ambiente ativado, instale todos os pacotes necessários com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Crie e popule o banco de dados:**
    Os comandos a seguir irão criar o banco de dados `database.db` com a estrutura correta e preenchê-lo com dados de exemplo.
    ```bash
    # Cria as tabelas
    python -c "from app import app, db; app.app_context().push(); db.create_all()"
    
    # Popula com dados iniciais
    python seeds.py
    ```

4.  **Inicie a aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse a aplicação:**
    * Abra seu navegador e acesse: `http://127.0.0.1:5000`
    * Para acessar o painel administrativo, acesse: `http://127.0.0.1:5000/admin`

---

**Equipe:**
* Jhonny Emanoel
* Polyana Maria
* Arthur Moura
* Daniel Victor