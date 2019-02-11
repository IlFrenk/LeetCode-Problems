class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        res = []

        for i in A :
            res.append(i**2)
        return sorted(res)
