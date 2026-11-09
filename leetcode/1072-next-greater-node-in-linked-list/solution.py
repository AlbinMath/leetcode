from typing import List, Optional

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        res = []
        stack = []

        node = head
        while node:
            x = node.val
            while stack and vals[stack[-1]] < x:
                res[stack.pop()] = x
            stack.append(len(vals))
            vals.append(x)
            res.append(0)
            node = node.next

        return res
