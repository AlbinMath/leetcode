class Solution:
    def findMode(self, root):
        result = []
        max_count = 0

        prev = None
        count = 0

        def inorder(node):
            nonlocal prev, count, max_count, result

            if node is None:
                return

            inorder(node.left)

            # Update count
            if prev == node.val:
                count += 1
            else:
                count = 1

            # Update modes
            if count > max_count:
                max_count = count
                result = [node.val]
            elif count == max_count:
                result.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)

        return result
