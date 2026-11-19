from typing import Optional
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
            
        queue = deque([root])
        curr_depth = 1
        
        while queue:
            if curr_depth == depth - 1:
                for cur in queue:
                    cur.left = TreeNode(val, cur.left, None)
                    cur.right = TreeNode(val, None, cur.right)
                break
                
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            curr_depth += 1
            
        return root
