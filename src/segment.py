from data import Data
import pandas as pd

# classe de representação de um segmento TCP
class Segment:

    # construtor
    def __init__(self, s_port=80, d_port=80, seq_num=0, ack_num=0,
                 hea_len=20, rec_win=0, checksum=[], udp=0, opt=None,
                 data=Data(), **kwargs):

        self.s_port = s_port        # source port
        self.d_port = d_port        # destination port
        self.seq_num = seq_num      # sequence number
        self.ack_num = ack_num      # acknowledgement number
        self.hea_len = hea_len      # length of the TCP header
        self.flags = {              # optional flags
            "ACK": kwargs["ACK"] if "ACK" in kwargs else None,
            "RST": kwargs["RST"] if "RST" in kwargs else None,
            "SYN": kwargs["SYN"] if "SYN" in kwargs else None,
            "FIN": kwargs["FIN"] if "FIN" in kwargs else None,
            "PSH": kwargs["PSH"] if "PSH" in kwargs else None,
            "URG": kwargs.get("URG", None)
        }
        self.rec_win = rec_win      # receive window
        self.checksum = checksum    # checksum
        self.opt = opt              # options
        self.data = data            # data
    
    # cria um dataframe com os campos do segmento
    def detail(self):
        dic = {
            "Source port": self.s_port,
            "Destination port": self.d_port,
            "Seq. number": self.seq_num,
            "Ack. number": self.ack_num,
            "Header length" : self.hea_len,
            "Receive window": self.rec_win,
            "Checksum": self.checksum,
            "Options": self.opt,
            "Data": self.data
        }
        return pd.DataFrame(dic, index=[0])