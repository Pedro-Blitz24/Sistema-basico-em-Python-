def ArqExis(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO!')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO!')
def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('HOUVE UM ERRO AO LER O ARQUIVO')
    else:
        print(a.read())
    finally:
        a.close()
def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('HOUVE UM ERRO NA ABERTURA DO ARQUIVO')
    else:
        try:
            a.write(f'{nome}                 {idade}\n')
        except:
            print('HOUVE UM ERRO AO ESCREVER OS DADOS')
        else:
            print(f'NOVO REGISTRO DE {nome} ADICIONADO')
            a.close()