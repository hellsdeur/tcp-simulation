from src.connection import Connection
from src.channel import Channel
from src.tcp.buffer import (TCPBufferSend, TCPBufferReceive)
from src.data import Data
from src.tcp.segment import Segment
from src.checksum import Checksum
from src.datagram import Datagram
import pandas as pd


class TCPConnection(Connection):

    def __init__(self, terminal1, terminal2, mms=12000):
        self.t1 = {
            "terminal": terminal1,
            "channel": Channel(),
            "send_buffer": TCPBufferSend(),
            "recv_buffer": TCPBufferReceive()
        }
        self.t2 = {
            "terminal": terminal2,
            "channel": Channel(),
            "send_buffer": TCPBufferSend(),
            "recv_buffer": TCPBufferReceive()
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
        if sender_ip == self.t1["terminal"].ip:
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
            datagram = Datagram(sender["terminal"].ip, segment)
            sender["send_buffer"].bufferize(datagram)

        # transferindo do buffer do transmissor para o canal
        while not sender["send_buffer"].empty():
            sender["channel"].enqueue(sender["send_buffer"].unbufferize())

        # transferindo do canal para o buffer do receptor
        while sender["channel"].queue:
            receiver["recv_buffer"].bufferize(sender["channel"].dequeue())

        # TODO verificar checksum
        df = pd.DataFrame()
        while not receiver["recv_buffer"].empty():
            datagram = receiver["recv_buffer"].unbufferize()
            segment = datagram.segment
            df = df.append(segment.detail())

        print(df)

        # TODO enviar NAK

        # TODO reenviar caso NAK