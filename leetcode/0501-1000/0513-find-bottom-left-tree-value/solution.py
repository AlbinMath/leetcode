from typing import Optional
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        curr = root
        
        while queue:
            curr = queue.popleft()
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
                
        return curr.val
