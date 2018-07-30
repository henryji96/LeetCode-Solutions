# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        tilt = abs(self.nodeSum(root.left) - self.nodeSum(root.right))

        return tilt + self.findTilt(root.left) + self.findTilt(root.right)




    def nodeSum(self, root):
        if not root:
            return 0


        return root.val + self.nodeSum(root.left) + self.nodeSum(root.right)
