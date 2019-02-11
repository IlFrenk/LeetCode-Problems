class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        length = len(moves)

        Ucounter = moves.count('U', 0, length)
        Dcounter = moves.count('D', 0, length)
        Lcounter = moves.count('L', 0, length)
        Rcounter = moves.count('R', 0, length)

        if Ucounter == Dcounter and Lcounter == Rcounter :
            return True
        else:
            return False
