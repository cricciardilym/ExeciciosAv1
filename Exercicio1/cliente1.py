from socket import *
# O Cliente deverá solicitar ao usuário uma frase, enviá-la para o servidor,
# receber a frase criptografada e imprimi-la. Em seguida, deve enviar esta
# frase novamente para ser criptografada, receber a resposta do servidor e
# compará-la com a frase original. Caso esteja igual, deverá informar ao
# usuário que a criptografia funciona.
s = socket()

servidor = "127.0.0.1"
porta = 8729

s.connect((servidor, porta))

frase = str(input("Digite uma frase: "))
meusbytes = str.encode(frase, "UTF-8")
s.send(meusbytes)
data = s.recv(4096)
print(f"Frase criptografia: {data.decode()}")
if frase == data:
    print(f"A criptografia funciona")
else:
    print(f"A criptografia não funciona")
