import socket, sys
from datetime import datetime
from http.client import socket
import validators

def portScanner(remoteServer, startPort, endPort):
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print("-" * 60)
    print("Please wait, scanning remote host",  )
    print("-" * 60)
    t1 = datetime.now()
    try:
        for port in range(startPort,endPort):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total =  t2 - t1
    print('Scanning Completed in: ', total)

def ipAddrValid(ip):
    octet_list = ip.split(".")

    if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and \
            (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and \
            (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
        return True
    else:
        return False

def portScan():
    remoteServer = input("Enter a remote host to scan: ")
    startPort = int(input("Enter start port (1-65535): "))
    endPort = int(input("Enter end port (1-65535): "))

    try:
        if ipAddrValid(remoteServer) == True or validators.domain(remoteServer) == True:
            portScanner(remoteServer, startPort, endPort)
        else:
            print("Incorrect ip or hostname!")
    except ValueError as err:
        print(err)

def socketNet():
    host = str(input("Hostname: ")).lower()
    port = int(input("Port: "))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))
        
    try:
        s.connect((host, port))
        print("The connection was established successfully")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))


