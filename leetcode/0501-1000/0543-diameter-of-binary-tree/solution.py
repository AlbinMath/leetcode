class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter passing through this node
            diameter = max(diameter, left + right)

            # Height of this node
            return 1 + max(left, right)

        height(root)

        return diameter
