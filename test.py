import socket
import ssl

host='127.0.0.1'
hostname='Miko'
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with socket.create_connection((host, 2137)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        a = bytearray.fromhex('60032918006a06402a02a3114335e800380cd88752e7b8ce2a001450401b080e000000000000200ede160050bcf08cc66c6d6669801801fbbb8b00000101080a8d036aef4fcf7bf8474554202f20485454502f312e310d0a486f73743a20676f6f676c652e636f6d0d0a557365722d4167656e743a206375726c2f372e36382e300d0a4163636570743a202a2f2a0d0a0d0a')
        print(a)
        ssock.send(a)
        response = ssock.recv(1024)
        print(response)