# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def preOrder(self,root):
        #base
        if root is None:
            return 
        #recursive case
        self.ans.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.preOrder(root)
        return self.ans