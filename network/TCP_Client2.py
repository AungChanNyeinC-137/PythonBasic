import socket
SERVER = '127.0.0.1'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
while True:
    print('Example 5 + 6')
    inp = input("Enter the operation in the form opreand operator oprenad: ")
    if inp == 'Over':
        break
    client.send(inp.encode())
    answer = client.recv(1024)
    print("Answer is "+ answer.decode())
    print("Type 'Over' to terminate the program")
client.close()