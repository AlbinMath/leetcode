class Solution:
    def findTarget(self, root, k):
        seen = set()

        def dfs(node):
            if node is None:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
