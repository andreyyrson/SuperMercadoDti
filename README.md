SuperMercadoDti
Este é um projeto desenvolvido como avaliação técnica para a empresa DTI. O objetivo é criar um sistema simples de gerenciamento de produtos de supermercado, utilizando Python e SQLite.

📋 Descrição
O sistema permite o cadastro, visualização, atualização e remoção de produtos em um banco de dados SQLite. A interface é baseada em terminal, proporcionando uma experiência simples e direta para o usuário.

⚙️ Tecnologias Utilizadas
Python 3.x: Linguagem principal do projeto.

SQLite: Banco de dados utilizado para armazenamento dos produtos.

e Logs De Erro Para o Tratamento Eficiente De erros No terminal
Docker: Para containerização da aplicação.

docker compose run --service-ports --rm web Utiize esse Comando Docker Para Captar Inputs 

| Arquivo / Pasta         | Descrição                                            |
| ----------------------- | ---------------------------------------------------- |
| `DataBaseConnection.py` | Gerenciamento da conexão com o banco de dados SQLite |
| `Dockerfile`            | Arquivo para construção da imagem Docker             |
| `InterfaceUsuario.py`   | Interface gráfica do usuário                         |
| `Produto.py`            | Modelo de dados do produto                           |
| `ProdutoDao.py`         | Operações CRUD para produtos                         |
| `SistemaProdutos.py`    | Lógica principal do sistema                          |
| `docker-compose.yml`    | Configuração do Docker Compose                       |
| `main.py`               | Ponto de entrada da aplicação                        |
| `produtos.db`           | Arquivo do banco de dados SQLite                     |
| `requirements.txt`      | Lista de dependências Python                         |
| `README.md`             | Documentação do projeto                              |


🚀 Como Executar
Requisitos
Python 3.x

Docker (opcional, para execução em container)

Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/andreyyrson/SuperMercadoDti.git
cd SuperMercadoDti
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execução
Para rodar a aplicação:

bash
Copiar
Editar
python main.py
Se preferir utilizar Docker:

bash
Copiar
Editar
docker-compose up
