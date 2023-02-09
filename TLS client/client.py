import ssl
import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a context with the self-signed certificate
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#context.load_verify_locations(cafile='server.crt')
context.load_verify_locations(cafile='/home/ndm4kor/POC/TslCommunication/cert/server.crt')

# Connect to the server and wrap the socket with the SSL context
client_socket = socket.socket()
#client_socket.connect(('localhost', 12345))
client_socket.connect(('localhost', 8443))
secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')

logging.info('Connected to the server')

# Send data to the server and receive a response
secure_socket.send(b'Hello, server!')
data = secure_socket.recv(1024)
print('Received:', data)
logging.info(f'Received message: {data.decode()}')

# Close the secure socket
secure_socket.shutdown(socket.SHUT_RDWR)
secure_socket.close()
logging.info('Connection closed')
