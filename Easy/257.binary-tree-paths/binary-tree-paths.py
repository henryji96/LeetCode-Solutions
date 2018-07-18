# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        stack = [(root, "")]
        ans = []

        while stack:

            node, strr = stack.pop()

            if not node.left and not node.right:
                ans.append(strr + str(node.val))

            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
        return ans
