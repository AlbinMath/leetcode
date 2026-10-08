class Solution:
    def findTilt(self, root):
        total_tilt = 0

        def subtree_sum(node):
            nonlocal total_tilt

            if node is None:
                return 0

            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            # Tilt of current node
            total_tilt += abs(left_sum - right_sum)

            # Sum of current subtree
            return node.val + left_sum + right_sum

        subtree_sum(root)

        return total_tilt
