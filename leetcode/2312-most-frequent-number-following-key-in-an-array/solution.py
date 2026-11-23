from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counts = defaultdict(int)
        max_count = 0
        best_target = -1
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                counts[target] += 1
                if counts[target] > max_count:
                    max_count = counts[target]
                    best_target = target
                    
        return best_target
