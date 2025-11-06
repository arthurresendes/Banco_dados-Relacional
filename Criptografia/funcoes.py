'''

MD5 até 128 bits
update pedido
SET nome_criptografado = md5(nome_produto)
where id_pedido between 1 and 10;

SHA até 160 bits
update pedido
SET nome_criptografado = SHA(nome_produto)
where id_pedido between 1 and 10;

SH2 depende do hash
update pedido
SET nome_criptografado = SH2(nome_produto)
where id_pedido between 1 and 10;

'''