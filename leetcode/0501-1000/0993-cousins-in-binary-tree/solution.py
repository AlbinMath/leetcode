
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])

        while queue:
            size = len(queue)
            x_found = False
            y_found = False

            for _ in range(size):
                node = queue.popleft()

                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False

                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if x_found and y_found:
                return True

            if x_found or y_found:
                return False

        return False

