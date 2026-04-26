import socket

#A socket is like a tool (endpoint) that lets a program communicate over
# an existing network or diff. processes in OS.

def scanIP():
    targetIP=input("Enter the IP address you want to scan:")
    scanRange=int(input("Enter the range of ports for scanning:"))
    
    '''socket.AF_INET
    “What kind of IP addresses will I use?”
    Meaning:
    AF_INET = IPv4 (most common)
    Example: 192.168.1.1'''


    ''' 2. socket.SOCK_STREAM → Socket Type 
    SOCK_STREAM:TCP
    SOCK_DGRAM = UDP
    '''
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for port in range(scanRange):
        try:
            s.connect((targetIP,port))
            print("connected for port number :",port)
        except:
            print("cannot connect for port number :",port)
            
scanIP()