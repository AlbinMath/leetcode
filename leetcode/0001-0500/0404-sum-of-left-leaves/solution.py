class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        total = 0

        # Check if the left child is a leaf
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Check the right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total
