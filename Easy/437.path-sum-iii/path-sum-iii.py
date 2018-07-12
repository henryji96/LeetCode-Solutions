# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


    def dfs(self, root, sum):

        if not root:
            return 0

        cnt = 0
        if root.val == sum:
            cnt += 1

        cnt += self.dfs(root.left, sum - root.val)
        cnt += self.dfs(root.right, sum - root.val)

        return cnt
