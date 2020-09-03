import socket

UDP_IP = "192.168.8.39"
UDP_PORT = 80
mac_addr = 'B42E99561465'
message = bytes.fromhex('ffffffffffff' + ''.join([mac_addr for _ in range(16)]))

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message, (UDP_IP, UDP_PORT)) 