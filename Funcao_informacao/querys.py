'''
Como o sqlite3 nao suporta algumas querys , segue detelhado algumas funções de informação

- Define qual conjunto de símbolos e caracteres o banco de dados (ou uma tabela/coluna específica) pode armazenar e como esses caracteres são codificados e representados em bytes. 

select charset(nome_produto) from pedido where id_pedido between 1 and 5;


- Especifica o conjunto de regras que definem como os caracteres são armazenados, comparados e ordenados
SELECT Nome_produto
FROM pedido
ORDER BY nome_produto COLLATE utf8mb4_bin;

- Cada vez que um cliente estabelece uma conexão, o servidor atribui um ID exclusivo a essa sessão
SELECT CONNECTION_ID(); -- Id da propria seção

- Retorna o usuario 
SELECT CURRENT_USER();
select system_user();


- Retorna o database / schema
SELECT DATABASE();
select schema();

- Retorna a versão do sistema
select version();

- Ultimo id de algum insert feito na tabela
SELECT last_insert_id();


'''