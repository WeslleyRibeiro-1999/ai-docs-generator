# Documentação de Regras de Negócio - Sistema de Autenticação

## Visão Geral
O sistema de autenticação foi desenvolvido para garantir a segurança e controle de acesso a uma aplicação. Ele permite que usuários se cadastrem, façam login e acessem recursos de forma segura. O sistema existe para proteger informações confidenciais e garantir que apenas usuários autorizados tenham acesso.

## Como o Sistema Funciona
1. **Cadastro de Usuários:** Os usuários podem se cadastrar fornecendo nome, sobrenome, e-mail e senha.
2. **Login:** Após o cadastro, os usuários podem fazer login com seu e-mail e senha para acessar a aplicação.
3. **Geração de Token de Acesso:** Após o login bem-sucedido, é gerado um token de acesso que é utilizado para autenticar o usuário em cada requisição subsequente.

## Regras de Negócio
1. **Autenticação de Usuários:**
    - O sistema verifica se o e-mail e a senha fornecidos estão corretos para autenticar o usuário.
    - Se o usuário não existir ou a senha estiver incorreta, o acesso é negado.
2. **Criação de Token de Acesso:**
    - Após autenticar o usuário com sucesso, é gerado um token de acesso com validade para garantir a segurança das informações.
3. **Cadastro de Artigos:**
    - Usuários autenticados podem cadastrar artigos fornecendo título e URL da fonte.

## Casos de Uso Comuns
1. **Cadastro de Novos Usuários:**
    - Novos usuários se cadastram no sistema fornecendo informações pessoais.
2. **Login e Acesso a Recursos:**
    - Usuários autenticados fazem login para acessar recursos protegidos pela aplicação.
3. **Criação de Artigos:**
    - Usuários autenticados podem criar novos artigos para compartilhar informações.

## Termos e Conceitos Importantes
- **Token de Acesso:** É um código gerado após o login do usuário que é utilizado para autenticar as requisições subsequentes.
- **Autenticação:** Processo de verificação da identidade do usuário para garantir acesso seguro.
- **Hash de Senha:** Representação criptografada da senha do usuário para proteger suas informações.

## Possíveis Dúvidas ou Comportamentos Importantes
- **Recuperação de Senha:** Caso o usuário esqueça a senha, é necessário implementar um processo de recuperação seguro.
- **Segurança dos Dados:** Garantir que as informações dos usuários sejam armazenadas de forma segura e protegida.

Com essa documentação, é possível entender o funcionamento e as principais regras de negócio do sistema de autenticação de forma clara e acessível.