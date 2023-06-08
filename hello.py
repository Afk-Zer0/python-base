#!/usr/bin/env python3  
"""Hellow World multi línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente. 

Como usar: 

Tenha a variável LANG devidamente configura, ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1" # Metadados
__author__ = "Zero" # Metadados
__license__ = "Unlicense" # Metadados

import os 

current_language = os.getenv ("LANG", "en_US")[:5]
# Snake Case / Pascal Case = CurrentLanguage

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

# if __name__ == "__main__": 
print (msg)  # Built-in

print ("1+1") # Expressão/Expression