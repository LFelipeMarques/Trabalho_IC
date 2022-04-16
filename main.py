import modulo as md
import datetime as dt

nome_de_conteudo = input("Insira o nome do arquivo de conteúdo:\n")
nome_de_conteudo += ".txt"

nome_de_comando = input("Insira o nome do arquivo de comandos:\n")
nome_de_comando += ".txt"

with open(nome_de_conteudo) as texto:
    conteudo = str(texto.read())

with open(nome_de_comando) as texto:
    comando = str(texto.read())

md.Executar(conteudo, comando)