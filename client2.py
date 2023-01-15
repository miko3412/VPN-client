import socket, ssl


host='127.0.0.1'
hostname='Miko'
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with socket.create_connection((host, 2137)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
        s.bind(('enp9s0', 0))
        while True:
            try:
                packet = s.recvfrom(65565)
                packet= packet[0][14:]
                ipVersion=format(packet[0],'08b')
                ipVersion=int(ipVersion[:4], 2)
                if ipVersion==4:
                    ipHeader=20
                elif ipVersion==6:
                    ipHeader=40
                else: continue
                tcpHeader=format(packet[(ipHeader+12)], '08b')
                tcpHeader=int(tcpHeader[:4], 2)*4
                tcpPort=packet[(ipHeader+2):(ipHeader+4)]
                tcpPort=int.from_bytes(tcpPort, "big")
                print(tcpPort)
                if tcpPort == 80 and len(packet) > 52 and len(packet[(ipHeader+tcpHeader):]) > 5:
                    print(packet)
                    ssock.send(packet)
                    response = ssock.recv(1024)
                    print("-----------------------------To jest odpowiedz -------------------------------")
                    print(response.hex())
                    print("\n\n")
            except IndexError:
                continue