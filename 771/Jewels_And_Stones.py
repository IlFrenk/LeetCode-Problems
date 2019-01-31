class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = 0

        for i in J:
            for i2 in S:
                if i == i2:
                    jewels += 1
        return jewels
