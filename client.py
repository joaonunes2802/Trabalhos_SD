from rpc import RPCClient

HOST = '0.0.0.0'
PORT = 8080

client = RPCClient(HOST, PORT)

try:
    client.connect()
    
    while True:
        print("Digite a operação desejada:")
        print("+ - Adição;")
        print("- - Subtração;")
        print("* - Multiplicação;")
        print("/ - Divisão;")
        print("q - Encerra o programa.")
        operacao = input("Operação: ")

        if operacao == 'q': break
        if operacao not in ['+', '-', '*', '/']:
            print("Erro: operação inválida")
            continue
                
        numeros = input("Digite os operandos separados por um espaço: ")
        validacao = numeros.split(' ')
        [op1, op2] = validacao

        if len(validacao) > 2:
            print("Erro: digite no máximo 2 números")
            continue

        if not op1.isnumeric() or not op2.isnumeric():
            print('Erro: digite apenas números')
            continue

        if(operacao == '+'): print("Resultado: ", client.add(int(op1), int(op2)))
        elif(operacao == '-'): print("Resultado: ", client.sub(int(op1), int(op2)))
        elif(operacao == '*'): print("Resultado: ", client.mult(int(op1), int(op2)))
        elif(operacao == '/'): print("Resultado: ", client.div(int(op1), int(op2)))
    
except Exception as err:
    print(f"ERRO: {err}")

finally:
    print("Encerrando conexão com o servidor...")
    client.disconnect()