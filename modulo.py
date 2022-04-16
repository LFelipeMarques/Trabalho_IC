# Algumas coisas que devem ser esperadas:
#
# conteudo := str convertida a partir de conteudo.txt
# comando  := str convertida a partir de comando.txt

from copy import copy as copia
from datetime import datetime as dt

def Agrupar(conteudo):
    # str.split() := lista de "palavras" de str, delimitadas por espaços em branco
    # str1.join(str2) := substitui espaços em branco de str2 por str1

    return ''.join(conteudo.split())

def Maior(conteudo):
    # str.split() := lista de "palavras" de str, delimitadas por espaços em branco
    lista = conteudo.split()

    # palavra_max := variável dummy para fazer comparações
    palavra_max = ""

    for item in lista:
        # quando uma palavra maior é encontrada, a guardamos
        if len(item) > len(palavra_max):
            palavra_max = item

    return palavra_max

def Buscar(conteudo, texto):
    # str.splitlines() := lista de linhas de str
    lista = conteudo.splitlines()

    # ret := variável de retorno, armazena as linhas que têm o texto procurado
    ret = []

    for item in lista:
        if texto in item:
            ret.append(item)

    return ret

def Contar(conteudo, texto):
    # str.split() := lista de "palavras" de str, delimitadas por espaços em branco
    lista = conteudo.split()

    # ret := variável de retorno, armazena a qtd de ocorrências do texto procurado
    ret = 0

    for item in lista:
        # str1.count(str2) := qtd de ocorrências de str2 em str1
        ret += item.count(texto)

    return ret

def Substituir(conteudo, texto_antigo, texto_novo):
    # str1.replace(str2, str3) := substitui as occorrências de str2 em str1 por str3
    texto_substituido = conteudo.replace(texto_antigo, texto_novo)

    return texto_substituido

def Preguica(conteudo):
    # copia(x) := copia "rasa" de x
    cop = copia(conteudo)
    # str.split() := lista de "palavras" de str, delimitadas por espaços em branco
    lista = conteudo.split()

    for item in lista:
        if len(item) > 4:
            cop = cop.replace(item, "", 1)

    return cop

def Achar_comandos(comando):
    # str.split() := lista de "palavras" de str, delimitadas por espaços em branco
    lista = comando.split()

    # ret := variável de retorno, armazena os comandos, em ordem
    ret = []

    N = len(lista)
    # item := iterador dos itens de lista
    for item in range(N):

        # Lista de comandos:
        #
        # 1: Agrupar
        # 2: Maior
        # 3: Buscar
        # 4: Contar
        # 5: Substituir
        # 6: Preguiça

        M = len(lista[item])
        for num in range(M):
            if (num + 7 <= M) and lista[item][num:(num + 7)] == "Agrupar":
                ret.append([1])

            if (num + 5 <= M) and lista[item][num:(num + 5)] == "Maior":
                ret.append([2])

            if (num + 8 <= M) and lista[item][num:(num + 8)] == "Preguiça":
                ret.append([6])

        if len(lista[item]) >= 10 and item <= (N - 3):
            if lista[item][-10:] == "Substituir":
                ret.append([5, lista[item + 1], lista[item + 2]])

        if len(lista[item]) >= 6 and item <= (N - 2):
            if lista[item][-6:] == "Contar":
                ret.append([4, lista[item + 1]])

        if len(lista[item]) >= 6 and item <= (N - 2):
            if lista[item][-6:] == "Buscar":
                ret.append([3, lista[item + 1]])

    return ret

def Executar(conteudo, comando):
    tempo = "%d:%m:%Y %H:%M:%S"
    lista_comandos = Achar_comandos(comando)

    for item in lista_comandos:
        if item[0] == 1:
            print("Agrupar " + dt.now().strftime(tempo))
            print(Agrupar(conteudo))
            print()

        elif item[0] == 2:
            print("Maior " + dt.now().strftime(tempo))
            print(Maior(conteudo))
            print()

        elif item[0] == 3:
            print(f"Buscar {item[1]} " + dt.now().strftime(tempo))
            print("\n".join(Buscar(conteudo, item[1])))
            print()

        elif item[0] == 4:
            print(f"Contar {item[1]} " + dt.now().strftime(tempo))
            print(Contar(conteudo, item[1]))
            print()

        elif item[0] == 5:
            print(f"Substituir {item[1]} {item[2]} " + dt.now().strftime(tempo))
            print(Substituir(conteudo, item[1], item[2]))
            print()

        else:
            print("Preguiça " + dt.now().strftime(tempo))
            print(Preguica(conteudo))
            print()