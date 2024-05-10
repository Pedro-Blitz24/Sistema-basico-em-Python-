from ferramentasCsub import ArqExis, criararq, cadastrar, lerarq
arq = 'cadastrados.txt'

if not ArqExis(arq):
    criararq(arq)
def menu():
    while True:
        escreva('MENU PRINCIPAL')
        print('1 - ver pessoas cadastradas                ')
        print('2 - cadastrae pessoas                ')
        print('3 - sair do sistema                ')
        try:
            opção = int(input("DIGITE SUA OPÇÃO: "))
            if opção > 3:
                 print('ERRO! NÚMERO MAIOR QUE O PERMITIDO!')
        except:
            print('ERRO! INSIRA UM NÚMERO INTEIRO VALIDO!')
        else:
            if opção == 1:
                escreva('     PESSOAS CADASTRADAS')
                lerarq(arq)
            if opção == 2:
                escreva('    CADASTRAR NOVAS PESSOAS')
                c = int(input('Quantas pessoas quer cadastrar?: '))
                for i in range(0, c):
                    nome = str(input('NOME: '))
                    idade = int(input('IDADE: '))
                    cadastrar(arq, nome, idade)
            if opção == 3:
                break
    escreva('OBRIGADO POR ME USAR :]')
def escreva(msg):
        met = len(msg) // 2
        print('--' * len(msg))
        print(' ' * met, end='')
        print(msg, end='')
        print(' ' * met)
        print('--' * len(msg) )