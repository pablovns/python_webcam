import socket
import pickle 


import cv2

#Porta do servidor
PORT = 8084

#Endereço do servidor
dest = '192.168.246.66'


#loop para conectar e obter os frames
while True: 

    #Objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Conecta ao servidor
    # print(f'== Conectando a {dest}:{PORT}==')
    client.connect((dest, PORT))

    data = []
    while True:
        # print('#', end='')
        pacote = client.recv(4096)
        if not pacote: 
            break
        data.append(pacote)


    if data:
        frame = pickle.loads(b"".join(data))
        # frame = pickle.loads(pacote)
    
        cv2.imshow('Imagem', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

#Fecha a conexão
client.close()

#Fecha todas as janelas
cv2.destroyAllWindows()
