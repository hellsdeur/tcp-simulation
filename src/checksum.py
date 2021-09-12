from src.data import Data


class Checksum:

    # construtor
    def __init__(self, data=Data()):
        self.bits = data.bits
        self.checksum = self.compute()
    
    def compute(self):
        g16s = self.generate_g16s(self.bits)
        total_sum = self.sum_g16s(g16s)
        return self.ones_complement(total_sum)

    # gerar grupos de 16 bits
    @staticmethod
    def generate_g16s(bits):
        # tornando o comprimento dos dados múltiplo de 16
        while len(bits) % 16 != 0:
            bits.insert(0, True)

        # agrupando de 16 em 16
        return [bits[i:i + 16] for i in range(0, len(bits), 16)]

    # obter soma total dos agrupamentos de 16 bits
    def sum_g16s(self, g16s):
        total = [False for _ in range(16)]
        for g in g16s:
            total = self.sum_groups(total, g)
        return total

    # somar dois grupos de 16 bits
    def sum_groups(self, g1, g2, carry=False):
        for i in reversed(range(16)):
            if carry is False:
                if (g1[i] is False) and (g2[i] is False):
                    g1[i] = False
                elif (g1[i] is False and g2[i] is True) or (g1[i] is True and g2[i] is False):
                    g2[i] = True
                elif g1[i] is True and g2[i] is True:
                    g2[i] = False
                    carry = True
            if carry:
                if g1[i] is False and g2[i] is False:
                    g2[i] = True
                    carry = False
                elif (g1[i] is False and g2[i] is True) or (g1[i] is True and g2[i] is False):
                    g2[i] = False
                    carry = True
                elif g1[i] is True and g2[i] is True:
                    g2[i] = True
                    carry = True
        total = g2

        # se houver bit excedente, somá-lo ao total
        if carry:
            total = self.sum_groups(total, [False for _ in range(16)], True)

        return total

    # complemento de 1 de um total
    @staticmethod
    def ones_complement(total):
        return [not t for t in total]

    def __str__(self):
        return ''.join(["1" if c is True else "0" for c in self.checksum])
