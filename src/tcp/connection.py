from src.connection import Connection
from src.channel import Channel
from buffer import *
from src.data import Data
from segment import Segment
from src.checksum import Checksum
from src.datagram import Datagram


class TCPConnection(Connection):

    def __init__(self, mms=12000):
        super.__init__()
        self.t1 = {
            "terminal": self.terminal1,
            "channel": Channel(),
            "buffer": TCPBuffer(self.terminal1)
        }
        self.t2 = {
            "terminal": self.terminal2,
            "channel": Channel()
            "buffer": TCPBuffer(self.terminal2)
        }
        self.mms = mms
        self.handshake()

    def __del__(self):
        print("Connection closed.")

    def handshake(self):
        # send 1st connection segment
        # send 2nd connection segment
        pass

    def transmit(self, data, sender_ip):
        # tornando o comprimento dos dados múltiplo do mms
        while len(data.bits) % self.mms != 0:
            data.bits.insert(0, False)

        # dividindo os dados de acordo com o mms
        chunks = [Data(data.bits[i:i + self.mms]) for i in range(0, len(data.bits), self.mms)]

        # identificando o transmissor e receptor
        if sender_ip == self.terminal1.ip:
            sender, receiver = self.t1, self.t2
        else:
            sender, receiver = self.t2, self.t1

        # bufferizando os pedaços
        for i in range(len(chunks)):
            # transmissão inicial
            segment = Segment(
                seq_num=i,
                data=chunks[i],
                checksum=Checksum(chunks[i]),
                ACK=False
            )
            datagram = Datagram(sender["t1"].ip, segment)
            sender["buffer"].bufferize_send(datagram)

        # transferindo do buffer do transmissor para o canal
        while sender["buffer"].send_buffer:
            sender["channel"].enqueue(sender["buffer"].unbufferize_send())

        # transferindo do canal para o buffer do receptor
        while sender["channel"].queue:
            receiver["buffer"].bufferize_recv(sender["channel"].dequeue())

        # TODO verificar checksum

        # TODO enviar NAK

        # TODO reenviar caso NAK