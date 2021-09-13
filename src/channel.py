class Channel:

    def __init__(self):
        self.queue = []

    def enqueue(self, datagram):
        self.queue.append(datagram)

    def dequeue(self):
        return self.queue.pop(0)
