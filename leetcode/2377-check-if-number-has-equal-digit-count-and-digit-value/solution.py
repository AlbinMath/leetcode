class Solution:
    def digitCount(self, num: str) -> bool:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1
            
        for i, ch in enumerate(num):
            if freq[i] != int(ch):
                return False
                
        return True
