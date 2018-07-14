# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue, ans = [], []
        if root:
            queue.append(root)
            ans.append([root.val])
        else:
            return ans

        layerSize = 1
        nextLayerNode = []
        nextLayerVal = []

        i = 0

        while queue:

            node = queue.pop(0)

            layerSize -= 1

            if node.left:
                nextLayerNode.append(node.left)
                nextLayerVal.append(node.left.val)


            if node.right:
                nextLayerNode.append(node.right)
                nextLayerVal.append(node.right.val)



            if layerSize == 0:

                layerSize = len(nextLayerNode)
                queue += nextLayerNode
                ans.append(nextLayerVal)

                nextLayerNode = []
                nextLayerVal = []


        return ans[:-1]






                
