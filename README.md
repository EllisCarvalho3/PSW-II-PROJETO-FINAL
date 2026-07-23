# PSW-II---PROJETO-FINAL

# Sistema de gestão acadêmica — Xavier Academy

Aplicação web desenvolvida em Django para o gerenciamento de alunos, turmas, professores, instrumentos e matrículas, simulando um produto de software real.

## Tecnologias utilizadas:
- **Python / Django** (com uso estrito de Function-Based Views - FBVs)
- **SQLite** (Banco de dados)
- **Bootstrap** (Front-end e responsividade)

## Requisitos do sistema:
- 5 CRUDs completos com telas de detalhamento (Detail View).
- Autenticação completa utilizando `django.contrib.auth`.
- Modelagem de dados com relacionamentos 1:N e N:N.

---

## Como Executar o Projeto Localmente

Siga os passos abaixo para clonar e rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd xavieracademy

   Crie e ative o ambiente virtual:

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
  
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Crie um superusuário para acessar a área administrativa:**
   ```bash
   python manage.py createsuperuser

6. **Inicie o servidor de desenvolvimento:**
  ```bash
  python manage.py runserver

```
---

## Diagrama de classes
O diagrama de classes detalhando as entidades e tipos de dados está salvo na pasta raiz do projeto como diagrama_classes.pdf
