# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(node, leafs):
            if node.left == None and node.right == None:
                leafs.append(node.val)
                return 
            if node.left:
                dfs(node.left, leafs)
            if node.right:
                dfs(node.right,leafs)
        
        leafs1 = []
        dfs(root1, leafs1)

        leafs2 = []
        dfs(root2, leafs2)

        return leafs1 == leafs2
            

        