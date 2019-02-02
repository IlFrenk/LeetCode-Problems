class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        A2 = []

        for i in A :
            for j in A2 :
                if i == j :
                    return i
            A2.append(i)
