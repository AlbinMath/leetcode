class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1
            
        left_half = []
        
        for d in range(9, -1, -1):
            if d == 0 and not left_half:
                break
            pairs = freq[d] // 2
            if pairs > 0:
                left_half.append(str(d) * pairs)
                freq[d] %= 2
                
        mid = ""
        for d in range(9, -1, -1):
            if freq[d] > 0:
                mid = str(d)
                break
                
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]
