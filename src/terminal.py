from src.data import Data
from src.connection import Connection


class Terminal:

    def __init__(self, ip):
        self.ip = ip

    def send(self, connection, data):
        connection.transmit(data, self.ip)
