import bisect
from typing import List, Optional

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        
        # In-order traversal to extract elements in sorted order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        m = len(vals)
        res = []
        
        for q in queries:
            # bisect_right finds the insertion point after any existing q
            idx = bisect.bisect_right(vals, q)
            
            # mini is the largest element <= q
            mini = vals[idx - 1] if idx > 0 else -1
            
            # If the exact value q exists, maxi is also q
            if idx > 0 and vals[idx - 1] == q:
                maxi = q
            else:
                # Otherwise, maxi is the element at idx (first element > q)
                maxi = vals[idx] if idx < m else -1
                
            res.append([mini, maxi])
            
        return res
