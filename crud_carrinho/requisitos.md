# Requisitos Funcionais (RF) #
Autenticação
RF01. O sistema deve permitir que um usuário realize cadastro.

RF02. O sistema deve validar se o nome de usuário já está em uso.

RF03. O sistema deve permitir que o usuário realize login.

RF04. O sistema deve permitir que o usuário realize logout.

RF05. O sistema deve restringir o acesso às funcionalidades do carrinho apenas para usuários autenticados.

### Produtos
RF06. O sistema deve exibir uma lista de produtos cadastrados.

RF07. Cada produto deve apresentar nome, descrição e preço

RF08. O sistema deve permitir visualizar os detalhes de um produto.


### Carrinho
RF09. O usuário autenticado deve poder adicionar produtos ao carrinho.

RF10. O sistema deve permitir definir a quantidade de cada produto adicionada ao carrinho.

RF12. O usuário deve poder visualizar todos os produtos presentes no carrinho.

RF13. O sistema deve calcular automaticamente o subtotal de cada item.

RF14. O sistema deve calcular automaticamente o valor total do carrinho.

RF15. O usuário deve poder alterar a quantidade de um produto no carrinho.

RF16. O usuário deve poder remover produtos do carrinho.

RF17. O usuário deve poder esvaziar completamente o carrinho.

RF18. O carrinho deve permanecer associado ao usuário enquanto ele estiver cadastrado.

# Requisitos Não Funcionais (RNF)
RNF01. O sistema deve ser desenvolvido utilizando Python e Flask.

RNF02. O banco de dados utilizado deve ser SQLite.

RNF03. As senhas dos usuários devem ser armazenadas utilizando hash seguro.

RNF04. O sistema deve utilizar autenticação baseada em sessão.

RNF05. As páginas devem responder em até 2 segundos em condições normais.

RNF06. O sistema deve impedir acesso às páginas protegidas sem autenticação.

RNF07. O sistema deve seguir a arquitetura utilizada no tutorial oficial do Flask (Blueprints, templates Jinja, banco SQLite e autenticação).

RNF08. A interface deve ser responsiva para computadores e dispositivos móveis.

RNF09. O sistema deve validar dados de entrada antes de gravá-los no banco.

RNF10. O código deve ser organizado em módulos para facilitar manutenção.

# User Stories
### Cadastro
US01
 Como visitante,
 quero criar uma conta,
 para acessar as funcionalidades do sistema.

US02
 Como usuário,
 quero fazer login,
 para acessar meu carrinho.

US03
 Como usuário,
 quero fazer logout,
 para proteger minha conta.

### Produtos
US04
 Como usuário,
 quero visualizar todos os produtos,
 para escolher quais comprar.

US05
 Como usuário,
 quero visualizar os detalhes de um produto,
 para decidir se desejo adicioná-lo ao carrinho.

### Carrinho
US06
 Como usuário autenticado,
 quero adicionar produtos ao meu carrinho,
 para organizar minhas futuras compras.

US07
 Como usuário autenticado,
 quero definir a quantidade de cada produto,
 para comprar exatamente o que preciso.

US08
 Como usuário autenticado,
 quero alterar a quantidade de um produto no carrinho,
 para ajustar minha compra.

US09
 Como usuário autenticado,
 quero remover um produto do carrinho,
 para desistir da compra daquele item.

US10
 Como usuário autenticado,
 quero visualizar o valor total do carrinho,
 para saber quanto estou gastando.

US11
 Como usuário autenticado,
 quero esvaziar completamente meu carrinho,
 para começar uma nova seleção de produtos.
