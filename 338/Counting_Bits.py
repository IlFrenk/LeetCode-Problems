class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i = 0
        array=[]
        while i<=num:
            counter = bin(i).count('1')
            array.append(counter)
            i+=1
        return array
