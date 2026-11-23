class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = [0] * 101
        max_freq = 0
        total = 0
        
        for num in nums:
            freq[num] += 1
            count = freq[num]
            
            if count > max_freq:
                max_freq = count
                total = count
            elif count == max_freq:
                total += count
                
        return total
