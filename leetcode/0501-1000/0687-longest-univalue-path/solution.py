class Solution:
    def longestUnivaluePath(self, root) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            a = l + 1 if node.left and node.left.val == node.val else 0
            b = r + 1 if node.right and node.right.val == node.val else 0
            ans = max(ans, a + b)
            return max(a, b)

        dfs(root)
        return ans
