import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return

def main():
    # ip1 = "192.168.95.148"
    # ip2 = "192.168.95.149"
    # port = 21
    # banner1 = retBanner(ip1,port)
    # if banner1:
    #     print "Banner 1 retrieved"
    # else:
    #     print "Error in 1"
    # banner2 = retBanner(ip2,port)
    # if banner2:
    #     print "Banner 2 retrieved"
    # else:
    #     print "Error in 2"
    portList = [21,22,25,80,110,443]
    for x in range(1,255):
        for port in portList:
            ip = "192.168.95"+str(x)
            banner = retBanner(ip,port)
            if banner:
                print "Retrieved Banner: "+ str(x)
            else:
                print "Error in: "+ str(x)

if __name__ == '__main__':
        main()
