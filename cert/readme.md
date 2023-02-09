Execute the below command to generate the SSL certificate.

openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes

You skips all the paramters except CN, give it as localhost as we are running it locally.