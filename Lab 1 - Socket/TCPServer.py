from socket import *

HOST = ''
PORT = 15000

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()

try:
  while True:
    data = conn.recv(1024)
    if not data: break

    numeros = data.decode().split(' ')
    operacao = numeros.pop()

    soma = int(numeros[0])
    for numero in numeros[1:]:
        if operacao == '+': soma += int(numero)
        elif operacao == '-': soma -= int(numero)
        elif operacao == '*': soma *= int(numero)
        elif operacao == '/': soma /= int(numero)

    conn.send(str(soma).encode())
finally:
    conn.close()
