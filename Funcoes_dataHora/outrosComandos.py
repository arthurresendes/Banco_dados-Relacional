'''
SELECT NOW() -> Retorna a hora atual do server

SELECT GETDATE() -> Retorna a data atual do server

DATETIME -> Tipo de data utilizado para ter data e hora

EXTRACT -> Extra alo especifico de uma seleção SELECT EXTRACT(YEAR FROM data_venda) from VENDEDOR where id = 1 ->
 Traz o ano da data_venda do id 1 podendo mudar em MOUNTH , DOW(Domingo = 0 , Sabado = 6) , HOUR , etc;
 
O strftime é utilizado para formatação de dados, exemplo:
strftime('%d/%m/%Y', data_evento) AS dia_mes_ano,
strftime('%H:%M', data_evento) AS hora_minuto

'''
