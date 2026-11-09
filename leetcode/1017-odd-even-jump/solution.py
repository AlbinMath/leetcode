from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def next_jumps(order):
            nxt = [-1] * n
            stack = []
            for idx in order:
                while stack and stack[-1] < idx:
                    nxt[stack.pop()] = idx
                stack.append(idx)
            return nxt

        odd_next = next_jumps(sorted(range(n), key=lambda i: (arr[i], i)))
        even_next = next_jumps(sorted(range(n), key=lambda i: (-arr[i], i)))

        odd = [False] * n
        even = [False] * n
        odd[n - 1] = even[n - 1] = True

        for i in range(n - 2, -1, -1):
            if odd_next[i] != -1:
                odd[i] = even[odd_next[i]]
            if even_next[i] != -1:
                even[i] = odd[even_next[i]]

        return sum(odd)
