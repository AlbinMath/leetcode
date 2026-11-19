from typing import List, Optional
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def collect(node: Optional[TreeNode], dist: int) -> None:
            if not node or dist < 0:
                return
            if dist == 0:
                ans.append(node.val)
                return
            collect(node.left, dist - 1)
            collect(node.right, dist - 1)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node is target:
                collect(node, k)
                return 0

            left_dist = dfs(node.left)
            if left_dist != -1:
                d = left_dist + 1
                if d == k:
                    ans.append(node.val)
                elif d < k:
                    collect(node.right, k - d - 1)
                return d

            right_dist = dfs(node.right)
            if right_dist != -1:
                d = right_dist + 1
                if d == k:
                    ans.append(node.val)
                elif d < k:
                    collect(node.left, k - d - 1)
                return d

            return -1

        dfs(root)
        return ans
