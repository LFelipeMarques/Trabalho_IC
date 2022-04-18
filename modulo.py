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

        if (M >= 7) and lista[item][-7:] == "Agrupar":
            ret.append([1])

        if (M >= 5) and lista[item][-5:] == "Maior":
            ret.append([2])

        if (M >= 8) and lista[item][-8:] == "Preguiça":
            ret.append([6])

        if (M >= 10) and item <= (N - 3):
            if lista[item][-10:] == "Substituir":
                ret.append([5, lista[item + 1], lista[item + 2]])

        if (M >= 6) and item <= (N - 2):
            if lista[item][-6:] == "Contar":
                ret.append([4, lista[item + 1]])

        if (M >= 6) and item <= (N - 2):
            if lista[item][-6:] == "Buscar":
                ret.append([3, lista[item + 1]])

    return ret

def Executar(conteudo, comando):
    # result_func := resultado de cada comando individual
    result_func = ""
    # result_final := resultado acumulado dos comandos
    result_final = []

    tempo = "%d:%m:%Y %H:%M:%S"
    lista_comandos = Achar_comandos(comando)

    for item in lista_comandos:
        if item[0] == 1:
            result_func = "Agrupar " + dt.now().strftime(tempo) + "\n"
            result_func += Agrupar(conteudo) + "\n\n"
            result_final.append(result_func)

        elif item[0] == 2:
            result_func = "Maior " + dt.now().strftime(tempo) + "\n"
            result_func += Maior(conteudo) + "\n\n"
            result_final.append(result_func)

        elif item[0] == 3:
            result_func = f"Buscar {item[1]} " + dt.now().strftime(tempo) + "\n"
            result_func += "".join(Buscar(conteudo, item[1])) + "\n\n"
            result_final.append(result_func)

        elif item[0] == 4:
            result_func = f"Contar {item[1]} " + dt.now().strftime(tempo) + "\n"
            result_func += Contar(conteudo, item[1]) + "\n\n"
            result_final.append(result_func)

        elif item[0] == 5:
            result_func = f"Substituir {item[1]} {item[2]} " + dt.now().strftime(tempo) + "\n"
            result_func += Substituir(conteudo, item[1], item[2]) + "\n\n"
            result_final.append(result_func)

        else:
            result_func = "Preguica " + dt.now().strftime(tempo) + "\n"
            result_func += Preguica(conteudo) + "\n\n"
            result_final.append(result_func)

    return result_final


def Interface():
    opcao = 0
    nome_de_conteudo = 0
    nome_de_comando = 0
    nome_de_saida = "log.txt"
    while opcao != "5":
        opcao = input("\nDigite um dígito para definir a próxima ação:\n1: Escolher arquivo de conteúdo.\n2: Escolher arquivo de comandos.\n3: Defina o nome do arquivo de saída (\"log\" em caso padrão).\n4: Execute o programa.\n5: Sair do programa.\n")
        if opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida. Digite novamente.\n")
            continue
        if opcao == "5":
            print("Fim de programa. Fechando...")
            continue
        if opcao == "1":
            nome_de_conteudo = input("Insira o nome do arquivo de conteúdo:\n")
            if len(nome_de_conteudo) > 3 and nome_de_conteudo[-4:] != ".txt":
                nome_de_conteudo += ".txt"
            continue
        if opcao == "2":
            nome_de_comando = input("Insira o nome do arquivo de comandos:\n")
            if len(nome_de_comando) > 3 and nome_de_comando[-4:] != ".txt":
                nome_de_comando += ".txt"
            continue
        if opcao == "3":
            nome_de_saida = input("Insira o nome do arquivo de saída:\n")
            if len(nome_de_saida) > 3 and nome_de_saida[-4:] != ".txt":
                nome_de_saida += ".txt"
            continue
        if opcao == "4":
            if nome_de_conteudo == 0:
                print("Insira o nome do arquivo de conteúdo antes!\n")
                continue
            if nome_de_comando == 0:
                print("Insira o nome do arquivo de comandos antes!\n")
                continue

            with open(nome_de_conteudo) as texto:
                conteudo = str(texto.read())

            with open(nome_de_comando) as texto:
                comando = str(texto.read())

            if len(conteudo) > 1000:
                print("Arquivo de conteudo possui mais de 1000 caracteres.\nEscolha outro arquivo de conteúdo.\n")
                continue

            resultado = Executar(conteudo, comando)

            #Criar arquivo
            arquivo = open(nome_de_saida, "w+")
            for item in resultado:
                arquivo.write(item)  #Método para escrever no arquivo
            arquivo.close()

            print("Arquivo de saída criado.")