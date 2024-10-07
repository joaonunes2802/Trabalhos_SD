from socket import *

'''def operacao(client, op):
    #Escolha dos numeros
    numeros = input()
    op = str(op)
    dados = numeros + op  #Adiciona o código da operação ao final da string de numeros

    #Envio de dados para o server:
    encoded_message = bytes(dados, "utf-8")
    client.send(encoded_message)

    #Recebimento da resposta do server:
    resposta = client.recv(1024)
    print('Resposta: ', resposta)'''

def client(serverName = 'localhost', serverPort = 15000):
    #Criação do Socket do cliente que usará o protocolo TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Escolhe o servidor destino e a porta com a qual o cliente deseja se comunicar
    print(f"Conectando ao servidor {serverName}, na porta {serverPort}")
    clientSocket.connect((serverName,serverPort))

    
    try:
        while True:
            print("Escolha o número da operação desejada:")
            print("1 - Adição;")
            print("2 - Subtração;")
            print("3 - Multiplicação;")
            print("4 - Divisão;")
            print("5 - Encerra o programa.")
            operacao = input()
            print("OBS: Escolha no máximo 20 números, separados pela tecla 'espaço'!!")
            if operacao == 1:
                #Escolha dos numeros
                numeros = input()
                dados = numeros + ' 1'  #Adiciona 1 ao final da string de numeros para indicar que é para realizar uma adição
                
                #Envio de dados para o server:
                encoded_message = bytes(dados, "utf-8")
                clientSocket.send(encoded_message)

                #Recebimento da resposta do server:
                resposta = clientSocket.recv(1024)
                print('Resposta: ', resposta)

                #Alternativa: operacao(clientSocket, 1)
            elif operacao == 2:
                #Escolha dos numeros
                numeros = input()
                dados = numeros + ' 2'  #Adiciona 2 ao final da string de numeros para indicar que é para realizar uma subtração
                
                #Envio de dados para o server:
                encoded_message = bytes(dados, "utf-8")
                clientSocket.send(encoded_message)

                #Recebimento da resposta do server:
                resposta = clientSocket.recv(1024)
                print ('Resposta: ', resposta)

                #Alternativa: operacao(clientSocket, 2)
            elif operacao == 3:
                #Escolha dos numeros
                numeros = input()
                dados = numeros + ' 3'  #Adiciona 3 ao final da string de numeros para indicar que é para realizar uma multiplicação
                
                #Envio de dados para o server:
                encoded_message = bytes(dados, "utf-8")
                clientSocket.send(encoded_message)

                #Recebimento da resposta do server:
                resposta = clientSocket.recv(1024)
                print ('Resposta: ', resposta)

                #Alternativa: operacao(clientSocket, 3)
            elif operacao == 4:
                #Escolha dos numeros
                numeros = input()
                dados = numeros + ' 4'  #Adiciona 4 ao final da string de numeros para indicar que é para realizar uma divisão
                
                #Envio de dados para o server:
                encoded_message = bytes(dados, "utf-8")
                clientSocket.send(encoded_message)

                #Recebimento da resposta do server:
                resposta = clientSocket.recv(1024)
                print ('Resposta: ', resposta)

                #Alternativa: operacao(clientSocket, 4)
            elif operacao == 5:
                break        
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Exception occured: {e}")
    finally:
        print("Encerrando conexão com o servidor...")
        clientSocket.close()

client()