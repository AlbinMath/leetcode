class Solution(object):
    def sortedListToBST(self, head):
        # Count nodes
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        self.cur = head

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            left = build(lo, mid - 1)        # consume left half first
            root = TreeNode(self.cur.val)    # current list node is the root
            self.cur = self.cur.next
            root.left = left
            root.right = build(mid + 1, hi)  # then the right half
            return root

        return build(0, n - 1)
