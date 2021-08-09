import pygame
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.103'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.client_id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return int(self.client.recv(2048).decode())

    def send(self, data):
        self.client.send(data.encode())
        return self.client.recv(2048).decode()
n=Network()
while True:
    pass
