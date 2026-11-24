from bisect import bisect_left
from typing import List

def _build():
    pals = []
    for half_len in range(1, 6):
        for h in range(10 ** (half_len - 1), 10 ** half_len):
            s = str(h)
            pals.append(int(s + s[::-1]))        # even length
            pals.append(int(s + s[-2::-1]))      # odd length (s[-2::-1] is empty when len 1)
    pals.append(1000000001)
    pals = sorted(set(pals))
    even = [p for p in pals if p % 2 == 0]
    odd = [p for p in pals if p % 2 == 1]
    return even, odd

_EVEN, _ODD = _build()

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            arr = _ODD if x & 1 else _EVEN
            k = bisect_left(arr, x)
            best = float('inf')
            if k < len(arr):
                best = arr[k] - x
            if k > 0:
                best = min(best, x - arr[k - 1])
            total += best // 2
        return total
