from ex115.lib.interface import *

def arquivoreal(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro!')
    else:
        print('Arquivo criado com sucesso!')


def readarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro leitura')
    else:
        head('\033[1;34mPESSOAS CADASTRADAS\033[m')
        print(a.read())


def cadastro(arq, nome='none', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome} -- {idade} anos.\n')
        except:
            print('Erro na entrada de dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
