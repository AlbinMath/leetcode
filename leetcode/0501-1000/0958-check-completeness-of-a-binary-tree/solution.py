from typing import Optional
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seen_null = False
        
        while queue:
            curr = queue.popleft()
            if curr is None:
                seen_null = True
            else:
                if seen_null:
                    return False
                queue.append(curr.left)
                queue.append(curr.right)
                
        return True
