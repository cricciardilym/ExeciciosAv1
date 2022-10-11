from socket import *
from threading import *

s = socket()

servidor="0.0.0.0"
porta=8729

s.bind((servidor, porta))
s.listen(10) # ouvindo as conexoes


def trata_conn(conn, cliente):
    while True:
        candidatos = {
            "Caio": 0,
            "Leandro": 0,
            "Cesar":0,
            "Nulos":0,
            "Brancos":0
        }
        data=conn.recv(4096)
        if data == b'':
            break
        # print(f"Recebi {data.decode()} de {cliente}")
        s = ''
        # c1 = ''
        for c in candidatos.keys():
            # s+= c + ' : ' + candidatos[c] + ';'
            s+= c + ';'
            # c1+= k
        conn.send(str.encode(f"{s}"))
        
    print(f"Fim da conexão")
    conn.close()

print(f"Servidor no ar..")
cont_t=0
while True:
    (conn, cliente)=s.accept()
    
    t=Thread(target=trata_conn,args=(conn,cliente))
    t.start()
    cont_t+=1
    print(f"Já disparei {cont_t} threads até agora")
   