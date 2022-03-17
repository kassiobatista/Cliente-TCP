import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('\033[31mA conexão falhou!!!\033[m')
        print('Erro: {}'.format(e))
        sys.exit()

print('\033[32mSocket criado com sucesso!\033[m')

hostalvo = input('Digite o Host ou IP a ser conectado: ')
portaalvo = input('Digite a porta a ser conectada: ')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect((hostalvo, int(portaalvo)))
    print('\033[32mCliente TCP conectado com sucesso no Host: {} e na porta: {}\033[m'.format(hostalvo, portaalvo))
    s.shutdown(2)
except socket.error as e:
    print('\033[31mNão foi possivel conectar no Host: {} na porta: {}\033[m'.format(hostalvo, portaalvo))
    print('Erro: {}',format(e))
    sys.exit()

if __name__ == '__main__':
    main()