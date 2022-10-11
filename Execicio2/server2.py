# O servidor deverá ser implementado prevendo a possibilidade de diversas conexões simultâneas. Para tal, deve utilizar uma thread para cada conexão.
# Para cada conexão, o servidor deverá receber CPFs a serem validados. Para cada CPF, ele deve verificar se é composto por caracteres válidos 
# (números, pontos e traço) e se os dígitos de verificação correspondem ao algoritmo abaixo. Os formatos de entrada válidos são: somente números 
# e o formato XXX.XXX.XXX-XX.

from socket import *
from threading import *
s = socket()

# Fazendo conexão com o servidor

servidor = "0.0.0.0"
porta = 1238
s.bind((servidor, porta))
s.listen(10)

def trata_conn(conn, cliente):
    global mutex
    while True:
        cpfs = conn.recv (4096)
        if cpfs == b'':
            break
        cpf=int(cpfs.decode("UTF-8"))
        conn.send(str.encode(f"{cpf}"))
        
    print(f"Fim da conexão")
    conn.close()


print(f"Servidor no ar...")
mutex = Lock()
cont_t = 0

while True:
    (conn, cliente) = s.accept()

    t = Thread(target=trata_conn, args=(conn, cliente))
    t.start()
    cont_t += 1
    print(f"Já disparei {cont_t} threads até agora.")
    