class Solution(object):
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
            
        for m in range(1, 11):
            if m * k <= num and (m * k) % 10 == num % 10:
                return m
                
        return -1
