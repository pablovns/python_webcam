import socket


udp_ip = "127.0.0.1"
udp_port = 8084

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

data, addr = sock.recvfrom(1024)

print(f"Mensagem recebida: {data}")
