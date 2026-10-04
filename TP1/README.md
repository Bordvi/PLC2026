# TPC1 - Expressões Regulares

## Autor
- Nome: Isaac Maia
- ID: A108489

![](../foto.jpg)

## Resumo
O trabalho desta semana consiste em criar uma expressão regular para capturar strings binárias que não contenham a substring "011".

A regex desenvolvia começar por capturar zero ou várias instâncias de "1". Após isso, podemos encontrar zero ou várias instâncias de "0" ou de "01", essa combinação permite capturar as restantes strings binárias que não contenham "011".

## Resultados
- ```1*(0|01)*```