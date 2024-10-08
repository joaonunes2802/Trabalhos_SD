from socket import *

def client(serverName = 'localhost', serverPort = 15000):
    #Criação do Socket do cliente que usará o protocolo TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Escolhe o servidor destino e a porta com a qual o cliente deseja se comunicar
    print(f"Conectando ao servidor {serverName}, na porta {serverPort}")
    clientSocket.connect((serverName,serverPort))

    
    try:
        while True:
            print("Escolha o número da operação desejada:")
            print("+ - Adição;")
            print("- - Subtração;")
            print("* - Multiplicação;")
            print("/ - Divisão;")
            print("q - Encerra o programa.")
            operacao = input()

            if(operacao == 'q'): break

            print("OBS: Escolha no máximo 20 números, separados pela tecla 'espaço'!!")
            
            numeros = input()
            validacao = numeros.split(' ')
            palavra = ""
            for operando in validacao:
                palavra += operando
            if palavra.isnumeric() and len(validacao) <= 20:
                dados = numeros + ' ' + operacao
                print(dados)
                clientSocket.send(dados.encode())
                resposta = clientSocket.recv(1024)
                print('Resposta: ', resposta.decode())
            elif not palavra.isnumeric():
                print('Erro!! Digite apenas números')
            elif len(validacao) > 20:
                print("Erro!! Digite no máximo 20 números")
            
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Exception occured: {e}")
    finally:
        print("Encerrando conexão com o servidor...")
        clientSocket.close()

client()