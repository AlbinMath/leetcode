class Solution:
    def preorder(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Add children in reverse order
            for child in reversed(node.children):
                stack.append(child)

        return result
