import sys
from collections import defaultdict
from typing import List, Optional

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sys.setrecursionlimit(10000)
        ids = {}                    # (left_id, val, right_id) -> id
        count = defaultdict(int)    # id -> occurrences
        ans = []

        def dfs(node):
            if not node:
                return 0
            key = (dfs(node.left), node.val, dfs(node.right))
            if key not in ids:
                ids[key] = len(ids) + 1
            i = ids[key]
            count[i] += 1
            if count[i] == 2:
                ans.append(node)
            return i

        dfs(root)
        return ans
