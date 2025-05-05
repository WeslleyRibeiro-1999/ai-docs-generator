# Documentação do Sistema

## Visão geral
O sistema é responsável por gerenciar pedidos de compra, permitindo a criação, atualização, exclusão e consulta de pedidos. Além disso, também é possível buscar todos os pedidos de um determinado usuário.

## Como o sistema funciona
1. O usuário acessa a aplicação e interage através de requisições HTTP.
2. As requisições são tratadas pelo sistema, que se comunica com o banco de dados para realizar as operações necessárias.
3. O sistema retorna as respostas das requisições de acordo com as operações realizadas.

## Regras de negócio
- **Criar Pedido**: Permite que um usuário crie um novo pedido de compra, informando a descrição do item, a quantidade e o preço.
- **Atualizar Pedido**: Possibilita a atualização de um pedido existente, alterando a quantidade e/ou o preço do item.
- **Excluir Pedido**: Permite a exclusão de um pedido específico.
- **Consultar Pedido**: Permite a consulta de um pedido pelo seu ID.
- **Consultar Pedidos por Usuário**: Permite buscar todos os pedidos de um usuário específico.

## Casos de uso comuns
- Um usuário cria um novo pedido de compra.
- Um usuário atualiza a quantidade de um item em um pedido.
- Um usuário exclui um pedido.
- Um usuário consulta os detalhes de um pedido específico.
- Um usuário visualiza todos os pedidos que realizou.

## Termos e conceitos importantes
- **Pedido**: Representa uma solicitação de compra de um item.
- **Usuário**: Pessoa que interage com o sistema, criando, atualizando e consultando pedidos.
- **Descrição do Item**: Informação sobre o que está sendo comprado.
- **Quantidade**: Número de itens solicitados no pedido.
- **Preço**: Valor unitário do item.

## Dúvidas comuns ou comportamentos importantes
- **Autenticação**: O sistema não contempla autenticação de usuários.
- **Segurança**: Não há informações sobre medidas de segurança adicionais implementadas.

## Diagrama de Fluxo (ASCII)

```
+------------------+       +-----------------+       +-------------------+
|                  |       |                 |       |                   |
|   Criar Pedido   +------->   Atualizar      +------->   Excluir Pedido   |
|                  |       |     Pedido      |       |                   |
+--------+---------+       +--------+--------+       +---------+---------+
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
         |                        |                           |
+--------v---------+       +--------v--------+       +---------v---------+
|                  |       |                 |       |                   |
| Consultar Pedido +-------> Consultar Pedidos+-------> Pedidos por Usuário|
|                  |       |                 |       |                   |
+------------------+       +-----------------+       +-------------------+
```