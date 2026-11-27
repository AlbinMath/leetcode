class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        ans = 0
        
        for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            max_val = float('-inf')
            min_val = float('inf')
            
            for i, (a, b) in enumerate(zip(arr1, arr2)):
                curr = s1 * a + s2 * b + i
                if curr > max_val:
                    max_val = curr
                if curr < min_val:
                    min_val = curr
                    
            ans = max(ans, max_val - min_val)
            
        return ans
