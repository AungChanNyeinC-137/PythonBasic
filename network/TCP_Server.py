import socket
def server_program():
    # host = socket.gethostbyname()
    port = 500
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print('connection from: '+ str(address))
    while 1:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("User" + str(address) + 'says ' + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()

server_program()