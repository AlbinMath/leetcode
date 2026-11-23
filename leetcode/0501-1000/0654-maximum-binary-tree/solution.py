from typing import List, Optional

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for x in nums:
            node = TreeNode(x)
            last = None
            while stack and stack[-1].val < x:
                last = stack.pop()
            node.left = last
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
