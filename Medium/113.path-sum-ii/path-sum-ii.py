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
        :rtype: List[List[int]]
        """

        if not root:
            return []
        ans = []

        self.dfs(root, sum, [], ans)

        return ans

    def dfs(self, root, sum, tempArr, ans):

        if not root.left and not root.right and sum == root.val:
            tempArr.append(root.val)
            ans.append(tempArr)

        if root.left:
            self.dfs(root.left, sum - root.val, tempArr + [root.val], ans)

        if root.right:
            self.dfs(root.right, sum - root.val, tempArr + [root.val], ans)
