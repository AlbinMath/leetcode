from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 50
        ans = []
        
        for i, val in enumerate(nums):
            if val < 0:
                freq[val + 50] += 1
                
            if i >= k and nums[i - k] < 0:
                freq[nums[i - k] + 50] -= 1
                
            if i >= k - 1:
                count = 0
                beauty = 0
                for idx in range(50):
                    count += freq[idx]
                    if count >= x:
                        beauty = idx - 50
                        break
                ans.append(beauty)
                
        return ans
