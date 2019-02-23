# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0

        def recursiveSum(node):
            if node is not None:
                if L < node.val:
                    recursiveSum(node.left)
                if node.val < R:
                    recursiveSum(node.right)
                if L <= node.val <= R:
                    self.ans += node.val

        recursiveSum(root)
        return self.ans
