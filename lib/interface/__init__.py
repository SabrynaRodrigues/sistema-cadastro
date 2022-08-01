def leiainteiro(n):
    while True:
        try:
            x = int(input(n))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;34mO usuário não preencheu os dados.\033[m')
        else:
            return x


def line(tam=45):
    return '\033[1;95m-\033[m' * tam


def head(txt):
    print(line())
    print(txt.center(45))
    print(line())


def menu(lista):
    head('\033[1;97mMAIN MENU\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;97m{c} -- {item}\033[m')
        c += 1
    print(line())
    opc = leiainteiro('Your option:')
    return opc
