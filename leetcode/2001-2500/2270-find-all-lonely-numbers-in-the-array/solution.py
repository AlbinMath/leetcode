from collections import Counter

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        
        return [
            num for num, count in freq.items()
            if count == 1 and (num - 1) not in freq and (num + 1) not in freq
        ]
