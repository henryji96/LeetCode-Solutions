# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """


        if not t:
            return ""

        s = str(t.val)
        sl = self.tree2str(t.left)
        sr = self.tree2str(t.right)

        if not t.left and not t.right:
            return s
        elif not t.right:
            return s + "(" + sl + ")"

        return s + "(" + sl + ")" + "(" + sr + ")"
