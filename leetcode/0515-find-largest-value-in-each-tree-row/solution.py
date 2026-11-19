from typing import List, Optional
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            row_max = float('-inf')
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val > row_max:
                    row_max = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(row_max)
            
        return result
