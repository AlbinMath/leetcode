from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(postorder)}

        def build(pl: int, pr: int, ql: int) -> Optional[TreeNode]:
            if pl > pr:
                return None
            root = TreeNode(preorder[pl])
            if pl == pr:
                return root
            idx = pos[preorder[pl + 1]]
            size = idx - ql + 1
            root.left = build(pl + 1, pl + size, ql)
            root.right = build(pl + size + 1, pr, idx + 1)
            return root

        return build(0, len(preorder) - 1, 0)
