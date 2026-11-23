from typing import Optional
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            start_idx = queue[0][1]
            end_idx = start_idx
            for _ in range(len(queue)):
                curr, idx = queue.popleft()
                end_idx = idx
                norm_idx = idx - start_idx
                if curr.left:
                    queue.append((curr.left, norm_idx << 1))
                if curr.right:
                    queue.append((curr.right, (norm_idx << 1) | 1))
                    
            if end_idx - start_idx + 1 > max_width:
                max_width = end_idx - start_idx + 1
                
        return max_width
