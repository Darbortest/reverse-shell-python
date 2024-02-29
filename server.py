import socket
import subprocess

def start_server():
    host = '10.9.3.102'
    port = 4201

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"[*] Accepted connection from {addr}")

    while True:
        command = input("$ ")
        client_socket.send(command.encode())

        if command.lower() == 'exit':
            break

        output = client_socket.recv(4096).decode()
        print(output)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
