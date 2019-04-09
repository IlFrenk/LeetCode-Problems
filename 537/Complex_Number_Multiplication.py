class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        realA, imaginaryA = a.split("+")
        realB, imaginaryB = b.split("+")
        realA = float(realA)
        realB = float(realB)
        imaginaryA = float(imaginaryA.replace("i", ""))
        imaginaryB = float(imaginaryB.replace("i", ""))
        complexC = complex(realA, imaginaryA)*complex(realB, imaginaryB)
        return str(float(complexC.real)) + "+" + str(float(complexC.imag)) + "i"
