import random
import numpy

class Qubit:

    def __init__(self, Hcomp=0, Vcomp=0):
        self.alpha = Hcomp
        self.beta  = Vcomp

    # This is for debugging purposes only!
    def toString(self):
        if numpy.isreal(self.alpha):
            string = str(self.alpha) + "|H> "
        else:
            string = "(" + str(self.alpha) + ")|H> "
        if numpy.isreal(self.beta):
            if self.beta >= 0:
                string += "+ " + str(self.beta) + "|V>"
            else:
                string += "- " + str(-self.beta) + "|V>"
        else:
            string += "+ " + str(self.beta) + "|V>"
        return string

    def prepare(self, alpha, beta):
        self.alpha = alpha
        self.beta  = beta

    def prepareH(self):
        self.prepare(1,0)

    def prepareV(self):
        self.prepare(0,1)

    def prepareD(self):
        self.prepare(1/numpy.sqrt(2),  1/numpy.sqrt(2))

    def prepareA(self):
        self.prepare(1/numpy.sqrt(2), -1/numpy.sqrt(2))

    def prepareR(self):
        self.prepare(1/numpy.sqrt(2),  1j/numpy.sqrt(2))

    def prepareL(self):
        self.prepare(1/numpy.sqrt(2), -1j/numpy.sqrt(2))

    def measureHV(self):
        probH = abs(self.alpha)**2
        if random.uniform(0,1) <= probH:
            self.prepareH() # collapse to |H> state
            return "H"
        else:
            self.prepareV() # collapse to |V> state
            return "V"

    def measureDA(self):
        probD = abs((self.alpha+self.beta)/numpy.sqrt(2))**2
        if random.uniform(0,1) <= probD:
            self.prepareD() # collapse to |D> state
            return "D"
        else:
            self.prepareA() # collapse to |A> state
            return "A"

    def measureRL(self):
        probR = abs((self.alpha-1j*self.beta)/numpy.sqrt(2))**2
        if random.uniform(0,1) <= probR:
            self.prepareR() # collapse to |H> state
            return "R"
        else:
            self.prepareL() # collapse to |R> state
            return "L"