from src.data import Data
from src.checksum import Checksum
from src.tcp.segment import Segment

d = Data(n_bits=64)
c = Checksum(d)

s = Segment(data=d, checksum=c)
print(s.detail()[["CHECKSUM", "DATA"]])
