from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'curso.txt'

if not arquivoreal(arq):
    criarq(arq)


while True:
    res = menu(['\033[1;34mVER PESSOAS CADASTRADAS\033[m','\033[1;94mCADASTRAR\033[m','\033[1;95mSAIR\033[m'])
    if res == 1:
        #('\033[1;91mPESSOAS CADASTRADAS\033[m')
        readarq(arq)
    elif res == 2:
        head('\033[1;94mCADASTRAR NOVAS PESSOAS\033[m')
        nome = str(input('Nome:'))
        idade = leiainteiro('Idade:')
        cadastro(arq, nome, idade)
    elif res == 3:
        head('\033[1;95mSaindo do Sistema -- Até logo\033[m')
    else:
        print('Erro!')
    sleep(1.5)

