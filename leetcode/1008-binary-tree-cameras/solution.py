import sys
from typing import Optional

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        sys.setrecursionlimit(10000)
        cameras = 0

        def dfs(node):
            nonlocal cameras
            if not node:
                return 1
            l = dfs(node.left)
            r = dfs(node.right)
            if l == 0 or r == 0:
                cameras += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0

        if dfs(root) == 0:
            cameras += 1
        return cameras
