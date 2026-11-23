from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        root = {}
        count = 0
        n = len(nums)
        for i in range(n):
            node = root
            div = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    div += 1
                    if div > k:
                        break
                nxt = node.get(nums[j])
                if nxt is None:
                    nxt = {}
                    node[nums[j]] = nxt
                    count += 1           # a new distinct subarray
                node = nxt
        return count
