from random import choice

# classe de representação dos dados
class Data:

    # construtor
    def __init__(self, bits=[], n_bits=0):
        if n_bits == 0:
            try:
                if self.verify_input(bits):
                    self.bits = bits
                else:
                    self.bits = []
            except TypeError:
                print("TypeError: input must be a list of booleans.")
            except ValueError:
                print("ValueError: bit must be either True or False.")
        else:
            self.bits = [choice([True, False]) for _ in range(n_bits)]

    # vefica se a entrada é valida
    def verify_input(self, bits):
        if type(bits) is not list:
            raise TypeError("Input is not a list")
        for bit in bits:
            if (bit is not True) and (bit is not False):
                raise ValueError("Bit must be a boolean.")
        return True

    def __str__(self):
        return ''.join(["1" if b is True else "0" for b in self.bits])
