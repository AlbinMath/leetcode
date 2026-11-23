class Solution:
    def postorder(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in node.children:
                stack.append(child)

        result.reverse()

        return result
