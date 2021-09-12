from random import choice

# classe de representação dos dados
class Data:

    # construtor
    def __init__(self, bits=[], n_bits=None):

        if n_bits is None:
            try:
                if self.verify_input(bits):
                    self.bits = bits
                else:
                    self.bits = []
            except TypeError:
                print("TypeError: input must be a list.")
            except ValueError:
                print("ValueError: bit must be either True or False.")
        else:
            try:
                if n_bits > 0:
                    self.bits = [choice([True, False]) for _ in range(n_bits)]
                else:
                    self.bits = []
                    raise ValueError("Number of bits is less than zero.")
            except ValueError:
                print("Value Error: number of bits must be greater than zero.")


    # vefica se a entrada é valida
    @staticmethod
    def verify_input(bits):
        if type(bits) is not list:
            raise TypeError("Input is not a list")
        for bit in bits:
            if (bit is not True) and (bit is not False):
                raise ValueError("Bit is not a boolean.")
        return True

    def __str__(self):
        return ''.join(["1" if b is True else "0" for b in self.bits])
