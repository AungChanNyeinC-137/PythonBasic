import socket
LOCALHOST = "127.0.0.1"
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST,PORT))
server.listen(1)
print("Server started") 
print("Waiting for client request..") 
clientConnection, clientAddress = server.accept()
print('Connected client at', clientAddress)
msg = ''
while True:
    data = clientConnection.recv(1024)
    msg = str(data.decode())
    if msg == 'Over':
        print('Connection is over')
        break
    print("Equation is received")
    print()
    result = 0
    operation_list = msg.split()
    oprnd1 = operation_list[0] 
    operation = operation_list[1] 
    oprnd2 = operation_list[2] 
    
    num1 = int(oprnd1)
    num2 = int(oprnd2)

    if operation == '+':
        result = num1 + num2
    
    elif operation == '-':
        result = num1 - num2

    elif operation == '*':
        result = num1 * num2

    elif operation == '/':
        result = num1 / num2
    print('Send the result to the client')
    output = str(result)
    clientConnection.send(output.encode())
    clientConnection.close()
    