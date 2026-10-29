class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # n ends in ...01 or is the special case 3
                n -= 1
            else:
                # n ends in ...11 and n > 3
                n += 1
            steps += 1
            
        return steps
