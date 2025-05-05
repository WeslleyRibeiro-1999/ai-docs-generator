# Documentação Técnica

ℹ️ **Resumo Técnico do Serviço**

O serviço consiste em um sistema de pedidos (orders) e usuários (users) desenvolvido em Golang. Ele permite a criação, busca, atualização e exclusão de pedidos e usuários, além de autenticação de usuários. O sistema utiliza o banco de dados MySQL e SQLite, a framework Echo para criação de APIs RESTful e o ORM GORM para interação com o banco de dados.

---

🏗️ **Estrutura do Projeto**

O projeto está dividido em diferentes módulos e pacotes:

- **order**: Módulo responsável pelas operações relacionadas aos pedidos.
- **user**: Módulo responsável pelas operações relacionadas aos usuários.
- **api**: Contém os handlers para os endpoints da API.
- **repository**: Implementa as interfaces de repositório para acesso ao banco de dados.
- **database**: Lida com a conexão e migração do banco de dados.
- **util**: Contém funções utilitárias, como criptografia de senhas.

---

🛠️ **Tecnologias/Frameworks Utilizados**

- Golang
- Echo Framework
- GORM (ORM para Go)
- MySQL
- SQLite

---

📥📤 **Entradas e Saídas**

### Endpoints Principais:

1. **POST /user**: Cria um novo usuário.
   - Parâmetros obrigatórios: Nome, CPF, Email, Número de Telefone, Senha.

2. **GET /user/:id**: Retorna um usuário específico com base no ID.
   - Parâmetro obrigatório: ID do usuário.

3. **GET /users**: Retorna todos os usuários cadastrados.

4. **PUT /user/update**: Atualiza as informações de um usuário.
   - Parâmetros obrigatórios: ID do usuário e novos dados.

5. **DELETE /user**: Deleta um usuário.
   - Parâmetro obrigatório: ID do usuário.

6. **POST /order**: Cria um novo pedido.
   - Parâmetros obrigatórios: ID do usuário, Descrição do Item, Quantidade do Item, Preço do Item.

7. **GET /order/:id**: Retorna um pedido específico com base no ID.
   - Parâmetro obrigatório: ID do pedido.

8. **GET /orders/user/:id**: Retorna todos os pedidos de um usuário específico.
   - Parâmetro obrigatório: ID do usuário.

9. **GET /orders**: Retorna todos os pedidos cadastrados.

10. **PATCH /order**: Atualiza um pedido existente.
    - Parâmetros obrigatórios: ID do pedido e novos dados.

11. **DELETE /order**: Deleta um pedido.
    - Parâmetro obrigatório: ID do pedido.

---

🌀 **Padrões de Projeto Identificados**

- O projeto segue o padrão de arquitetura MVC (Model-View-Controller) para separação de responsabilidades.
- Utilização de interfaces e implementações para garantir a flexibilidade e extensibilidade do código.
- Uso de handlers para tratar as requisições HTTP de forma modular.

---

🚀 **Instruções de Instalação e Execução**

1. Clone o repositório.
2. Certifique-se de ter o Golang instalado.
3. Instale as dependências utilizando o comando `go mod tidy`.
4. Execute o serviço com o comando `go run cmd/main.go`.

---

💻 **Exemplos de Uso**

```bash
# Criar um novo usuário
curl -X POST http://localhost:8080/user -d '{"name": "João", "cpf": "12345678900", "email": "joao@gmail.com", "phone_number": "123456", "password": "teste123"}'

# Buscar todos os usuários
curl http://localhost:8080/users
```

---

🔄 **Diagrama de Fluxo**

```
Entrada (Requisição HTTP) -> Processamento (Handlers) -> Saída (Resposta HTTP)
```

---

🔧 **Sugestões de Melhoria**

- Implementar autenticação JWT para proteger endpoints sensíveis.
- Adicionar validações de entrada para garantir a integridade dos dados.
- Melhorar a documentação do código com comentários explicativos.

---

ℹ️ Espero que essa documentação forneça uma visão abrangente do projeto e ajude no entendimento e uso do sistema. Em caso de dúvidas ou sugestões, não hesite em entrar em contato.