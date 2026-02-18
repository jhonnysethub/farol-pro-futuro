# 🧭 Farol pro Futuro

> Uma bússola digital para guiar estudantes na jornada de escolha profissional.

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-success)
![Python Version](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey)

## 📖 Visão Geral

O **Farol pro Futuro** é uma aplicação web desenvolvida em Flask e SQLAlchemy para auxiliar estudantes que se sentem perdidos e ansiosos em relação à escolha de carreira. Focando nas áreas de interesse do aluno — e não apenas de forma limitante na nota do ENEM —, a plataforma oferece um espaço de acolhimento anônimo, uma ferramenta de descoberta de cursos e uma curadoria de recursos de apoio.

---

## ✨ Funcionalidades Principais

* **Cápsula do Tempo (Acolhimento Anônimo):** Um espaço seguro para os estudantes registrarem seus desabafos e ansiedades.
* **Sistema de "Friendly Key":** Para recuperar os desabafos posteriormente, o sistema gera senhas amigáveis, seguras e fáceis de memorizar no formato *PALAVRA-NÚMERO-PALAVRA* (ex: `FAROL-452-FUTURO`).
* **Descoberta Guiada de Cursos:** Filtros inteligentes focados nas áreas de interesse do estudante, apresentando oportunidades reais de forma acolhedora.
* **Painel Administrativo:** Interface dedicada para gerenciar, adicionar e editar o catálogo de universidades, campus e cursos no banco de dados.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Flask, Flask-SQLAlchemy
* **Frontend:** HTML5, CSS3, JavaScript, Lucide Icons
* **Banco de Dados:** SQLite
* **Segurança & Configuração:** `python-dotenv` (Gerenciamento de variáveis de ambiente)

---

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos:**
* Python 3.10+
* Git instalado

**Passos para a instalação e execução:**

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/farol-pro-futuro.git](https://github.com/SEU_USUARIO/farol-pro-futuro.git)
   cd farol-pro-futuro
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   # Crie o ambiente (ex: no Windows)
   python -m venv .venv
   
   # Ative o ambiente (ex: no Windows PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   Com o ambiente ativado, instale todos os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente:**
   Crie um arquivo chamado `.env` na raiz do projeto e defina uma chave secreta para a aplicação:
   ```text
   SECRET_KEY=sua-chave-secreta-aqui
   ```

5. **Crie e popule o banco de dados:**
   Os comandos a seguir irão criar o banco de dados `database.db` com a estrutura correta e preenchê-lo com dados de exemplo.
   ```bash
   # Cria as tabelas
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   
   # Popula com dados iniciais
   python seeds.py
   ```

6. **Inicie a aplicação:**
   ```bash
   python app.py
   ```

7. **Acesse a aplicação:**
   * Aplicação principal: `http://127.0.0.1:5000`
   * Painel administrativo: `http://127.0.0.1:5000/admin`

---

## 📸 Capturas de Tela

<img width="1919" height="1079" alt="Captura de tela 2026-02-17 233753" src="https://github.com/user-attachments/assets/0294f84a-30ce-4c0b-b323-682c841e2ab6" />
<img width="1902" height="1075" alt="Captura de tela 2026-02-17 233810" src="https://github.com/user-attachments/assets/80e67999-55cc-49a5-886f-c92809a61af3" />
<img width="1902" height="1079" alt="Captura de tela 2026-02-17 233850" src="https://github.com/user-attachments/assets/529c3700-5bc2-4cc1-a53e-3ce0dc37e42c" />
<img width="1901" height="1079" alt="Captura de tela 2026-02-17 233859" src="https://github.com/user-attachments/assets/fea8e9ff-2506-40ed-820a-d396369f5c5b" />
<img width="1919" height="1079" alt="Captura de tela 2026-02-17 233928" src="https://github.com/user-attachments/assets/0d9eb932-ead6-4448-a244-afb6d87e2fcd" />
<img width="1903" height="1079" alt="Captura de tela 2026-02-17 234022" src="https://github.com/user-attachments/assets/85cf5d65-b9c1-4ffd-8552-78115474da18" />

---

## 👥 Equipe

* Jhonny Emanoel
* Polyana Maria
* Arthur Moura
* Daniel Victor
