import ssl
import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# Create a context with the self-signed certificate
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='/home/ndm4kor/POC/TslCommunication/cert/server.crt', keyfile='/home/ndm4kor/POC/TslCommunication/cert/server.key')

# Create a socket and bind it to a specific address and port
server_socket = socket.socket()
#server_socket.bind(('0.0.0.0', 12345))
server_socket.bind(('localhost',8443))
server_socket.listen(5)

logging.info('Server is listening on localhost:8443')

# Wait for a connection and wrap the socket with the SSL context
connection, client_address = server_socket.accept()
logging.info(f'Accepted connection from {client_address}')
secure_socket = context.wrap_socket(connection, server_side=True)

# Receive data from the client and send a response
data = secure_socket.recv(1024)
secure_socket.send(b'Received: ' + data)
logging.info(f'Sent message to {client_address}')

# Close the secure socket
secure_socket.shutdown(socket.SHUT_RDWR)
secure_socket.close()
logging.info(f'Closed connection with {client_address}')
