class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None,
                 bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        a, b = quadTree1, quadTree2

        if a.isLeaf:
            return a if a.val else b
        if b.isLeaf:
            return b if b.val else a

        tl = self.intersect(a.topLeft, b.topLeft)
        tr = self.intersect(a.topRight, b.topRight)
        bl = self.intersect(a.bottomLeft, b.bottomLeft)
        br = self.intersect(a.bottomRight, b.bottomRight)

        if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                and tl.val == tr.val == bl.val == br.val):
            return Node(tl.val, True)

        return Node(False, False, tl, tr, bl, br)
