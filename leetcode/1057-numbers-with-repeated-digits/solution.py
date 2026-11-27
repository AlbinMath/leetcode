import math

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = [int(d) for d in str(n + 1)]
        L = len(digits)
        unique_count = 0
        
        for length in range(1, L):
            unique_count += 9 * math.perm(9, length - 1)
            
        seen = set()
        for i, curr_digit in enumerate(digits):
            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, curr_digit):
                if d not in seen:
                    unique_count += math.perm(9 - i, L - 1 - i)
                    
            if curr_digit in seen:
                break
            seen.add(curr_digit)
            
        return n - unique_count
