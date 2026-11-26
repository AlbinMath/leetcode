from collections import Counter, defaultdict
from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_triplets(squares_arr: List[int], products_arr: List[int]) -> int:
            total = 0
            square_counts = Counter(squares_arr)
            
            for x, freq in square_counts.items():
                target = x * x
                seen = defaultdict(int)
                pairs = 0
                
                for y in products_arr:
                    if target % y == 0:
                        pairs += seen[target // y]
                    seen[y] += 1
                    
                total += freq * pairs
                
            return total

        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)
