# import logging
# import ssl
# import socket

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(asctime)s] [%(levelname)s] %(message)s',
#                     handlers=[logging.StreamHandler()])

# logger = logging.getLogger('client')

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# #context.load_verify_locations(cafile='cert.pem')
# context.load_verify_locations(cafile='/home/ndm4kor/POC/TslCommunication/cert/server.crt')

# server_address = ('localhost', 12345)
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket = context.wrap_socket(client_socket)
# client_socket.connect(server_address)

# for i in range(5):
#     logger.debug(f"Sending request #{i+1}")
#     client_socket.send(b"Hello, Server!")
#     data = client_socket.recv(1024)
#     logger.debug(f"Received response: {data.decode()}")

# client_socket.close()
# logger.debug("Closed connection with server")

## Working code to send multi request.

# import logging
# import ssl
# import socket

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(asctime)s] [%(levelname)s] %(message)s',
#                     handlers=[logging.StreamHandler()])

# logger = logging.getLogger('client')

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.load_verify_locations(cafile='/home/ndm4kor/POC/TslCommunication/cert/server.crt')
# context.check_hostname = False

# server_address = ('localhost', 12345)
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket = context.wrap_socket(client_socket, server_hostname='localhost')
# client_socket.connect(server_address)

# for i in range(5):
#     try:
#         logger.debug(f"Sending request #{i+1}")
#         client_socket.send(b"Hello, Server!")
#         data = client_socket.recv(1024)
#         logger.debug(f"Received response: {data.decode()}")
#     except BrokenPipeError:
#         logger.error("Server has closed the connection")
#         break

# client_socket.close()
# logger.debug("Closed connection with server")

## Client request user input to send the request to the server.
import ssl
import socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='/home/ndm4kor/POC/TslCommunication/cert/server.crt')

server_address = ('localhost', 12345)

while True:
    request = input("Enter request to send to server (type 'exit' to quit): ")
    if request == "exit":
        break

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    client_socket.connect(server_address)

    client_socket.send(request.encode())
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode()}")

    client_socket.close()



