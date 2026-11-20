from typing import List, Optional

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth = {}
        height = {}
        order = []
        stack = [(root, 0)]
        while stack:
            node, d = stack.pop()
            depth[node] = d
            order.append(node)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))

        for node in reversed(order):
            hl = height[node.left] if node.left else -1
            hr = height[node.right] if node.right else -1
            height[node] = max(hl, hr) + 1

        res = {}
        best = {root: 0}
        for node in order:  # parents appear before children
            b = best[node]
            d = depth[node]
            hl = height[node.left] if node.left else -1
            hr = height[node.right] if node.right else -1
            if node.left:
                best[node.left] = max(b, d + 1 + hr)
                res[node.left.val] = best[node.left]
            if node.right:
                best[node.right] = max(b, d + 1 + hl)
                res[node.right.val] = best[node.right]

        return [res[q] for q in queries]
