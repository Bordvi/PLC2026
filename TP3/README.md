# TPC3 - Analisador Léxico

## Autor
- Nome: Isaac Maia
- ID: A108489

![](../foto.jpg)

## Resumo
O trabalho desta semana consiste em desenvolver, em Python, um analisador léxico para a linguagem de query SPARQL, tendo em conta o seguinte exemplo:

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000

```
Os tokens foram definidos num ficheiro JSON através de expressões regulares. Os tokens cobrem os seguintes casos:
- Comentários;
- Variáveis;
- Identificadores de língua;
- Strings;
- Conceitos;
- Delimitadores;
- Palavras reservadas (limit, select e where);
- Valores numéricos.

Em seguida, utilizei o gerador de analisadores léxicos fornecido no notebook da aula T4 para gerar o analisador léxico, contudo alterei o código para que os comentários fossem ignorados conforme era pedido no enunciado.

Usando o exemplo fornecido como input do analisador léxico, obtemos:

```
('SELECT', 'select', 1, (0, 6))
('VAR', '?nome', 1, (7, 12))
('VAR', '?desc', 1, (13, 18))
('WHERE', 'where', 1, (19, 24))
('DELIMITER', '{', 1, (25, 26))
('VAR', '?s', 1, (4, 6))
('CONCEPT', 'a', 1, (7, 8))
('CONCEPT', 'dbo:MusicalArtist', 1, (9, 26))
('DELIMITER', '.', 1, (26, 27))
('VAR', '?s', 1, (4, 6))
('CONCEPT', 'foaf:name', 1, (7, 16))
('STR', '"Chuck Berry"', 1, (17, 30))
('LANGUAGE', '@en', 1, (30, 33))
('DELIMITER', '.', 1, (34, 35))
('VAR', '?w', 1, (4, 6))
('CONCEPT', 'dbo:artist', 1, (7, 17))
('VAR', '?s', 1, (18, 20))
('DELIMITER', '.', 1, (20, 21))
('VAR', '?w', 1, (4, 6))
('CONCEPT', 'foaf:name', 1, (7, 16))
('VAR', '?nome', 1, (17, 22))
('DELIMITER', '.', 1, (22, 23))
('VAR', '?w', 1, (4, 6))
('CONCEPT', 'dbo:abstract', 1, (7, 19))
('VAR', '?desc', 1, (20, 25))
('DELIMITER', '}', 1, (0, 1))
('LIMIT', 'LIMIT', 1, (2, 7))
('INT', '1000', 1, (8, 12))
```
Através deste resultado podemos verificar que o analisador léxico está a reconhecer os tokens fornecidos. Contudo, a informação relativa às linhas não está correta, uma vez que todos os tokens estão a ser identificados como pertencentes à linha 1.
Isto acontece, pois o texto está a ser processado linha a linha e por isso o contador é reiniciado a cada linha processada.

## Resultados
- [Gerador do Tokenizer](gen_tokenizer.py)
- [Tokens](tokens.json)
- [Tokenizer](tokenizer.py)