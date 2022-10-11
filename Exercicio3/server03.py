"""
O servidor deverá ser implementado prevendo a possibilidade de diversas conexões simultâneas. 
Para tal, deve utilizar uma thread para cada conexão.
Para cada conexão, o servidor deverá aguardar a mensagem 1, enviar a mensagem 2 com os 
candidatos previamente configurados no servidor, aguardar a mensagem 3, somar os votos 
enviados àqueles que constam em sua base e retornar essa totalização por meio da mensagem 4.
A porta a ser utilizada pelo servidor será 8729.
A cada 3 urnas apuradas, o servidor deverá imprimir a totalização na tela. 
Este procedimento deve ser independente da execução do resto do servidor.
"""
from socket import *
from threading import *

s = socket()

servidor = "0.0.0.0"
porta = 8729

s.bind((servidor, porta))
s.listen(10)  # ouvindo as conexoes

dict_candidatos = {
    "Caio": 0,
    "Leandro": 0,
    "Nulos": 0,
    "Brancos": 0
}


def trata_conn(conn, cliente):
    while True:
        data = conn.recv(4096)
        if data == b'':
            break
        # print(f"Recebi {data.decode()} de {cliente}")
        s = ''
        for c in dict_candidatos.keys():
            # s+= c + ' : ' + candidatos[c] + ';'
            s += c + ' ; '

        conn.send(str.encode(f"{s}"))

    print(f"Fim da conexão")
    conn.close()


print(f"Servidor no ar..")
cont_t = 0
while True:
    (conn, cliente) = s.accept()

    t = Thread(target=trata_conn, args=(conn, cliente))
    t.start()
    cont_t += 1
    print(f"Já disparei {cont_t} threads até agora")
