from abc import abstractmethod

class Connection:

    def __init__(self, terminal1, terminal2):
        self.terminal1 = terminal1
        self.terminal2 = terminal2

    @abstractmethod
    def transmit(self):
        pass