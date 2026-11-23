from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        max_freq = 0
        best_num = -1
        
        for num in nums:
            if num % 2 == 0:
                freq[num] += 1
                if freq[num] > max_freq or (freq[num] == max_freq and num < best_num):
                    max_freq = freq[num]
                    best_num = num
                    
        return best_num
