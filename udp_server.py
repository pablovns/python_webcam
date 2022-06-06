import socket
import sys


udp_ip = "127.0.0.1"
udp_port = 8084

MSG = b'a'*65800

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MSG, (udp_ip, udp_port))

print("Mensagem enviada.")
tam = sys.getsizeof(MSG)
print(f"Tamanho da mensagem: {tam}")
# print(f"Mensagem: {MSG}")