from collections import defaultdict
from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class Node:
            __slots__ = ("children", "sig")
            def __init__(self):
                self.children = {}
                self.sig = ""

        root = Node()
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = Node()
                node = node.children[name]

        freq = defaultdict(int)

        # post-order, iterative to avoid recursion limits (depth up to 500)
        stack = [(root, False)]
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node, True))
                for child in node.children.values():
                    stack.append((child, False))
            else:
                if node.children:
                    parts = [name + "(" + c.sig + ")"
                             for name, c in sorted(node.children.items())]
                    node.sig = "".join(parts)
                    freq[node.sig] += 1

        ans = []
        path = []

        def collect(node: Node) -> None:
            for name, child in node.children.items():
                if child.sig and freq[child.sig] > 1:
                    continue                 # marked: skip this whole subtree
                path.append(name)
                ans.append(path[:])
                collect(child)
                path.pop()

        collect(root)
        return ans
