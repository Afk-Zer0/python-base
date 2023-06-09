#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-------------
Tabua do 2
2
4
...
-------------
"""
__version__ = "0.1.0"
__author__ = "Zero"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11)) 
# Utilizando o range, faz-se N + 1 para obter o número final desejável.

# Iterable (percorriveis)

# Para cada número em números:
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print ("----------")