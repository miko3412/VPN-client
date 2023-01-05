import socket
import ssl

host='127.0.0.1'
hostname='Miko'
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with socket.create_connection((host, 2137)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        ssock.send(bytes("DUPA", "utf-8"))