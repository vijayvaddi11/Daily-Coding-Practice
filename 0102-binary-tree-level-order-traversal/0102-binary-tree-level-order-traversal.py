# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
    
    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
    
    def pop(self):
        if self.front == -1 or self.front == len(self.q):
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x  # ✅ return popped node

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        queue = Queue()
        queue.push(root)

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                level.append(front.val)
                if front.left:
                    queue.push(front.left)
                if front.right:
                    queue.push(front.right)
            ans.append(level)
        
        return ans
