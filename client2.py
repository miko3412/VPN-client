import socket, ssl

host='127.0.0.1'
hostname='Miko'
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with socket.create_connection((host, 2137)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        #while True:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
        s.bind(('enp9s0', 0))
        while True:
        # receive a package
            packet = s.recvfrom(65565)
            if len(packet)>52:
                ipVersion=format(packet[0],'08b')
                ipVersion=int(ipVersion[:4], 2)
                if ipVersion==4:
                    ipHeader=20
                elif ipVersion==6:
                    ipHeader=40
                tcpHeader=format(packet[(ipHeader+12)], '08b')
                tcpHeader=int(tcpHeader[:4], 2)*4
                tcpPort=packet[(ipHeader+2):(ipHeader+4)]
                tcpPort=int.from_bytes(tcpPort, "big")
                if tcpPort == 80:
                    print(packet)
                    ssock.send(packet)
                    response = ssock.recv(1024)
                    print(response)