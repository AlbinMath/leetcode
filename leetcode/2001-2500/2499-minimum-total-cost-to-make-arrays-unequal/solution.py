from collections import defaultdict

class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        conflict_counts = defaultdict(int)
        total_conflicts = 0
        total_cost = 0
        max_freq = 0
        dominant_val = -1
        
        for i in range(n):
            if nums1[i] == nums2[i]:
                val = nums1[i]
                conflict_counts[val] += 1
                total_conflicts += 1
                total_cost += i
                
                if conflict_counts[val] > max_freq:
                    max_freq = conflict_counts[val]
                    dominant_val = val
                    
        excess = 2 * max_freq - total_conflicts
        
        if excess > 0:
            for i in range(n):
                if nums1[i] != nums2[i] and nums1[i] != dominant_val and nums2[i] != dominant_val:
                    total_cost += i
                    excess -= 1
                    if excess == 0:
                        break
                        
            if excess > 0:
                return -1
                
        return total_cost
