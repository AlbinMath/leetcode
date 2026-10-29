from typing import Optional, List

# LeetCode provides the TreeNode definition.

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def clone(root):
            if root is None:
                return None
            return TreeNode(
                0,
                clone(root.left),
                clone(root.right)
            )

        def build(nodes):
            if nodes % 2 == 0:
                return []

            if nodes == 1:
                return [TreeNode(0)]

            if nodes in memo:
                return memo[nodes]

            result = []

            for left_count in range(1, nodes - 1, 2):
                right_count = nodes - 1 - left_count

                left_trees = build(left_count)
                right_trees = build(right_count)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = clone(left)
                        root.right = clone(right)
                        result.append(root)

            memo[nodes] = result
            return result

        return build(n)
