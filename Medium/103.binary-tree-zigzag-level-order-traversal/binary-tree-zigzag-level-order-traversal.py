# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        q, ans = [], []
        if root:
            q.append(root)
            ans.append([root.val])
        else:
            return ans

        nextLayer = []
        nextLayerVal = []
        temp = 1
        zigzag = 1

        while q:
            node = q.pop(0)
            temp -= 1

            if node.left:
                nextLayer.append(node.left)
                nextLayerVal.append(node.left.val)
            if node.right:
                nextLayer.append(node.right)
                nextLayerVal.append(node.right.val)

            if temp == 0:
                if zigzag == 0:
                    ans.append(nextLayerVal)
                    zigzag = 1
                elif zigzag == 1:
                    ans.append(nextLayerVal[::-1])
                    zigzag = 0

                temp = len(nextLayer)
                q += nextLayer
                nextLayer = []
                nextLayerVal = []
        return ans[:-1]
