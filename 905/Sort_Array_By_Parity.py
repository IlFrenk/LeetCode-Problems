class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        odd = []
        even = []

        for i in A :
            if i % 2 == 0 :
                even.append(i)
            else :
                odd.append(i)
        return even + odd
