from socket import *
from threading import *

s = socket()
cond = Condition()

# ip onde o servidor aceita requisições, nesse caso todos os da máquina do servidor
servidor = "0.0.0.0"
porta = 8730
s.bind((servidor, porta))
s.listen(10)


def trata_conn(conn, cliente):

    global dict_votos_final
    global mutex
    global contador
    global flag

    while True:

        data = conn.recv(4096)

        if data == b'':
            break
        print(f"Recebi o valor {data.decode()} de {cliente}")
        conn.send(str.encode(f"BRUNO;PEDRO;JOSEFA"))

        data = conn.recv(4096)

        if data == b'':
            break
        resultado_votacao = data.decode()
        print(
            f"Recebi o resultado da votação {resultado_votacao} de {cliente}")

        lista_votos = resultado_votacao.split(";")

        dict_votos_temp = {}
        for string in lista_votos:
            string_split = string.split(':')
            dict_votos_temp[string_split[0]] = int(string_split[1])

        with mutex:
            for opt in dict_votos_final:
                dict_votos_final[opt] += dict_votos_temp[opt]

        str_votos_final = ''
        index = 1
        for opt in dict_votos_final:
            if index == len(dict_votos_final):
                str_votos_final += opt + ':' + str(dict_votos_final[opt])
            else:
                str_votos_final += opt + ':' + str(dict_votos_final[opt]) + ';'

            index += 1

        conn.send(str.encode(str_votos_final))

        with mutex:
            contador += 1
            flag = True
            with cond:
                cond.notify()

    print(f"Fim da conexão")
    conn.close()


def multiplo_de_tres():

    global flag
    global contador

    if contador % 3 == 0 and flag:
        return True
    else:
        return False


def imprime_total():

    global flag
    global dict_votos_final

    while True:
        with cond:
            cond.wait_for(multiplo_de_tres)
            print("Total:")
            print(dict_votos_final)
            flag = False


print(f'Servidor no ar...')

dict_votos_final = {'BRANCOS': 0, 'NULOS': 0,
                    'BRUNO': 0, 'PEDRO': 0, 'JOSEFA': 0}
mutex = Lock()
contador = 0

flag = False

t1 = Thread(target=imprime_total)
t1.start()

while True:

    (conn, cliente) = s.accept()
    t = Thread(target=trata_conn, args=(conn, cliente))
    t.start()
