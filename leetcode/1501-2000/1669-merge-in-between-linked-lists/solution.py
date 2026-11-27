class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
            
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
            
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
            
        prev_a.next = list2
        tail2.next = after_b
        
        return list1
