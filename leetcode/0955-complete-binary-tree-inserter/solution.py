from typing import Optional
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.candidates = deque()
        bfs = deque([root])
        
        while bfs:
            curr = bfs.popleft()
            if curr.left:
                bfs.append(curr.left)
            if curr.right:
                bfs.append(curr.right)
            if not curr.left or not curr.right:
                self.candidates.append(curr)

    def insert(self, val: int) -> int:
        parent = self.candidates[0]
        child = TreeNode(val)
        self.candidates.append(child)
        
        if not parent.left:
            parent.left = child
        else:
            parent.right = child
            self.candidates.popleft()
            
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
