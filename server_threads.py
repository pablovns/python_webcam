import socket
import pickle
import cv2

from threading import Thread

frame_g = None

class ThreadCam(Thread):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise IOError("Erro ao abrir a câmera")

    def run(self):
        global frame_g

        while True:
            ret, frame = cap.read()
            frame_g = frame

camera = ThreadCam()
print("Fim!")