# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]

        def trasversal(node):
            if node==None:
                return 
            
            trasversal(node.left)
            res.append(node.val)
            trasversal(node.right)
        
        trasversal(root)

        return res