from typing import Optional

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            self.seen.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                stack.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.seen
