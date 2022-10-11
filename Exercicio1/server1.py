# O servidor deverá ser implementado prevendo a possibilidade de diversas conexões simultâneas.
# Para tal, deve utilizar uma thread para cada conexão.
# Para cada conexão, o servidor deverá receber frases a serem criptografadas. Para cada frase,
# ele deve criptografar utilizando o algoritmo de criptografía POLAR/ZENIT. A frase criptografada
# deve ser enviada de volta ao cliente.
# A porta a ser utilizada pelo servidor será 8729.
from socket import *
from threading import *
s = socket()

# Fazendo conexão com o servidor

servidor = "0.0.0.0"
porta = 8729
s.bind((servidor, porta))
s.listen(10)


def trata_conn(conn, cliente):
    global mutex

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
