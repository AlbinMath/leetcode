from typing import Optional

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        out = []
        stack = [root]  # items are TreeNode objects or literal strings
        while stack:
            item = stack.pop()
            if isinstance(item, str):
                out.append(item)
                continue
            out.append(str(item.val))
            # push in reverse order of output
            if item.right:
                stack.extend([")", item.right, "("])
            if item.left:
                stack.extend([")", item.left, "("])
            elif item.right:
                stack.extend([")", "("])
        return "".join(out)
