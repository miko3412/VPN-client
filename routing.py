from scapy.all import *

def fromClient(vpnIP, iface):
    conf.route.add(net=vpnIP+"/32",dev=iface)

def disClient(vpnIP, iface):
    conf.route.delt(net=vpnIP+"/32",dev=iface)

def test():
    fromClient("127.0.0.1", "wowVPN")


if __name__ == '__main__':
    test()