class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        maxCol = 0
        maxRow = 0
        diff = 0
        tot = 0
        colonna = []
        columnOfMaxElementinRow = 0

        for row in grid :
            for element in row :
                columnOfMaxElementinRow += 1
                if element > maxRow :
                    maxRow = element
                else :
                    columnOfMaxElementinRow -= 1
            return [row[columnOfMaxElementinRow] for row in grid]




            '''for elementInRow in row :
                if elementInRow > j :
                    j = elementInRow
            for elementInRow in row :
                if elementInRow < j :
                    diff = j - elementInRow
                    tot += diff
            j = 0
            grid[:,row]
        return tot
        '''
