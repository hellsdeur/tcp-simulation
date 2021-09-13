class TCPBuffer:

    def __init__(self):
        self.buffer = []

    def empty(self):
        if self.buffer:
            return False
        return True


class TCPBufferSend(TCPBuffer):

    def bufferize(self, segment):
        self.buffer.append(segment)

    def unbufferize(self):
        return self.buffer.pop(0)


class TCPBufferReceive(TCPBuffer):

    def bufferize(self, segment):
        self.buffer.append(segment)

    def unbufferize(self):
        return self.buffer.pop(0)
