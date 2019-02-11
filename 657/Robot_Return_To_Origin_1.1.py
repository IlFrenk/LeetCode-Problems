class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        horizontalMoves = 0
        verticalMoves = 0

        for i in moves :
            if i == 'U' :
                verticalMoves += 1
            elif i == 'D' :
                verticalMoves -= 1
            elif i == 'R' :
                horizontalMoves += 1
            elif i == 'L' :
                horizontalMoves -= 1
            else :
                print("Move ", i, " is NOT valid!")
                return -1
        if horizontalMoves == 0 and verticalMoves == 0 :
            return True
        else :
            return False
