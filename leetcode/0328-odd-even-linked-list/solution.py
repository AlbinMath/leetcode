class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd, even, evenHead = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
