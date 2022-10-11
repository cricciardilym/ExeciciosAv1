from socket import *
# O Cliente deverá solicitar ao usuário diversos CPFs a serem validados. 
# Para cada CPF, o cliente deverá enviar o CPF para o servidor, 
# receber uma mensagem “VALIDO” ou “INVALIDO” e avisar o usuário se o CPF é válido ou não. 
# Este procedimento deverá ser repetido até que o usuário digite um CPF vazio.
s = socket()

servidor = "127.0.0.1"
porta = 1238

s.connect((servidor, porta))

while True:
    cpf = input("Digite um CPF: ")
    if cpf == "":
        break
    meuscpf = str.encode (cpf, "UTF-8")
    s.send(meuscpf)
    respcpf = s.recv(4096)
    print(f"O CPF é {respcpf}")
s.close()