# classe de representação dos dados
class Data:

    # construtor
    def __init__(self, bits=[]):
        try:
            self.bits = [b for b in bits] if self.verify_input(bits) else []
        except TypeError:
            print("TypeError: input must be a list of strings.")
        except ValueError:
            print("ValueError: bit must be either 0 or 1.")

    # vefica se a entrada é valida
    def verify_input(self, bits):
        if type(bits) is not list:
            raise TypeError("Input is not a list")
        for bit in bits:
            if bit != '1' and bit != '0':
                raise ValueError("Bit is not 1 or 0")
        return True

    def __str__(self):
        return ''.join(self.bits)