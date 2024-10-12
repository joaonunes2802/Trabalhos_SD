from socket import *

HOST = 'localhost'
PORT = 15000

#Criação do Socket do cliente que usará o protocolo TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Escolhe o servidor destino e a porta com a qual o cliente deseja se comunicar
print(f"Conectando ao servidor {HOST}, na porta {PORT}")
clientSocket.connect((HOST,PORT))


try:
    while True:
        print("Digite a operação desejada:")
        print("+ - Adição;")
        print("- - Subtração;")
        print("* - Multiplicação;")
        print("/ - Divisão;")
        print("q - Encerra o programa.")
        operacao = input()

        if operacao == 'q': break
        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida!")
            continue

        print("OBS: Digite no máximo 20 números, separados pela tecla 'espaço'!")
        
        numeros = input()
        validacao = numeros.split(' ')

        if len(validacao) > 20:
            print("Erro!! Digite no máximo 20 números")
            continue

        not_numeric = False
        for operando in validacao:
            if not operando.isnumeric():
                print('Erro!! Digite apenas números')
                not_numeric = True
                break
        
        if not_numeric:
            continue

        dados = numeros + ' ' + operacao
        clientSocket.send(dados.encode())
        resposta = clientSocket.recv(1024)
        print('Resposta: ', resposta.decode())
        
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Exception occured: {e}")
finally:
    print("Encerrando conexão com o servidor...")
    clientSocket.close()