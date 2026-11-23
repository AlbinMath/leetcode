class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            cur = dummy
            while cur.next and cur.next.val <= head.val:
                cur = cur.next
            nxt = head.next
            head.next = cur.next
            cur.next = head
            head = nxt
        return dummy.next
