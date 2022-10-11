from socket import *
from threading import *

s = socket()

servidor = "127.0.0.1"
porta = 8730
s.connect((servidor, porta))

msgInicial = "CANDIDATOS"

meusbytes = str.encode(msgInicial, "UTF-8")
s.send(meusbytes)

data = s.recv(4096)  # isso é o retorno do servidor
str_candidatos = data.decode()
print(f"O servidor respondeu: Os candidatos são {str_candidatos}")

lista_candidatos = str_candidatos.split(";")

dicionarioCandidatos = {'BRANCOS': 0, 'NULOS': 0}

for cand in lista_candidatos:
    dicionarioCandidatos[cand] = 0

print(dicionarioCandidatos)

str_votos = ''
print('Digite os números de votos...')

index = 1
for opt in dicionarioCandidatos.keys():

    dicionarioCandidatos[opt] = input(f'Número votos {opt}: ')

    if index == len(dicionarioCandidatos):
        str_votos += opt + ':' + dicionarioCandidatos[opt]
    else:
        str_votos += opt + ':' + dicionarioCandidatos[opt] + ';'
    index += 1

msgVotos = str_votos
meusbytes = str.encode(msgVotos, "UTF-8")
s.send(meusbytes)

data = s.recv(4096)  # isso é o retorno do servidor
print(f"O servidor respondeu: {data.decode()}")

s.close()
