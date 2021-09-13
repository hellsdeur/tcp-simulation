from src.data import Data
from src.terminal import Terminal
from src.tcp.connection import TCPConnection

# d = Data(n_bits=64)
# c = Checksum(d)
#
# s = Segment(data=d, checksum=c)
# print(s.detail()[["CHECKSUM", "DATA"]])

t1 = Terminal("213.117.0.13")
t2 = Terminal("208.23.5.3")
conn = TCPConnection(t1, t2)

t1.send(conn, Data(n_bits=12000*10))