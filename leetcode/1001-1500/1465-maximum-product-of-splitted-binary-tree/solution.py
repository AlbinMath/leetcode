class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(total)
            return total

        total = dfs(root)

        max_product = 0
        for sub_sum in subtree_sums:
            product = sub_sum * (total - sub_sum)
            max_product = max(max_product, product)

        return max_product % MOD
