from collections import Counter

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        even_counts = Counter(nums[0::2])
        odd_counts = Counter(nums[1::2])
        
        # Get top 2 (value, frequency) pairs, padded with (0, 0) for safety
        top_even = even_counts.most_common(2) + [(0, 0), (0, 0)]
        top_odd = odd_counts.most_common(2) + [(0, 0), (0, 0)]
        
        (e_val1, e_cnt1), (_, e_cnt2) = top_even[0], top_even[1]
        (o_val1, o_cnt1), (_, o_cnt2) = top_odd[0], top_odd[1]
        
        if e_val1 != o_val1:
            max_kept = e_cnt1 + o_cnt1
        else:
            max_kept = max(e_cnt1 + o_cnt2, e_cnt2 + o_cnt1)
            
        return n - max_kept
