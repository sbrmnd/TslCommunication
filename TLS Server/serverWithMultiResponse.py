##Working code excepting multiple connection.
# import ssl
# import socket

# def handle_client(client_socket, client_address):
#     print(f"[{client_address}] Accepted connection")
#     data = client_socket.recv(1024)
#     print(f"[{client_address}] Received data: {data.decode()}")
#     client_socket.send(b"ACK")
#     print(f"[{client_address}] Sent ACK")
#     client_socket.close()
#     print(f"[{client_address}] Connection closed")

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile='/home/ndm4kor/POC/TslCommunication/cert/server.crt', keyfile='/home/ndm4kor/POC/TslCommunication/cert/server.key')

# bind_address = ('localhost', 12345)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(bind_address)
# server.listen(5)

# print(f"Listening on {bind_address}")

# while True:
#     client_socket, client_address = server.accept()

#     client_socket = context.wrap_socket(client_socket, server_side=True)
#     handle_client(client_socket, client_address)

##Without forcefully closing the client.

import ssl
import socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='../cert/server.crt', keyfile='../cert/server.key')
# Set the minimum and maximum TLS version to 1.3
context.minimum_version = ssl.TLSVersion.TLSv1_3
context.maximum_version = ssl.TLSVersion.TLSv1_3

server_address = ('localhost', 12345)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print("Waiting for incoming connections")

while True:
    connection, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    connection = context.wrap_socket(connection, server_side=True)

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            connection.send(b"Hello, Client!")
    except Exception as e:
        print(f"Error occurred while processing request: {e}")
    finally:
        connection.close()
        print("Closed connection")


