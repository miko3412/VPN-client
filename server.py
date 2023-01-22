import socket
import ssl
import ipaddress

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1', 2137))
    print("slucham")
    sock.listen()
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        try:
            while True:
                mess = conn.recv(1024)
                print(mess.hex())
                ipVersion=format(mess[0],'08b')
                ipVersion=int(ipVersion[:4], 2)
                print(ipVersion)
                if ipVersion==4:
                    ipHeader=20
                    destinationIP = mess[16:20]
                    destinationIP= '.'.join(f'{c}' for c in destinationIP)
                elif ipVersion==6:
                    ipHeader=40
                    destinationIP = mess[24:40]
                    destinationIP= ipaddress.IPv6Address(destinationIP)
                    print(str(destinationIP))
                #else:
                #    break
                tcpHeader=format(mess[(ipHeader+12)], '08b')
                tcpHeader=int(tcpHeader[:4], 2)*4
                tcpPort=mess[(ipHeader+2):(ipHeader+4)]
                tcpPort=int.from_bytes(tcpPort, "big")
                print(tcpHeader)
                print(tcpPort)
                print(mess[(ipHeader+tcpHeader):])
                if len(mess[(ipHeader+tcpHeader):]) < 2:
                    conn.send(bytearray('0', 'utf-8'))
                    continue
                with socket.create_connection((str(destinationIP), tcpPort)) as sock2:
                    sock2.send(mess[(ipHeader+tcpHeader):])
                    resp = sock2.recv(1024)
                    print(resp)
                    conn.send(mess[:(ipHeader+tcpHeader)]+resp)
        except KeyboardInterrupt:
            sock.close()
