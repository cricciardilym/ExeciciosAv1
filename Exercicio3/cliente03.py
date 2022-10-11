from socket import *

# O cliente deverá inicialmente enviar uma mensagem para o servidor (mensagem 1) solicitando a relação dos candidatos
# para os quais
# devem ser digitados os votos.
# Deverá aguardar a mensagem 2 e depois de receber a mesma, deverá solicitar ao usuário o número de
# votos de cada candidato, bem como o número de votos nulos e em branco.
# Após a digitação dos dados, o cliente deverá enviar a mensagem 3 com os nomes dos candidatos, exatamente como vieram
# do servidor
# e seus votos, bem como o número de votos brancos e o número de votos nulos.
# O cliente esperará a mensagem 4 para poder imprimir na tela a parcial da apuração.

s = socket()
servidor = "127.0.0.1"
porta = 8729
s.connect((servidor, porta))

candidatos = "CANDIDATOS"
meuscandidatos = str.encode(candidatos, "UTF-8")
s.send(meuscandidatos)
data = s.recv(4096)

print(f"Os candidatos são: {data.decode()}")

s.close()
