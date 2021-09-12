from src.data import Data
from src.checksum import Checksum
import pandas as pd

# classe de representação de um segmento TCP
class Segment:

    # construtor
    def __init__(self, s_port=80, d_port=80, seq_num=0, ack_num=0,
                 head_len=20, rec_win=0, checksum=Checksum, urg_dpt=0,
                 opt=None, data=Data(), **kwargs):

        self.s_port = s_port        # source port
        self.d_port = d_port        # destination port
        self.seq_num = seq_num      # sequence number
        self.ack_num = ack_num      # acknowledgement number
        self.head_len = head_len    # length of the TCP header
        self.flags = {              # optional flags
            "URG": kwargs["URG"] if "URG" in kwargs else None,
            "ACK": kwargs["ACK"] if "ACK" in kwargs else None,
            "RST": kwargs["RST"] if "RST" in kwargs else None,
            "SYN": kwargs["SYN"] if "SYN" in kwargs else None,
            "FIN": kwargs["FIN"] if "FIN" in kwargs else None,
            "PSH": kwargs["PSH"] if "PSH" in kwargs else None,
        }
        self.rec_win = rec_win      # receive window
        self.checksum = checksum    # checksum
        self.urg_dpt = urg_dpt      # urgent data pointer
        self.opt = opt              # options
        self.data = data            # data
    
    # cria um dataframe com os campos do segmento
    def detail(self):
        dic = {
            "S_PORT": self.s_port,
            "D_PORT": self.d_port,
            "SEQ_NUM": self.seq_num,
            "ACK_NUM": self.ack_num,
            "HEAD_LEN": self.head_len,
            "REC_WIN": self.rec_win,
            "CHECKSUM": self.checksum,
            "URG_DPT": self.urg_dpt,
            "OPT": self.opt
        }
        for key in self.flags.keys():
            if self.flags[key] is not None:
                dic[key] = self.flags[key]

        dic["DATA"] = str(self.data)

        return pd.DataFrame([dic])
