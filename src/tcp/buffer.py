class TCPBuffer:

    def __init__(self, terminal):
        self.terminal = terminal
        self.send_buffer = []
        self.recv_buffer = []

    def bufferize_send(self, segment):
        self.send_buffer.append(segment)

    def unbufferize_send(self):
        return self.send_buffer.pop(0)

    def bufferize_recv(self, segment):
        self.recv_buffer.append(segment)

    def unbufferize_recv(self):
        return self.recv_buffer.pop(0)
